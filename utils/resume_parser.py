# utils/resume_parser.py
import fitz  # PyMuPDF
import re
import io
from collections import defaultdict
from typing import List, Dict

# Optional fallbacks
try:
    import pdfplumber
except Exception:
    pdfplumber = None

try:
    from pdf2image import convert_from_bytes
    import pytesseract
    OCR_AVAILABLE = True
except Exception:
    OCR_AVAILABLE = False


# -----------------------
# Low-level helpers
# -----------------------

# Fix common PDF ligature / weird Unicode extracted characters
UNICODE_FIX_MAP = {
    "Ɵ": "ti",
    "Ŧ": "T",
    "Ŋ": "N",
    "ƞ": "n",
    "Ō": "o",
    "ō": "o",
    "ſ": "s",
    "ﬀ": "ff",
    "ﬁ": "fi",
    "ﬂ": "fl",
    "ﬃ": "ffi",
    "ﬄ": "ffl",
    "ﬅ": "ft",
    "ﬆ": "st",
    "": "-",     # fancy bullet
    "": "-",     # bullet
    "•": "•",     # preserve real bullet
}


def normalize_unicode_characters(text: str) -> str:
    """Fix broken unicode from stylized PDFs (ligatures, mis-encodings)."""
    for bad, good in UNICODE_FIX_MAP.items():
        text = text.replace(bad, good)
    return text

def _normalize_whitespace(s: str) -> str:
    s = s.replace('\r', '\n')
    s = re.sub(r'\n{3,}', '\n\n', s)  # collapse many blank lines
    s = re.sub(r'[ \t]+', ' ', s)
    s = s.strip()
    return s


def _fix_hyphenation(text: str) -> str:
    # remove hyphen+newline splits (word-breaking at line endings)
    text = re.sub(r'-\n\s*', '', text)
    # convert single newline within paragraph to space
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    # collapse multiple spaces
    text = re.sub(r' +', ' ', text)
    return text


def _is_bullet_token(tok: str) -> bool:
    tok = (tok or "").strip()
    return bool(re.match(r'^[-•\u2022\u25E6\u2043]|\d+[\.\)]', tok))


def _merge_blocks(blocks: List[dict]) -> List[dict]:
    """
    Merge close blocks (helps join broken lines/columns)
    Blocks expected to have keys: bbox=(x0,y0,x1,y1), text (str)
    """
    if not blocks:
        return blocks
    merged = []
    blocks_sorted = sorted(blocks, key=lambda b: (round(b['bbox'][1]), round(b['bbox'][0])))
    for b in blocks_sorted:
        if not merged:
            merged.append(b.copy())
            continue
        last = merged[-1]
        # vertical gap
        y_gap = b['bbox'][1] - last['bbox'][3]
        x_diff = abs(b['bbox'][0] - last['bbox'][0])
        # if close vertically and near same x, join as same paragraph line
        if 0 <= y_gap < 18 and x_diff < 30:
            last['text'] = (last['text'].rstrip() + ' ' + b['text'].lstrip()).strip()
            last['bbox'] = (
                min(last['bbox'][0], b['bbox'][0]),
                min(last['bbox'][1], b['bbox'][1]),
                max(last['bbox'][2], b['bbox'][2]),
                max(last['bbox'][3], b['bbox'][3]),
            )
        else:
            merged.append(b.copy())
    return merged


# -----------------------
# Extractors
# -----------------------
def _extract_blocks_with_pymupdf(file_bytes: bytes):
    doc = fitz.open(stream=file_bytes, filetype='pdf')
    blocks = []
    for pno, page in enumerate(doc, start=1):
        d = page.get_text("dict")
        for block in d.get("blocks", []):
            if block.get("type") != 0:
                continue
            # gather lines
            lines = []
            x0, y0, x1, y1 = block.get("bbox", (0, 0, 0, 0))
            for line in block.get("lines", []):
                line_text = ""
                for span in line.get("spans", []):
                    line_text += span.get("text", "")
                if line_text.strip():
                    lines.append(line_text.strip())
            text = "\n".join(lines).strip()
            if text:
                blocks.append({
                    "page": pno,
                    "bbox": (x0, y0, x1, y1),
                    "text": text
                })
    # try to merge small fragments
    merged = _merge_blocks(blocks)
    return merged


def _extract_text_pdfplumber(file_bytes: bytes):
    if not pdfplumber:
        return ""
    out = []
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            t = page.extract_text() or ""
            out.append(t)
    return "\n\n".join(out)


def _ocr_pdf_bytes(file_bytes: bytes):
    """Return OCR text if available."""
    if not OCR_AVAILABLE:
        return ""
    pages = convert_from_bytes(file_bytes, dpi=300)
    texts = []
    for img in pages:
        texts.append(pytesseract.image_to_string(img, lang='eng'))
    return "\n\n".join(texts)


# -----------------------
# High-level parsing heuristics
# -----------------------
def _blocks_to_plain(blocks: List[dict]) -> str:
    if not blocks:
        return ""
    lines = []
    for b in blocks:
        # split block's text into lines
        for ln in b['text'].splitlines():
            ln2 = ln.strip()
            if ln2:
                lines.append(ln2)
        # add separator between blocks to preserve paragraphs
        lines.append("")
    merged = "\n".join(lines)
    merged = _normalize_whitespace(merged)
    merged = _fix_hyphenation(merged)
    return merged


def _smart_structure_from_plain(plain: str) -> Dict:
    """
    Heuristic structural parser: split into sections using heading patterns,
    detect Experience sections and parse role/company/dates + bullets.
    """
    lines = [ln.strip() for ln in plain.splitlines() if ln.strip() != ""]
    sections = defaultdict(list)
    current = "GENERAL"
    heading_regex = re.compile(r'^[A-Z][A-Z\s]{2,}$')  # all-caps-ish heading
    # also allow common headings case-insensitive
    known_headings = {"EXPERIENCE", "WORK EXPERIENCE", "EDUCATION", "SKILLS", "PROJECTS", "SUMMARY", "ABOUT", "CONTACT", "COURSES", "HOBBIES", "ACHIEVEMENTS"}

    for ln in lines:
        # detect explicit "Skills:" style headers
        if re.match(r'^(Skills|Skills:|SKILLS)\b', ln, re.I):
            current = "SKILLS"
            continue
        # all-caps heading or known heading word
        clean_ln = re.sub(r'[^\w\s]', '', ln).strip()
        if heading_regex.match(clean_ln) or clean_ln.upper() in known_headings:
            current = clean_ln.upper()
            sections[current]  # ensure exists
            continue
        sections[current].append(ln)

    # Now post-process certain sections
    structured = {}
    for sec, items in sections.items():
        if sec in ("EXPERIENCE", "WORK EXPERIENCE"):
            structured["EXPERIENCE"] = _parse_experience_block(items)
        elif sec == "EDUCATION":
            structured["EDUCATION"] = _parse_education_block(items)
        elif sec == "SKILLS":
            structured["SKILLS"] = _parse_skills_block(items)
        elif sec in ("PROJECTS",):
            structured["PROJECTS"] = _parse_bulleted_block(items)
        elif sec in ("SUMMARY", "ABOUT", "GENERAL"):
            # combine into summary if short or keep as list otherwise
            txt = " ".join(items)
            structured["SUMMARY"] = txt.strip()
        else:
            # default: keep as list
            structured[sec] = _parse_bulleted_block(items)
    return structured


def _parse_bulleted_block(lines: List[str]) -> List[str]:
    out = []
    buffer = []
    for ln in lines:
        if _is_bullet_token(ln[:2]):
            out.append(ln.lstrip('-• ').strip())
        else:
            # if line is long, treat as paragraph
            out.append(ln)
    return out


def _parse_skills_block(lines: List[str]) -> List[str]:
    text = " ".join(lines)
    # try to split by commas or bullets or slashes
    candidates = re.split(r'[,/•\n]|;|-', text)
    skills = []
    for c in candidates:
        c = c.strip()
        if len(c) >= 2 and len(c) < 40:
            # filter out numbers and stray words
            if re.search(r'[A-Za-z]', c):
                skills.append(c)
    # dedupe preserve order
    seen = set()
    res = []
    for s in skills:
        lower = s.lower()
        if lower not in seen:
            seen.add(lower)
            res.append(s)
    return res


def _parse_education_block(lines: List[str]) -> List[dict]:
    # naive: find lines that look like degree/institute/year combos
    results = []
    cur = {}
    for ln in lines:
        # year range pattern
        yr = re.search(r'(\b20\d{2}\b|\b19\d{2}\b|\b\d{4}\b)', ln)
        if yr and cur:
            # finalize previous
            cur['note'] = cur.get('note', '').strip()
            results.append(cur)
            cur = {}
        # heuristics: if contains 'University' or 'Institute' or 'School'
        if re.search(r'\b(University|Institute|College|School|Baccalaureate|Bachelor|Master|B\.Tech|BTech|MBA|GL Bajaj)\b', ln, re.I):
            if cur:
                # store previous then new
                results.append(cur)
                cur = {}
            cur['institution'] = ln
        else:
            cur['note'] = (cur.get('note', '') + " " + ln).strip()
    if cur:
        results.append(cur)
    return results


def _parse_experience_block(lines: List[str]) -> List[dict]:
    """
    Heuristic parser for EXPERIENCE lines.
    Looks for patterns like:
      Role | Company | Date-range
      Role, Company — Date
    Followed by bullet lines for points (lines starting with '-' or '•' or starting with indent).
    """
    entries = []
    cur = None
    for ln in lines:
        # If this line looks like a role/company/date header
        # common separators: ' | ', ' - ', '—', '–'
        header_match = re.split(r'\s[\|\-–—]\s|\s{2,}', ln)
        # header_match is list of chunks
        if len(header_match) >= 2 and re.search(r'\d{4}|\bPresent\b|\bPresent\b', ln, re.I):
            # treat this as new experience header
            if cur:
                entries.append(cur)
            cur = {"role": header_match[0].strip(), "company": header_match[1].strip() if len(header_match) > 1 else "", "duration": "", "points": []}
            # try to extract duration from the full line
            dur = re.search(r'(\b\d{4}\b(?:\s*[-–—]\s*\b(?:Present|\d{4})\b)?)', ln)
            if dur:
                cur["duration"] = dur.group(0)
            continue

        # If line contains a year-range (but didn't match above)
        year_range = re.search(r'\b(19|20)\d{2}\b(?:\s*[-–—]\s*\b(?:Present|\d{4})\b)?', ln)
        if year_range and ("," in ln or "@" in ln or "-" in ln):
            # try to split role/company and duration
            parts = re.split(r'\s[\|\-–—]\s', ln)
            if cur:
                # finalize previous, start new
                entries.append(cur)
            cur = {"role": parts[0].strip(), "company": (parts[1].strip() if len(parts) > 1 else ""), "duration": year_range.group(0), "points": []}
            continue

        # bullets or indented lines -> add to points
        if _is_bullet_token(ln[:2]) or ln.startswith(("•", "-", "—")):
            if not cur:
                # If no header, create a generic entry
                cur = {"role": "", "company": "", "duration": "", "points": []}
            cur['points'].append(re.sub(r'^[-•\u2022\.\s]+', '', ln).strip())
            continue

        # If regular sentence and we have current entry, attach as explanation
        if cur:
            # long sentences often belong to points
            if len(ln.split()) > 6:
                cur['points'].append(ln)
            else:
                # maybe short details e.g., "Remote" or "Full-time"
                cur.setdefault('meta', []).append(ln)
        else:
            # not part of experience; skip
            continue

    if cur:
        entries.append(cur)
    # post-process: collapse empty entries
    final = []
    for e in entries:
        if not e.get('role') and not e.get('company') and not e.get('points'):
            continue
        final.append(e)
    return final


# -----------------------
# Public API
# -----------------------
def parse_resume(file_obj) -> dict:
    """
    Accepts a file-like object (e.g. Streamlit uploaded_file).
    Returns:
      {
        "plain_text": "...",   # cleaned
        "flat_text": "...",    # paragraphs with some structure
        "structured": { ... }, # mode-B JSON structure
        "skills": [ ... ]
      }
    """
    file_obj.seek(0)
    file_bytes = file_obj.read()

    # 1) try PyMuPDF block extraction
    try:
        blocks = _extract_blocks_with_pymupdf(file_bytes)
        plain = _blocks_to_plain(blocks)
    except Exception:
        blocks = []
        plain = ""

    # 2) if plain too short, fallback to pdfplumber text extraction
    if (not plain or len(plain.strip()) < 80) and pdfplumber is not None:
        try:
            plumber_text = _extract_text_pdfplumber(file_bytes)
            if len(plumber_text.strip()) > len(plain):
                plain = plumber_text
        except Exception:
            pass

    # 3) OCR fallback
    if (not plain or len(plain.strip()) < 200) and OCR_AVAILABLE:
        try:
            ocr_text = _ocr_pdf_bytes(file_bytes)
            if len(ocr_text.strip()) > len(plain):
                plain = ocr_text
        except Exception:
            pass

    # final cleaning
    # final cleaning + unicode fix
    plain_text = _normalize_whitespace(plain)
    plain_text = normalize_unicode_characters(plain_text)
    plain_text = _fix_hyphenation(plain_text)


    # build structured JSON from plain text
    structured = _smart_structure_from_plain(plain_text)

    # try to assemble flat_text for human display (sections + bullets)
    flat_parts = []
    for k, v in structured.items():
        flat_parts.append(f"### {k}")
        if isinstance(v, str):
            flat_parts.append(v)
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    # for experience entries
                    role = item.get('role', '')
                    comp = item.get('company', '')
                    dur = item.get('duration', '')
                    flat_parts.append(f"{role} | {comp} | {dur}".strip())
                    for p in item.get('points', []):
                        flat_parts.append(f"- {p}")
                else:
                    flat_parts.append(f"- {item}")
        else:
            flat_parts.append(str(v))
        flat_parts.append("")  # spacer

    flat_text = "\n".join(flat_parts).strip()

    # skills lumps
    skills = structured.get("SKILLS") or []

    return {
        "plain_text": plain_text,
        "flat_text": flat_text,
        "structured": structured,
        "skills": skills
    }


# small test-run when module run directly
if __name__ == "__main__":
    import sys, json
    if len(sys.argv) > 1:
        path = sys.argv[1]
        with open(path, "rb") as f:
            out = parse_resume(f)
            print("PLAIN\n", out["plain_text"][:1000])
            print("\nFLAT\n", out["flat_text"][:2000])
            print("\nSTRUCTURED\n", json.dumps(out["structured"], indent=2)[:4000])
    else:
        print("Usage: python utils/resume_parser.py resume.pdf")
