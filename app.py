import streamlit as st
import json
import time
from utils.resume_parser import parse_resume, clean_text
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
    # 🔥 Add Loading Spinner
    with st.spinner("⏳ Analyzing your resume... Please wait..."):

         # Force delay so spinner is visible
        time.sleep(2)

        raw_text = parse_resume(uploaded_file)
        time.sleep(1)

        cleaned_text = clean_text(raw_text)
        time.sleep(1)

        st.subheader("Extracted Resume Text")
        st.write(cleaned_text)

        time.sleep(1)
        suggestions, resume_score, keyword_match = get_resume_feedback(cleaned_text, selected_role)
        show_suggestions(suggestions, resume_score, keyword_match)
else:
    st.info("Please upload a PDF resume to get started.")
