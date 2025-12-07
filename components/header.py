import streamlit as st
from pathlib import Path
import base64

ASSETS_LOGO_PATH = Path("assets/logo_Pixel.png")

def _get_logo_base64(path: Path) -> str:
    try:
        return base64.b64encode(path.read_bytes()).decode()
    except Exception:
        return ""

def show_navbar(active_page="Home"):
    logo_b64 = _get_logo_base64(ASSETS_LOGO_PATH)
    img_tag = f'<img src="data:image/png;base64,{logo_b64}" width="36" style="border-radius:6px; vertical-align:middle;" />' if logo_b64 else ''

    nav_html = f"""
    <style>
    /* hide Streamlit's default header safely */
    header[role="banner"], [data-testid="stHeader"], [data-testid="stToolbar"] {{
        display: none !important;
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        visibility: hidden !important;
    }}

    /* fixed full-bleed navbar in the main document (not iframe) */
    .navbar {{
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        width: 100vw !important;
        z-index: 999999 !important;
        background: linear-gradient(135deg,#667eea 0%,#764ba2 100%) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.35) !important;
    }}
    .navbar .nav-inner {{
        max-width: 1200px;
        margin: 0 auto;
        display:flex;
        align-items:center;
        justify-content:space-between;
        padding: 12px 20px;
        box-sizing: border-box;
    }}
    .nav-links a {{ color:#fff; text-decoration:none; padding:8px 12px; border-radius:14px; }}
    .nav-links a.active {{ background: rgba(255,255,255,0.12); }}
    /* push app content below fixed navbar */
    .block-container {{ padding-top: 72px !important; }}
    @media (max-width:768px) {{
      .block-container {{ padding-top: 110px !important; }}
    }}
    </style>

    <div class="navbar" role="navigation" aria-label="Main navigation">
      <div class="nav-inner">
        <div style="display:flex; align-items:center; gap:12px;">
          {img_tag}
          <div style="color:#fff; font-weight:700; font-size:18px;">Smart Resume Reviewer</div>
        </div>
        <div class="nav-links" role="menu" aria-label="Primary">
          <a href="/Home" class="{'active' if active_page=='Home' else ''}">🏠 Home</a>
          <a href="/Home" class="{'active' if active_page=='Analyzer' else ''}">📤 Resume Analyzer</a>
          <a href="/Contributors" class="{'active' if active_page=='Contributors' else ''}">👥 Contributors</a>
          <a href="/Login" class="{'active' if active_page=='Login' else ''}">🔐 Login</a>
        </div>
      </div>
    </div>
    """

    # render to main document (not iframe)
    st.markdown(nav_html, unsafe_allow_html=True)


def show_header():
    st.markdown("<h1 class='fade-down' style='text-align: center;'>Smart Resume Analyzer 🧠📄</h1>", unsafe_allow_html=True)
    st.markdown("<h5 class='fade-down' style='text-align: center; color: gray;'>Upload your resume (PDF) and get instant feedback!</h5>", unsafe_allow_html=True)
