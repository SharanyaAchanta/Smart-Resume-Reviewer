import streamlit as st
from pathlib import Path

def local_css():
    css_path = Path.cwd() / "static" / "css" / "globals.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("globals.css not found at " + str(css_path))
