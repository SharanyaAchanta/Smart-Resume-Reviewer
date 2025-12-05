import streamlit as st
from pathlib import Path
import base64

ASSETS_LOGO_PATH = Path("assets/logo_Pixel.png")
def _get_logo_base64(path: Path) -> str:
    try:
        return base64.b64encode(path.read_bytes()).decode()
    except:
        return ""

def show_navbar(active="Home"):
    logo_b64 = _get_logo_base64(ASSETS_LOGO_PATH)
    img_src = f"data:image/png;base64,{logo_b64}" if logo_b64 else ""

    navbar_html = f"""
    <style>
        .navbar {{
            position: fixed; top: 0; left: 0; width: 100%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            padding: 12px 18px; z-index: 9999;
            display: flex; justify-content: space-between; align-items: center;
            border-radius: 10px;
        }}
        .nav-links a {{
            color: white; text-decoration: none;
            padding: 8px 15px; margin-left: 10px;
            border-radius: 20px; font-weight: 600;
            background: transparent;
        }}
        .nav-links a.active {{
            background-color: rgba(255,255,255,0.18);
        }}
        .block-container {{ margin-top: 90px !important; }}
    </style>

    <div class="navbar">
      <div style="display:flex; align-items:center; gap:12px;">
        {f'<img src="{img_src}" width="36" style="border-radius:6px;">' if img_src else ''}
        <div style="color:white; font-weight:700;">Smart Resume Reviewer</div>
      </div>
      <div class="nav-links">
        <a href="/Home" class="{'active' if active=='Home' else ''}">🏠 Home</a>
        <a href="/Analyzer" class="{'active' if active=='Analyzer' else ''}">📤 Resume Analyzer</a>
        <a href="?page=contributors" class="{{'active' if active=='Contributors' else ''}}">👥 Contributors</a>
        <a href="?page=how_it_works" class="{{'active' if active=='How It Works' else ''}}">🛠️ How It Works</a>
        <a href="https://github.com/SharanyaAchanta/Smart-Resume-Reviewer" target="_blank">💻 GitHub</a>
      </div>
    </div>
    """
    st.markdown(navbar_html, unsafe_allow_html=True)
