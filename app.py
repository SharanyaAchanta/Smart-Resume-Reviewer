import streamlit as st
from utils.resume_parser import parse_resume, clean_text
from utils.analyze_resume import get_resume_feedback
from components.header import show_header
from components.suggestions import show_suggestions

st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")

show_header()

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    raw_text = parse_resume(uploaded_file)
    cleaned_text = clean_text(raw_text)

    st.subheader("Extracted Resume Text")
    st.write(cleaned_text)

    suggestions = get_resume_feedback(cleaned_text)
    show_suggestions(suggestions)
else:
    st.info("Please upload a PDF resume to get started.")
