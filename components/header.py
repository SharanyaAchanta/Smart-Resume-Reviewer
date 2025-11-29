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


def show_navbar():
  # try to get logo as base64; if not available, we will render text only
  logo_b64 = _get_logo_base64(ASSETS_LOGO_PATH)

  if logo_b64:
    img_src = f"data:image/png;base64,{logo_b64}"
  else:
    # empty src will simply not render an image
    img_src = ""


  navbar_html = f"""
  <style>
  .navbar {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 10000000;
    display: flex;
    justify-content:space-between;
    align-items:center;
    padding: 15px 20px;
    background: #0E1117;
    border: 0.5px solid gray;
    border-radius: 20px;
    box-sizing: border-box;
  }}

  /* push streamlit body down so it does not hide behind navbar */
  .block-container {{
    margin-top: 0 !important;
  }}

  .nav-links a {{
    margin-right:18px;
    color:white;
    text-decoration:none;
    font-size:15px;
    padding:8px 10px;
    border-radius:6px;
  }}
  .nav-links a:hover {{
    background: rgba(255,255,255,0.02);
    color: #00c9ff;
  }}

  @media (max-width:768px) {{
    .nav-links {{ display:none; }}
  }}


  /* keep navbar contents nicely aligned inside iframe */
  .navbar img {{
    display:inline-block;
    vertical-align:middle;
  }}

  .navbar h3 {{
    display:inline-block;
    vertical-align:middle;
    margin-left:6px;
  }}

  @keyframes fadeDown {{
    0% {{
      opacity: 0;
      transform: translateY(-20px);
    }}
    100% {{
      opacity: 1;
      transform: translateY(0);
    }}
  }}

  .fade-down {{
    opacity: 0;
    animation: fadeDown 0.7s ease-in-out forwards;
  }}
  </style>

  <div class="navbar fade-down">
    <div style="display:flex;align-items:center;gap:12px;">
      {f'<img src=\"{img_src}\" width=\"36\" style=\"border-radius:6px;\">' if img_src else ''}
      <h3 style="margin:0;color:white;">Smart Resume Analyzer</h3>
    </div>

    <div class="nav-links">
      <a href="#home">Home</a>
      <a href="#analyzer">Upload Resume</a>
      <a href="#features">Features</a>
      <a href="#hiw">How It Works</a>
      <a href="#about">About</a>
      <a href="https://github.com/SharanyaAchanta/Smart-Resume-Reviewer" target="_blank">Contribute</a>
    </div>
  </div>

  <script>
  document.addEventListener("click", function (e) {{
    const link = e.target.closest(".nav-links a");
    if (!link) return;

    const href = link.getAttribute("href");
    if (!href || !href.startsWith("#")) return;

    e.preventDefault();  // stop iframe scroll jump

    const id = href.substring(1);

    // Try to scroll on the parent (Streamlit main page)
    try {{
        const target = parent.document.getElementById(id);
        if (target) {{
            target.scrollIntoView({{ behavior: "smooth", block: "start" }});
            return;
        }}
    }} catch (_) {{ }}

    // fallback if parent fails
    const inside = document.getElementById(id);
    if (inside) {{
        inside.scrollIntoView({{ behavior: "smooth", block: "start" }});
    }}
  }});
  </script>
  """

  # Render the HTML using components.html (iframe). Because we embed the image as base64,
  # it will show correctly even when the HTML is rendered inside an iframe.
  components.html(navbar_html, height=100, scrolling=False)

def show_header():
  st.markdown("<h1 class='fade-down' style='text-align: center;'>Smart Resume Analyzer 🧠📄</h1>", unsafe_allow_html=True)
  st.markdown("<h5 class='fade-down' style='text-align: center; color: gray;'>Upload your resume (PDF) and get instant feedback!</h5>", unsafe_allow_html=True)