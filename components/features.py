import streamlit as st
from streamlit_lottie import st_lottie
import json
import os

from components.header import show_navbar, show_header 

show_navbar(active_page="Features")
show_header()

def load_lottie(path: str):
    """Load a Lottie animation from a local JSON file."""
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return None

def show_features_page():
    st.markdown("""
        <style>
            .feature-card, .additional-card {
                max-width: 700px;
                margin: 20px auto;  /* centers horizontally */
                background: linear-gradient(135deg, #f5f7fa, #e0eafc);
                padding: 25px;
                border-radius: 20px;
                box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                border-left: 6px solid #4a90e2;
            }
            .feature-card:hover, .additional-card:hover {
                transform: translateY(-5px);
                box-shadow: 0px 12px 35px rgba(0,0,0,0.2);
            }
            .feature-title, .additional-title {
                font-size: 22px;
                font-weight: 700;
                color: #1b1b1b;
                margin-bottom: 10px;
                text-align: center;
            }
            .feature-desc, .additional-desc {
                font-size: 16px;
                color: #333;
                text-align: center;
            }
            .section-divider {
                height: 4px;
                width: 100px;
                background: linear-gradient(90deg, #667eea, #764ba2);
                margin: 30px auto;
                border-radius: 4px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("🚀 Project Features")
    st.subheader("Explore the smart capabilities of the Smart Resume Reviewer")
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    assets_path = "assets"
    animations = {
        "ai_review": load_lottie(os.path.join(assets_path, "ai.json")),
        "analysis": load_lottie(os.path.join(assets_path, "analysis.json")),
        "security": load_lottie(os.path.join(assets_path, "security.json")),
    }

    # --- Feature Cards (stacked and center-aligned) ---
    features = [
        {
            "title": "🤖 AI-Powered Resume Review",
            "desc": "Automatically analyzes your resume for grammar issues, formatting mistakes, clarity improvements, and identifies missing important sections using AI.",
            "anim": animations["ai_review"]
        },
        {
            "title": "📊 Keyword & ATS Score Checking",
            "desc": "Detects relevant industry keywords, measures ATS friendliness, and highlights mismatches between job descriptions and resume content.",
            "anim": animations["analysis"]
        },
        {
            "title": "🔒 Secure File Handling",
            "desc": "Your uploaded resume is processed securely and never stored permanently. Temporary caching ensures safety and compliance.",
            "anim": animations["security"]
        }
    ]

    for f in features:
        # Full-width column
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-title">{f['title']}</div>
                    <div class="feature-desc">{f['desc']}</div>
                </div>
            """, unsafe_allow_html=True)
            if f['anim']:
                st_lottie(f['anim'], height=200)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # --- Additional Features in Centered Card ---
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("""
            <div class="additional-card">
                <div class="additional-title">✨ Additional Features</div>
                <div class="additional-desc">
                    - 📝 <b>PDF, DOCX Resume Support</b><br>
                    - 🎯 <b>Role-based Resume Optimization</b><br>
                    - 🧠 <b>Smart Suggestions for Skills, Projects & Achievements</b><br>
                    - 🌐 <b>Multi-page Resume Support</b><br>
                    - 🧩 <b>Ease of use with clean UI</b><br>
                    - ⚡ <b>Fast review engine</b>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.success("💡 Tip: Keep updating this page as new features are added to the project!")
