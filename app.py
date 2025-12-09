
import streamlit as st
import json
import time

# Theme from session (controlled by custom sidebar in header.py)
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"
theme = st.session_state.theme


if theme == "Dark":
    dark_css = """
        <style>
        body { background-color: #0e1117; color: white; }
        .stApp { background-color: #0e1117; }
        </style>
    """
    st.markdown(dark_css, unsafe_allow_html=True)

st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")

# --- LOADING SCREEN WITH ANIMATION ---
if "page_loaded" not in st.session_state:
    st.session_state.page_loaded = False

# Show loading screen on first load
if not st.session_state.page_loaded:
    # Full page loading overlay (Dark theme preview)
    st.markdown("""
    <style>
    .loading-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 99999;
        font-family: 'Segoe UI', -apple-system, sans-serif;
    }
    .loading-spinner {
        width: 60px;
        height: 60px;
        border: 6px solid rgba(255,255,255,0.1);
        border-top: 6px solid #00d4aa;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin-bottom: 24px;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .loading-title {
        font-size: 28px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 8px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }
    .loading-subtitle {
        font-size: 16px;
        color: rgba(255,255,255,0.85);
        margin-bottom: 16px;
    }
    .loading-dots {
        display: flex;
        gap: 4px;
    }
    .dot {
        width: 10px;
        height: 10px;
        background: rgba(0,212,170,0.8);
        border-radius: 50%;
        animation: bounce 1.4s infinite ease-in-out;
    }
    .dot:nth-child(1) { animation-delay: -0.32s; }
    .dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes bounce {
        0%, 80%, 100% { transform: scale(0); }
        40% { transform: scale(1); }
    }
    </style>
    
    <div class="loading-overlay">
        <div class="loading-spinner"></div>
        <div class="loading-title">Smart Resume Analyzer</div>
        <div class="loading-subtitle">Loading your AI-powered resume tool...</div>
        <div class="loading-dots">
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Simulate loading time and mark as loaded
    time.sleep(2.5)
    st.session_state.page_loaded = True
    st.rerun()
    st.stop()

# --- HIDE STREAMLIT DEFAULT LOADING ---
st.markdown("""
<style>
/* Hide Streamlit loading spinner */
[data-testid="stSpinnerOverlay"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# --- LOAD LOCAL CSS ---
try:
    from components.styles import local_css
    local_css()
except Exception:
    pass

# --- IMPORT COMPONENTS ---
from utils.resume_parser import parse_resume
from utils.analyze_resume import get_resume_feedback
from components.header import show_header, show_sidebar_navbar
from components.suggestions import show_suggestions
from components.contributors import show_contributors_page
from components.features import show_features_page
from components import resume_tips
from components.login import show_login


# ✅ CRITICAL: Initialize ALL session state FIRST - DARK MODE DEFAULT
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"  # 🛑 CHANGED: Dark is now default
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
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_login_modal" not in st.session_state:
    st.session_state.show_login_modal = False

# ✅ ROUTE TO RESUME TIPS PAGE
if st.session_state.current_page == "Resume Tips":
    resume_tips.main()  # components/resume_tips.py must define main()
    st.stop()

# Apply CSS overrides based on theme - DARK MODE FIRST
if st.session_state.theme == "Dark":
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #0e1117 !important;
            color: #e8f1f2 !important;
        }
        .card {
            background: #1b1f24 !important;
            color: #e8f1f2 !important;
        }
        [data-testid="stFileUploader"] {
            border: 2px solid rgba(80, 200, 120, 0.35) !important;
            background: linear-gradient(145deg, #131416, #1a1c1f) !important;
            padding: 30px !important;
            border-radius: 14px !important;
            transition: all 0.35s ease-in-out !important;
            cursor: pointer !important;
            margin: auto;
        }
        [data-testid="stFileUploader"] * {
            color: #e8f1f2 !important;
        }
        [data-testid="stFileUploader"] svg {
            fill: #2ecc71 !important;
            width: 36px !important;
            height: 36px !important;
        }
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
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #fafbfc !important;
            color: #1a202c !important;
        }
        .card {
            background: #f7fafc !important;
            color: #1a202c !important;
            border: 1px solid #e2e8f0 !important;
        }
        [data-testid="stFileUploader"] {
            border: 2px solid rgba(59, 130, 246, 0.3) !important;
            background: linear-gradient(145deg, #f8fafc, #edf2f7) !important;
            padding: 30px !important;
            border-radius: 14px !important;
            transition: all 0.35s ease-in-out !important;
            cursor: pointer !important;
            margin: auto;
        }
        [data-testid="stFileUploader"] * {
            color: #2d3748 !important;
        }
        [data-testid="stFileUploader"] svg {
            fill: #4299e1 !important;
            width: 36px !important;
            height: 36px !important;
        }
        [data-testid="stFileUploader"]:hover {
            border-color: #3182ce !important;
            box-shadow: 0px 0px 18px rgba(59, 130, 246, 0.25);
            transform: translateY(-2px);
        }
        [data-testid="stFileUploader"].drag-over {
            border-color: #2b6cb0 !important;
            box-shadow: 0px 0px 25px rgba(59, 130, 246, 0.35);
            background: #e6f3ff !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# [Rest of your existing code continues unchanged from here...]
# --- PERSISTENT PRIVACY BANNER ---
st.markdown(
    """
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
    padding-top: 50px !important;
}
</style>
<div class="privacy-banner">
    🔒 Privacy Notice: This tool processes your resume <strong>locally in memory</strong>. No files or personal information are stored.
</div>
""",
    unsafe_allow_html=True,
)

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

# -----------------------------
# UPDATED COOKIE BANNER - STANDARD WEBSITE STYLE
# -----------------------------
def cookie_banner():
    st.markdown(
        """
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
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
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
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        accept_essential = st.button("Accept Essential", key="accept_essential", use_container_width=True)
    with col2:
        accept_all = st.button("Accept All", key="accept_all", use_container_width=True)

    st.markdown(
        """
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

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
st.markdown(
    """
<style>
header, .stAppHeader, .stAppToolbar { 
    display: none !important;
}
.block-container {  
    padding-bottom: 200px !important;
    text-align: center; 
    margin-top: 0 !important;
}
@media (max-width: 768px) { 
    .block-container { 
        padding-top: 1.5rem !important; 
        padding-bottom: 220px !important; 
    } 
}
.stButton > button {
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 12px 28px !important;
}
.card {
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}
textarea, pre, .stTextArea, .stTextArea textarea { 
    text-align: left; 
    font-family: monospace; 
    font-size: 14px; 
}
.stInfo { background-color: rgba(0,200,83,0.1) !important; border-left: 4px solid #00c853 !important; }
</style>
""",
    unsafe_allow_html=True,
)

# --- SIDEBAR NAVBAR & HEADER ---
# --- SIDEBAR NAVBAR & HEADER ---
show_sidebar_navbar(active_page=st.session_state.current_page)
show_header()

# LOGIN MODAL TRIGGER (Single source of truth)
if st.session_state.get("show_login_modal", False):
    from components.login import show_login
    show_login()
    
    # BUTTONS TOGETHER AT BOTTOM
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("❌ Close", key="close_modal", use_container_width=True):
            st.session_state.show_login_modal = False
            st.rerun()
    with col2:
        if st.button("✅ Login Success", key="login_success", use_container_width=True):
            st.session_state.logged_in = True
            st.session_state.show_login_modal = False
            st.rerun()
    st.markdown("---")


st.markdown("<br><br>", unsafe_allow_html=True)

# --- CONSENT STATUS DISPLAY ---
if st.session_state.consent == "essential":
    st.info("✅ **Essential cookies enabled.** Some optional features may be limited.")
elif st.session_state.consent == "all":
    st.info("✅ **All cookies enabled.** Full functionality available.")


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
    
# ---- PERFECT BOTTOM LOGIN MODAL ----
if st.session_state.get("show_login_modal", False):
    from components.login import show_login
    show_login()
    
    # BUTTONS TOGETHER AT BOTTOM
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("❌ Close", key="close_modal", use_container_width=True):
            st.session_state.show_login_modal = False
            st.rerun()
    with col2:
        if st.button("✅ Login Success", key="login_success", use_container_width=True):
            st.session_state.logged_in = True
            st.session_state.show_login_modal = False
            st.rerun()
    st.markdown("---")

# --- LOAD JOB ROLES ---
try:
    with open("utils/job_roles.json", "r") as f:
        job_roles = json.load(f)
except Exception:
    job_roles = {"Default Role": "Default"}
    st.warning("Could not load utils/job_roles.json — using default role list.")

st.subheader("Choose Job Role")
categories = list(job_roles.keys()) if isinstance(job_roles, dict) else ["Default Role"]
selected_category = st.selectbox("Select Job Category:", categories)

if isinstance(job_roles, dict) and selected_category in job_roles:
    roles = list(job_roles[selected_category].keys())
    selected_role = st.selectbox("Select Specific Role:", roles, key="role_select")
    role_info = job_roles[selected_category][selected_role]
    with st.expander(f"ℹ️ {selected_role} - Required Skills & Info", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            st.info(role_info.get("description", "No description available"))
        with c2:
            st.success(f"**Required Skills:** {', '.join(role_info.get('required_skills', []))}")
else:
    selected_role = selected_category

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