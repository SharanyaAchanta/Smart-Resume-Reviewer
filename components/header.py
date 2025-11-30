import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

ASSETS_LOGO_PATH = Path("assets/logo_Pixel.png")

def _get_logo_base64(path: Path) -> str:
    """Return base64 string for image. If file missing, return empty string."""
    try:
        data = path.read_bytes()
        return base64.b64encode(data).decode()
    except Exception as e:
        # Could not read file
        return ""

def show_navbar(active_page="Home"):
    """Multipage navbar - pass current page name"""
    logo_b64 = _get_logo_base64(ASSETS_LOGO_PATH)
    img_src = f"data:image/png;base64,{logo_b64}" if logo_b64 else ""
    
    navbar_html = f"""
    <style>
    .navbar {{
        position: fixed; top: 0; left: 0; width: 100%; z-index: 10000000;
        display: flex; justify-content: space-between; align-items: center;
        padding: 15px 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none; border-radius: 0; box-shadow: 0 4px 20px rgba(102,126,234,0.3);
        box-sizing: border-box;
    }}
    .block-container {{ margin-top: 90px !important; }}
    .nav-links {{ display: flex; gap: 1rem; align-items: center; }}
    .nav-links a {{
        color: white; text-decoration: none; font-size: 15px; font-weight: 600;
        padding: 10px 16px; border-radius: 25px; transition: all 0.3s;
    }}
    .nav-links a:hover {{ background: rgba(255,255,255,0.2); transform: translateY(-2px); }}
    .nav-links .active {{ background: rgba(255,255,255,0.3) !important; }}
    @media (max-width:768px) {{ 
        .nav-links {{ gap: 0.5rem; }} 
        .nav-links a {{ padding: 8px 12px; font-size: 14px; }} 
    }}
    .navbar img {{ display: inline-block; vertical-align: middle; }}
    .navbar h3 {{ 
        display: inline-block; vertical-align: middle; margin-left: 6px; 
        margin: 0; color: white; 
    }}
    @keyframes fadeDown {{
        0% {{ opacity: 0; transform: translateY(-20px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
    }}
    .fade-down {{ animation: fadeDown 0.7s ease-in-out forwards; }}
    </style>
    
    <div class="navbar fade-down">
        <div style="display: flex; align-items: center; gap: 12px;">
            {f'<img src="{img_src}" width="36" style="border-radius: 6px;">' if img_src else ''}
            <h3>Smart Resume Reviewer</h3>
        </div>
        <div class="nav-links">
            <a href="/Home" class="{'active' if active_page=='Home' else ''}">🏠 Home</a>
            <a href="/Home" class="{'active' if active_page=='Analyzer' else ''}">📤 Resume Analyzer</a>
            <a href="/Contributors" class="{'active' if active_page=='Contributors' else ''}">👥 Contributors</a>
            <a href="https://github.com/SharanyaAchanta/Smart-Resume-Reviewer" target="_blank" style="padding: 10px 16px;">
                <i class="fab fa-github" style="font-size: 18px;"></i>
            </a>
        </div>
    </div>
    """
    components.html(navbar_html, height=100, scrolling=False)

def show_header():
    st.markdown("<h1 class='fade-down' style='text-align: center;'>Smart Resume Analyzer 🧠📄</h1>", unsafe_allow_html=True)
    st.markdown("<h5 class='fade-down' style='text-align: center; color: gray;'>Upload your resume (PDF) and get instant feedback!</h5>", unsafe_allow_html=True)
