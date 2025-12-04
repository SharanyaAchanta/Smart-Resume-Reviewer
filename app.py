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
from components.contributors import show_contributors_page

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

show_navbar("Analyzer")
show_header()

# Contributors button - CENTERED below header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("👥 View Contributors", use_container_width=True, type="primary"):
        st.session_state.show_contributors = True

# Show contributors if button clicked
if st.session_state.get("show_contributors", False):
    show_contributors_page()
    st.stop()
if "show_contributors" not in st.session_state:
    st.session_state.show_contributors = False


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

# Streamlit file uploader
uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf", help="Upload a PDF resume to analyze")



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

# --- Prevent duplicate processing due to Streamlit re-runs ---
# We use session_state to ensure we analyze once per uploaded file object
if "last_file_id" not in st.session_state:
    st.session_state.last_file_id = None

def _file_id(file):
    # file has attributes name and type; use size & lastModified if available
    try:
        return f"{file.name}-{file.size}-{getattr(file, 'lastModified', '')}"
    except Exception:
        return getattr(file, "name", str(file))

if uploaded_file:
    current_file_id = _file_id(uploaded_file)
    if st.session_state.last_file_id != current_file_id:
        st.session_state.last_file_id = current_file_id

        with st.spinner("⏳ Analyzing your resume... Please wait..."):
            # small delay to show spinner
            time.sleep(1)

            # Parse and analyze
            parsed = parse_resume(uploaded_file)  # returns dict per parser
            plain_text = parsed.get("plain_text", "")
            flat_text = parsed.get("flat_text", "")
            structured = parsed.get("structured", {})

            # show extracted plain text in textarea (exact, cleaned)
            st.subheader("📄 Extracted Resume Text — Cleaned (plain_text)")
            st.text_area("Extracted Resume Text", value=plain_text, height=350)

            # show flattened sectioned text
            st.subheader("📝 Structured (flat) view")
            st.text_area("Flat sections + bullets", value=flat_text, height=300)

            # show JSON structured output collapsed by default
            st.subheader("🔎 Parsed JSON Structure")
            st.json(structured)

            # call your analyzer with plain_text (the cleaned text)
            suggestions, resume_score, keyword_match = get_resume_feedback(plain_text, selected_role)
            show_suggestions(suggestions, resume_score, keyword_match)
    else:
        # same file re-run — avoid reprocessing
        st.info("Resume already analyzed — upload a different file to re-run analysis.")
        show_footer()
else:
    st.info("Please upload a PDF resume to get started.")
    show_footer()
