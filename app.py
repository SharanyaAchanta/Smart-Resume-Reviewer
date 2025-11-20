# app.py (replace the upload handling part)
import streamlit as st
import json
import time
from utils.resume_parser import parse_resume
from utils.analyze_resume import get_resume_feedback
from components.header import show_header
from components.suggestions import show_suggestions

st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")

show_header()

# Load job roles
with open("utils/job_roles.json", "r") as f:
    job_roles = json.load(f)

st.subheader("Choose Job Role")
selected_role = st.selectbox("Select the job you are applying for:", list(job_roles.keys()))

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

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
