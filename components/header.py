import streamlit as st

def show_header():
    st.markdown("<h1 class='fade-down' style='text-align: center;'>Smart Resume Analyzer 🧠📄</h1>", unsafe_allow_html=True)
    st.markdown("<h5 class='fade-down' style='text-align: center; color: gray;'>Upload your resume (PDF) and get instant feedback!</h5>", unsafe_allow_html=True)
