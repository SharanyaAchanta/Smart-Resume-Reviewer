import streamlit as st
from pathlib import Path
import base64

ASSETS_LOGO_PATH = Path("assets/logo_Pixel.png")

def _get_logo_base64(path: Path) -> str:
    try:
        return base64.b64encode(path.read_bytes()).decode()
    except Exception:
        return ""

def show_sidebar_navbar(active_page="Analyzer"):
    logo_b64 = _get_logo_base64(ASSETS_LOGO_PATH)
    img_tag = f'<img src="data:image/png;base64,{logo_b64}" width="40" style="border-radius:8px; vertical-align:middle;" />' if logo_b64 else ''
    
    current_theme = st.session_state.get('theme', 'Dark')
    
with st.sidebar:
        # === LOGIN SECTION (TOP) ===
    if "auth_mode" not in st.session_state:
        st.session_state.auth_mode = False
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        if st.button("🔐 Login", key="sidebar_login", use_container_width=True):
            st.session_state.auth_mode = True      # <— turn on full-page auth
            st.experimental_rerun()

        st.markdown("---")
    else:
        st.success("✅ Logged In")
        if st.button("🚪 Logout", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.experimental_rerun()
        st.markdown("---")
                else:
        st.success("✅ Logged In")
        if st.button("🚪 Logout", use_container_width=True):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
            st.markdown("---")
        
        # === LOGO & BRAND ===
        st.markdown(f"""
        <style>
        .sidebar-header {{
            padding: 1.5rem 1rem 1rem !important;
            background: linear-gradient(135deg, rgba(14,17,23,0.95) 0%, rgba(27,31,36,0.95) 100%) !important;
            border-radius: 16px !important;
            margin-bottom: 1.5rem !important;
            text-align: center !important;
            backdrop-filter: blur(20px) !important;
        }}
        .sidebar-title {{
            font-size: 24px !important;
            font-weight: 900 !important;
            background: linear-gradient(135deg, #00d4aa, #00b140) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            margin: 0 0 0.5rem 0 !important;
        }}
        .sidebar-subtitle {{
            color: rgba(255,255,255,0.8) !important;
            font-size: 14px !important;
            margin: 0 !important;
            line-height: 1.4 !important;
        }}
        </style>
        <div class="sidebar-header">
            {img_tag}
            <h1 class="sidebar-title">Smart Resume Analyzer</h1>
            <p class="sidebar-subtitle">Upload your resume (PDF) and get instant feedback!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # === NAVIGATION LINKS ===
        if st.button("🏠 Home", key="nav_home", use_container_width=True):
            st.session_state.current_page = "Analyzer"
            st.session_state.show_contributors = False
            st.session_state.show_features = False
            st.rerun()
            
        if st.button("📄 Analyzer", key="nav_analyzer", use_container_width=True):
            st.session_state.current_page = "Analyzer"
            st.session_state.show_contributors = False
            st.session_state.show_features = False
            st.rerun()
            
        if st.button("✨ Features", key="nav_features", use_container_width=True):
            st.session_state.show_features = True
            st.session_state.show_contributors = False
            st.session_state.current_page = "Features"
            st.rerun()
            
        if st.button("📝 Tips", key="nav_tips", use_container_width=True):
            st.session_state.current_page = "Resume Tips"
            st.session_state.show_features = False
            st.session_state.show_contributors = False
            st.rerun()
            
        if st.button("👥 Contributors", key="nav_contributors", use_container_width=True):
            st.session_state.show_contributors = True
            st.session_state.show_features = False
            st.session_state.current_page = "Contributors"
            st.rerun()
            
        # === THEME TOGGLE ===
        st.markdown("---")
        if st.button(f"{'☀️ Light' if current_theme == 'Dark' else '🌙 Dark'} Mode", 
                    key="theme_toggle_main", use_container_width=True):
            st.session_state.theme = "Light" if st.session_state.theme == "Dark" else "Dark"
            st.rerun()

def show_header():
    """SIMPLE TITLE ONLY in main content area"""
    st.markdown("""
    <style>
    .simple-title {
        font-size: clamp(2.5rem, 6vw, 4rem) !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #00d4aa 0%, #00b140 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        text-align: center !important;
        margin: 2rem 0 1rem 0 !important;
        padding: 1rem !important;
    }
    </style>
    <h1 class="simple-title">Smart Resume Analyzer 🧠📄</h1>
    """, unsafe_allow_html=True)
   