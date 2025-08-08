import streamlit as st

def show_header():
    st.markdown("<h1 style='text-align: center;'>Smart Resume Analyzer 🧠📄</h1>", unsafe_allow_html=True)
    st.write("Upload your resume (PDF) and get instant feedback!")
