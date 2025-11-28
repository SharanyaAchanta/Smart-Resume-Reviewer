# app.py (fixed ordering + robust imports)
import streamlit as st
import json
import time

# set page config first (required before any streamlit element)
st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")

# styles loader (must be called after set_page_config)
from components.styles import local_css
local_css()

# app utilities / components
from utils.resume_parser import parse_resume
from utils.analyze_resume import get_resume_feedback
from components.header import show_header, show_navbar
from components.suggestions import show_suggestions

# footer import: try common names and fall back
try:
    from components.footer import render_footer as show_footer
except Exception:
    try:
        from components.footer import show_footer
    except Exception:
        def show_footer():
            pass

# optional new upload card component (if present)
try:
    from components.upload_card import upload_card
    _HAS_UPLOAD_CARD = True
except Exception:
    _HAS_UPLOAD_CARD = False

# Render navigation / header after page config + css
show_navbar()
show_header()

# Hide Streamlit top header / toolbar so your navbar is the only top bar
st.markdown("""
<style>
/* hide Streamlit header and top toolbar */
header, .stAppHeader, .stAppToolbar {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# --- PREMIUM File Uploader Styling (Dark Neon Glow) ---
st.markdown("""
<style>
/* Outer container (removes Streamlit’s extra padding) */
.block-container {
    padding-top: 1rem;
}

/* Premium Upload Box */
[data-testid="stFileUploader"] {
    border: 2px solid rgba(80, 200, 120, 0.35) !important;
    background: linear-gradient(145deg, #131416, #1a1c1f) !important;
    padding: 30px !important;
    border-radius: 14px !important;
    transition: all 0.35s ease-in-out !important;
    cursor: pointer !important;
}

/* Icon + text color */
[data-testid="stFileUploader"] * {
    color: #e8f1f2 !important;
}

/* Make the cloud icon brighter */
[data-testid="stFileUploader"] svg {
    fill: #2ecc71 !important;
    width: 36px !important;
    height: 36px !important;
}

/* Hover (Neon Glow) */
[data-testid="stFileUploader"]:hover {
    border-color: #2ecc71 !important;
    box-shadow: 0px 0px 18px rgba(46, 204, 113, 0.25);
    transform: translateY(-2px);
}

/* Dragging file over the box */
[data-testid="stFileUploader"].drag-over {
    border-color: #1abc9c !important;
    box-shadow: 0px 0px 25px rgba(26, 188, 156, 0.35);
    background: #1c1f21 !important;
}

/* Browse files button sleek look */
[data-testid="stFileUploader"] button {
    background-color: rgba(255,255,255,0.06) !important;
    color: white !important;
    border-radius: 8px !important;
    padding: 6px 12px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}
</style>
""", unsafe_allow_html=True)

# Load job roles safely
try:
    with open("utils/job_roles.json", "r") as f:
        job_roles = json.load(f)
except Exception:
    job_roles = {"Default Role": "Default"}
    st.warning("Could not load utils/job_roles.json — using default role list.")

st.subheader("Choose Job Role")
selected_role = st.selectbox("Select the job you are applying for:", list(job_roles.keys()))

# --- Render upload UI ---
uploaded_file_legacy = st.file_uploader("Upload Resume (PDF)", type="pdf")
uploaded = None

# If upload_card component available, render it and try to capture return value
if _HAS_UPLOAD_CARD:
    try:
        uploaded_from_card = upload_card()
        if uploaded_from_card:
            uploaded = uploaded_from_card
    except TypeError:
        # upload_card might not return anything (older version). fallback below.
        pass
    except Exception as e:
        st.warning(f"Upload card component error: {e}")

# fallback to legacy uploader if nothing from upload_card
if not uploaded:
    uploaded = uploaded_file_legacy or st.session_state.get("resume_uploader")

# --- Drag-over JS to highlight uploader box (keeps working for legacy uploader) ---
st.markdown("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    const uploader = window.parent.document.querySelector('[data-testid="stFileUploader"]');

    if (uploader) {
        document.addEventListener('dragover', () => {
            uploader.classList.add('drag-over');
        });

        document.addEventListener('dragleave', () => {
            uploader.classList.remove('drag-over');
        });

        document.addEventListener('drop', () => {
            uploader.classList.remove('drag-over');
        });
    }
});
</script>
""", unsafe_allow_html=True)

# --- Resume processing flow ---
if uploaded:
    with st.spinner("⏳ Analyzing your resume... Please wait..."):
        time.sleep(1)
        parsed = parse_resume(uploaded)
        plain_text = parsed.get("plain_text", "")
        flat_text = parsed.get("flat_text", "")
        structured = parsed.get("structured", {})

        st.subheader("📄 Extracted Resume Text — Cleaned (plain_text)")
        st.text_area("Extracted Resume Text", value=plain_text, height=350)

        st.subheader("📝 Structured (flat) view")
        st.text_area("Flat sections + bullets", value=flat_text, height=300)

        st.subheader("🔎 Parsed JSON Structure")
        st.json(structured)

        suggestions, resume_score, keyword_match = get_resume_feedback(plain_text, selected_role)
        show_suggestions(suggestions, resume_score, keyword_match)
else:
    st.info("Please upload a PDF resume to get started.")

# Ensure footer renders regardless of upload state
show_footer()
