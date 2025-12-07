# app.py (replace the upload handling part)
import streamlit as st

# Theme toggle
theme = st.sidebar.radio("Theme Mode:", ["Light", "Dark"])

if theme == "Dark":
    dark_css = """
        <style>
        body { background-color: #0e1117; color: white; }
        .stApp { background-color: #0e1117; }
        </style>
    """
    st.markdown(dark_css, unsafe_allow_html=True)


import json
import time
from utils.resume_parser import parse_resume
from utils.analyze_resume import get_resume_feedback
from components.header import show_header
from components.suggestions import show_suggestions

st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")

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


show_header()

# Load job roles
with open("utils/job_roles.json", "r") as f:
    job_roles = json.load(f)

st.subheader("Choose Job Role")
selected_role = st.selectbox("Select the job you are applying for:", list(job_roles.keys()))

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

# --- Drag-over JS to highlight uploader box ---
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

if uploaded_file:
    with st.spinner("⏳ Analyzing your resume... Please wait..."):
        # small delay to show spinner
        time.sleep(1)

        parsed = parse_resume(uploaded_file)  # returns dict per new parser
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
    st.info("Please upload a PDF resume to get started.")
