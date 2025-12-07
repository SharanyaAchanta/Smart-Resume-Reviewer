
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


﻿import streamlit as st

import json
import time


st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")


# --- LOAD LOCAL CSS ---
try:
    from components.styles import local_css
    local_css()
except Exception:
    pass


# --- IMPORT COMPONENTS ---
from utils.resume_parser import parse_resume
from utils.analyze_resume import get_resume_feedback
from components.header import show_header, show_navbar
from components.suggestions import show_suggestions
from components.contributors import show_contributors_page
from components.features import show_features_page

st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")

# --- PERSISTENT PRIVACY BANNER ---
st.markdown("""
<style>
.privacy-banner {
    position: fixed;
    top: auto; 
    bottom: 0;
    left: 0; right: 0;
    width: 100%;
    background: #1f77b4;
    color: white;
    text-align: center;
    font-size: 14px;
    padding: 8px 0;
    z-index: 9999;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.main .block-container {
    padding-top: 50px !important; /* adjust spacing so content is not hidden under banner */
}
</style>
<div class="privacy-banner">
    🔒 Privacy Notice: This tool processes your resume <strong>locally in memory</strong>. No files or personal information are stored.
</div>
""", unsafe_allow_html=True)


# Footer import with fallback
try:
    from components.footer import render_footer as show_footer
except Exception:
    try:
        from components.footer import show_footer
    except Exception:
        def show_footer():
            return None


# Upload card check
try:
    from components.upload_card import upload_card
    _HAS_UPLOAD_CARD = True
except Exception:
    _HAS_UPLOAD_CARD = False


# ✅ CRITICAL: Initialize ALL session state FIRST (fixes refresh issues)
if "show_contributors" not in st.session_state:
    st.session_state.show_contributors = False
if "show_features" not in st.session_state:
    st.session_state.show_features = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "Analyzer"
if "last_file_id" not in st.session_state:
    st.session_state.last_file_id = None
if "consent" not in st.session_state:
    st.session_state.consent = None  # None = not chosen, "all" = accept all, "essential" = essential only


# -----------------------------
# UPDATED COOKIE BANNER - STANDARD WEBSITE STYLE
# -----------------------------
def cookie_banner():
    st.markdown("""
    <style>
    .cookie-overlay {
        position: fixed;
        left: 0; right: 0; bottom: 0;
        width: 100%;
        z-index: 10000;
        display: flex;
        justify-content: center;
        padding: 15px 0;
        background: rgba(0,0,0,0.8);
    }
    .cookie-popup {
        background: linear-gradient(135deg, #2c2c2c 0%, #1e1e1e 100%);
        border-radius: 16px;
        padding: 24px 28px;
        max-width: 650px;
        width: 90%;
        color: #f0f0f0;
        text-align: left;
        box-shadow: 0 20px 40px rgba(0,0,0,0.6);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255,255,255,0.1);
    }
    .cookie-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 12px;
        color: #00d4aa;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .cookie-text {
        font-size: 14px;
        margin-bottom: 20px;
        line-height: 1.6;
        color: #e0e0e0;
    }
    .cookie-buttons {
        display: flex;
        justify-content: flex-end;
        gap: 12px;
        flex-wrap: wrap;
    }
    .cookie-btn {
        padding: 10px 24px;
        font-size: 14px;
        font-weight: 600;
        border-radius: 8px;
        cursor: pointer;
        border: none;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        min-width: 130px;
    }
    .accept-all-btn {
        background: linear-gradient(135deg, #00c853 0%, #00b140 100%);
        color: white;
    }
    .accept-all-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 8px 25px rgba(0,200,83,0.4);
    }
    .accept-essential-btn {
        background: transparent;
        color: #fff;
        border: 2px solid #4a4a4a;
    }
    .accept-essential-btn:hover {
        background: rgba(255,255,255,0.1);
        border-color: #00c853;
        color: #00c853;
    }
    @media (max-width: 768px) {
        .cookie-popup { padding: 20px 16px; margin: 0 10px; }
        .cookie-text { font-size: 13px; }
        .cookie-buttons { flex-direction: column-reverse; }
        .cookie-btn { width: 100%; margin-bottom: 8px; }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cookie-overlay">
        <div class="cookie-popup">
            <div class="cookie-title">🍪 We use cookies</div>
            <div class="cookie-text">
                This website uses <strong>essential cookies</strong> for core functionality and <strong>optional cookies</strong> 
                to improve your experience, analyze usage, and personalize content.
                <br><br>
                You can manage your preferences below. Learn more in our <a href="#" style="color: #00c853;">Privacy Policy</a>.
            </div>
            <div class="cookie-buttons">
    """, unsafe_allow_html=True)

    # Buttons positioned properly
    col1, col2 = st.columns([1, 1])
    with col1:
        accept_essential = st.button("Accept Essential", key="accept_essential", use_container_width=True)
    with col2:
        accept_all = st.button("Accept All", key="accept_all", use_container_width=True)

    st.markdown("""
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if accept_all:
        st.session_state.consent = "all"
        st.rerun()
    if accept_essential:
        st.session_state.consent = "essential"
        st.rerun()


# ✅ CONSENT CHECK - SHOWS ON HOME PAGE ONLY ONCE
if st.session_state.consent is None:
    cookie_banner()
    st.stop()


# ✅ GLOBAL STYLING - HEADER FULLY VISIBLE (FIXED!)
st.markdown("""
<style>
/* ✅ FIXED: Header fully visible - no hiding! */
header, .stAppHeader, .stAppToolbar { 
    display: none !important;
}

/* Main container spacing - header stays visible */
.block-container {  
    padding-bottom: 200px !important;
    text-align: center; 
    margin-top: 0 !important;
}

/* Mobile responsive */
@media (max-width: 768px) { 
    .block-container { 
        padding-top: 1.5rem !important; 
        padding-bottom: 220px !important; 
    } 
}

/* Button styling */
.stButton > button {
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 12px 28px !important;
}

/* Card styling */
.card {
    background: #ffffff;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

/* Text areas */
textarea, pre, .stTextArea, .stTextArea textarea { 
    text-align: left; 
    font-family: monospace; 
    font-size: 14px; 
}

/* File uploader styling */
[data-testid="stFileUploader"] {
    border: 2px solid rgba(80, 200, 120, 0.35) !important;
    background: linear-gradient(145deg, #131416, #1a1c1f) !important;
    padding: 30px !important;
    border-radius: 14px !important;
    transition: all 0.35s ease-in-out !important;
    cursor: pointer !important;
    margin: auto;
}
[data-testid="stFileUploader"] * { color: #e8f1f2 !important; }
[data-testid="stFileUploader"] svg { fill: #2ecc71 !important; width: 36px !important; height: 36px !important; }
[data-testid="stFileUploader"]:hover { 
    border-color: #2ecc71 !important; 
    box-shadow: 0px 0px 18px rgba(46, 204, 113, 0.25); 
    transform: translateY(-2px); 
}
[data-testid="stFileUploader"].drag-over { 
    border-color: #1abc9c !important; 
    box-shadow: 0px 0px 25px rgba(26, 188, 156, 0.35); 
    background: #1c1f21 !important; 
}

/* Consent info styling */
.stInfo { background-color: rgba(0,200,83,0.1) !important; border-left: 4px solid #00c853 !important; }
</style>
""", unsafe_allow_html=True)


# --- NAVBAR & HEADER (FULLY VISIBLE NOW) ---
show_navbar(active_page=st.session_state.current_page)
show_header()
st.markdown("<br><br>", unsafe_allow_html=True)  # Extra spacing for header visibility


# --- CONSENT STATUS DISPLAY ---
if st.session_state.consent == "essential":
    st.info("✅ **Essential cookies enabled.** Some optional features may be limited.")
elif st.session_state.consent == "all":
    st.info("✅ **All cookies enabled.** Full functionality available.")


# --- PAGE BUTTONS CENTERED ---
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("👥 View Contributors", use_container_width=True, type="primary"):
        st.session_state.show_contributors = True
        st.session_state.show_features = False
        st.session_state.current_page = "Contributors"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("✨ Features", use_container_width=True, type="primary"):
        st.session_state.show_features = True
        st.session_state.show_contributors = False
        st.session_state.current_page = "Features"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# --- SHOW CONTRIBUTORS / FEATURES ---
if st.session_state.show_contributors:
    show_contributors_page()
    if callable(show_footer):
        show_footer()
    st.stop()
if st.session_state.show_features:
    show_features_page()
    if callable(show_footer):
        show_footer()
    st.stop()


# --- LOAD JOB ROLES ---
try:
    with open("utils/job_roles.json", "r") as f:
        job_roles = json.load(f)
except Exception:
    job_roles = {"Default Role": "Default"}
    st.warning("Could not load utils/job_roles.json — using default role list.")


st.subheader("Choose Job Role")
selected_role = st.selectbox("Select the job you are applying for:", list(job_roles.keys()))


# --- PRIVACY NOTICE ---
st.info(
    "🔒 **Privacy Notice:** Your resume is processed **only in memory** and **never stored on the server**. "
    "No personal data is saved or logged."
)


# --- FILE UPLOADER ---
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)", type="pdf", help="Upload a PDF resume to analyze"
)


# --- DRAG-OVER JS ---
st.markdown("""
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
""", unsafe_allow_html=True)


# --- HELPER: FILE ID ---
def _file_id(file):
    try:
        return f"{file.name}-{file.size}-{getattr(file, 'lastModified', '')}"
    except Exception:
        return getattr(file, "name", str(file))


# --- RESUME ANALYSIS ---
if uploaded_file:
    current_file_id = _file_id(uploaded_file)
    if st.session_state.last_file_id != current_file_id:
        st.session_state.last_file_id = current_file_id

        with st.spinner("⏳ Analyzing your resume... Please wait..."):
            time.sleep(1)

        parsed = parse_resume(uploaded_file)
        plain_text = parsed.get("plain_text", "")
        flat_text = parsed.get("flat_text", "")
        structured = parsed.get("structured", {})

        # --- Display Extracted Text ---
        st.markdown("<div class='card'><h4>📄 Extracted Resume Text — Cleaned</h4></div>", unsafe_allow_html=True)
        st.text_area("Extracted Resume Text", value=plain_text, height=350)

        st.markdown("<div class='card'><h4>📝 Structured (flat) view</h4></div>", unsafe_allow_html=True)
        st.text_area("Flat sections + bullets", value=flat_text, height=300)

        st.markdown("<div class='card'><h4>🔎 Parsed JSON Structure</h4></div>", unsafe_allow_html=True)
        st.json(structured)

        suggestions, resume_score, keyword_match = get_resume_feedback(plain_text, selected_role)
        st.markdown("<div class='card'><h4>💡 Suggestions & Resume Score</h4></div>", unsafe_allow_html=True)
        show_suggestions(suggestions, resume_score, keyword_match)
    else:
        st.info("Resume already analyzed — upload a different file to re-run analysis.")
        if callable(show_footer):
            show_footer()
else:
    st.info("Please upload a PDF resume to get started.")
    if callable(show_footer):
        show_footer()
