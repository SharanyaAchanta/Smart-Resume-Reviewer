# app.py (clean, fixed indentation, robust imports)
import streamlit as st
import json
import time

st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")

try:
    from components.styles import local_css
    local_css()
except Exception:
    pass

from utils.resume_parser import parse_resume
from utils.analyze_resume import get_resume_feedback
from components.header import show_header, show_navbar
from components.suggestions import show_suggestions

try:
    from components.footer import render_footer as show_footer
except Exception:
    try:
        from components.footer import show_footer
    except Exception:
        def show_footer():
            return None

try:
    from components.upload_card import upload_card
    _HAS_UPLOAD_CARD = True
except Exception:
    _HAS_UPLOAD_CARD = False

show_navbar()
show_header()

st.markdown(
    """
<style>
header, .stAppHeader, .stAppToolbar {
    display: none !important;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<style>
.block-container { padding-top: 1rem; }
[data-testid="stFileUploader"] {
    border: 2px solid rgba(80, 200, 120, 0.35) !important;
    background: linear-gradient(145deg, #131416, #1a1c1f) !important;
    padding: 30px !important;
    border-radius: 14px !important;
    transition: all 0.35s ease-in-out !important;
    cursor: pointer !important;
}
[data-testid="stFileUploader"] * { color: #e8f1f2 !important; }
[data-testid="stFileUploader"] svg { fill: #2ecc71 !important; width: 36px !important; height: 36px !important; }
[data-testid="stFileUploader"]:hover { border-color: #2ecc71 !important; box-shadow: 0px 0px 18px rgba(46, 204, 113, 0.25); transform: translateY(-2px); }
[data-testid="stFileUploader"].drag-over { border-color: #1abc9c !important; box-shadow: 0px 0px 25px rgba(26, 188, 156, 0.35); background: #1c1f21 !important; }
[data-testid="stFileUploader"] button {
    background-color: rgba(255,255,255,0.06) !important;
    color: white !important;
    border-radius: 8px !important;
    padding: 6px 12px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}
</style>
""",
    unsafe_allow_html=True,
)

try:
    with open("utils/job_roles.json", "r") as f:
        job_roles = json.load(f)
except Exception:
    job_roles = {"Default Role": "Default"}
    st.warning("Could not load utils/job_roles.json — using default role list.")

st.subheader("Choose Job Role")
selected_role = st.selectbox("Select the job you are applying for:", list(job_roles.keys()))

uploaded_file_legacy = st.file_uploader("Upload Resume (PDF)", type="pdf")
uploaded = None

if _HAS_UPLOAD_CARD:
    try:
        uploaded_from_card = upload_card()
        if uploaded_from_card:
            uploaded = uploaded_from_card
    except TypeError:
        pass
    except Exception as e:
        st.warning(f"Upload card component error: {e}")

if not uploaded:
    uploaded = uploaded_file_legacy or st.session_state.get("resume_uploader")

st.markdown(
    """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const uploader = window.parent.document.querySelector('[data-testid="stFileUploader"]');
    if (uploader) {
        document.addEventListener('dragover', () => { uploader.classList.add('drag-over'); });
        document.addEventListener('dragleave', () => { uploader.classList.remove('drag-over'); });
        document.addEventListener('drop', () => { uploader.classList.remove('drag-over'); });
    }
});
</script>
""",
    unsafe_allow_html=True,
)

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

show_footer()

