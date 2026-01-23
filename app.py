import streamlit as st
import json
import time
import fitz
import hashlib
import pandas as pd


# Helper function to generate unique file ID
def _file_id(uploaded_file):
    """Generate a unique ID for an uploaded file based on name and size."""
    if uploaded_file is None:
        return None
    file_name = uploaded_file.name
    file_size = uploaded_file.size
    file_id_str = f"{file_name}_{file_size}"
    return hashlib.md5(file_id_str.encode()).hexdigest()


# Theme from session (controlled by custom sidebar in header.py)
if "theme" not in st.session_state:
    st.session_state.theme = "Light"
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
    st.markdown("""
    <style>
    .loading-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: #ffffff;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 99999;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    .loading-spinner {
        width: 60px;
        height: 60px;
        border: 4px solid rgba(0,0,0,0.05);
        border-top: 4px solid #3b82f6;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin-bottom: 24px;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .loading-title {
        font-size: 24px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 8px;
    }
    .loading-subtitle {
        font-size: 15px;
        color: #6b7280;
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
    
    time.sleep(2.5)
    st.session_state.page_loaded = True
    st.rerun()
    st.stop()

# --- HIDE STREAMLIT DEFAULT LOADING ---
st.markdown("""
<style>
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
from utils.resume_history import save_review, show_history_ui
from utils.resume_parser import parse_resume
from utils.analyze_resume import get_resume_feedback
from components.header import show_header, show_sidebar_navbar
from components.suggestions import show_suggestions, get_grammar_suggestions
from components.contributors import show_contributors_page
from components.features import show_features_page
from components import resume_tips
from components.login import show_login

# ✅ CRITICAL: Initialize ALL session state FIRST
if "theme" not in st.session_state:
    st.session_state.theme = "Light"
if "show_contributors" not in st.session_state:
    st.session_state.show_contributors = False
if "show_features" not in st.session_state:
    st.session_state.show_features = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "Landing"
if "last_file_id" not in st.session_state:
    st.session_state.last_file_id = None
if "consent" not in st.session_state:
    st.session_state.consent = None
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_login_modal" not in st.session_state:
    st.session_state.show_login_modal = False
if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = False
if "job_description" not in st.session_state:
    st.session_state.job_description = ""
if "experience_level" not in st.session_state:
    st.session_state.experience_level = "Mid Level"

# Footer import with fallback
try:
    from components.footer import render_footer as show_footer
except Exception:
    try:
        from components.footer import show_footer
    except Exception:
        def show_footer():
            return None

from components.login import show_login_page  # use your new full-page function
from components.landing import show_landing_page

# Static Pages
try:
    from components.static_pages import (
        show_service_page, show_blogs_page, show_about_page, 
        show_pricing_page, show_faq_page
    )
except ImportError:
    # Fallback to avoid crashes if file missing during dev
    def show_service_page(): st.info("Service Page")
    def show_blogs_page(): st.info("Blogs Page")
    def show_about_page(): st.info("About Page")
    def show_pricing_page(): st.info("Pricing Page")
    def show_faq_page(): st.info("FAQ Page")

# If we are in auth mode and not logged in, only show login/signup page
if st.session_state.get("auth_mode", False) and not st.session_state.get("logged_in", False):
    show_login_page()
    st.stop()

# -----------------------------
# MAIN APP LOGIC
# -----------------------------

# Note: Routing will be handled after consent check and global styling
from components.resume_builder import show_resume_builder

st.markdown("""
<style>

header nav {
    display: flex !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    justify-content: space-between !important;
}

header nav * {
    white-space: nowrap !important;
}

header nav ul {
    display: flex !important;
    gap: 18px !important;
}

/* Fix text breaking like Hom
e / Servi
ces */
header nav li, header nav a, header nav span {
    white-space: nowrap !important;
}

</style>
""", unsafe_allow_html=True)

# Apply CSS overrides based on theme
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
            fill: #EC4899 !important;
            width: 36px !important;
            height: 36px !important;
        }
        [data-testid="stFileUploader"]:hover {
            border-color: #EC4899 !important;
            box-shadow: 0px 0px 18px rgba(236, 72, 153, 0.25);
            transform: translateY(-2px);
        }
        [data-testid="stFileUploader"].drag-over {
            border-color: #F472B6 !important;
            box-shadow: 0px 0px 25px rgba(244, 114, 182, 0.35);
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
            border: 2px dashed #e5e7eb !important;
            background: #ffffff !important;
            padding: 40px !important;
            border-radius: 12px !important;
            transition: all 0.2s ease-in-out !important;
            cursor: pointer !important;
            margin: auto;
            box-shadow: none !important;
        }
        [data-testid="stFileUploader"] * {
            color: #4b5563 !important;
            font-family: 'Inter', sans-serif !important;
        }
        [data-testid="stFileUploader"] svg {
            fill: #EC4899 !important;
            width: 48px !important;
            height: 48px !important;
            margin-bottom: 10px !important;
        }
        [data-testid="stFileUploader"]:hover {
            border-color: #EC4899 !important;
            background: #FDF2F8 !important;
        }
        [data-testid="stFileUploader"].drag-over {
            border-color: #EC4899 !important;
            background: #FDF2F8 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

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
    background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
    color: white;
    text-align: center;
    font-size: 14px;
    padding: 8px 0;
    z-index: 9999;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.main .block-container {
    padding-top: 0 !important;
}
</style>
<div class="privacy-banner">
    🔒 Privacy Notice: This tool processes your resume <strong>locally in memory</strong>. No files or personal information are stored.
</div>
""",
    unsafe_allow_html=True,
)


# Upload card check
try:
    from components.upload_card import upload_card
    _HAS_UPLOAD_CARD = True
except Exception:
    _HAS_UPLOAD_CARD = False

# -----------------------------
# UPDATED COOKIE BANNER
# -----------------------------
# This allows the landing page to be visible behind the cookie banner
# ✅ CONSENT CHECK
if st.session_state.consent is None:
    with st.container():
        st.markdown("""
        <div style="
            background: #1F2937; 
            padding: 20px; 
            border-radius: 12px; 
            margin-bottom: 20px; 
            border: 1px solid #374151;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        ">
            <div style="font-size: 1.2rem; font-weight: bold; color: white; margin-bottom: 10px;">🍪 We use cookies</div>
            <div style="color: #D1D5DB; margin-bottom: 20px;">
                This website uses essential cookies to ensure you get the best experience on our website.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Action Buttons in standard columns (High Visibility)
        cb1, cb2 = st.columns([1, 5])
        with cb1:
            if st.button("Accept", key="cookie_accept_top", type="primary", width="stretch"):
                st.session_state.consent = "all"
                st.rerun()
        with cb2:
            if st.button("Later", key="cookie_later_top", width="content"):
                st.session_state.consent = "later"
                st.rerun()
                
# ✅ LANDING PAGE - Handle early and stop
if st.session_state.current_page == "Landing":
    show_landing_page()
    if callable(show_footer):
        show_footer()
    st.stop()

# ✅ GLOBAL STYLING (applies to all non-landing pages)
# Professional styles are loaded via components.styles.local_css() above

# --- SIDEBAR NAVBAR & HEADER ---
show_sidebar_navbar(active_page=st.session_state.current_page)
show_header()

# LOGIN MODAL TRIGGER (single source of truth)
if st.session_state.get("show_login_modal", False):
    show_login()
    st.markdown("")  # small spacer

st.markdown("<br>", unsafe_allow_html=True)

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

# ✅ ROUTING FOR OTHER PAGES
if st.session_state.current_page == "Services":
    show_service_page()
    if callable(show_footer):
        show_footer()
    st.stop()
elif st.session_state.current_page == "Blogs":
    show_blogs_page()
    if callable(show_footer):
        show_footer()
    st.stop()
elif st.session_state.current_page == "About":
    show_about_page()
    if callable(show_footer):
        show_footer()
    st.stop()
elif st.session_state.current_page == "Pricing":
    show_pricing_page()
    if callable(show_footer):
        show_footer()
    st.stop()
elif st.session_state.current_page == "FAQ":
    show_faq_page()
    if callable(show_footer):
        show_footer()
    st.stop()
elif st.session_state.current_page == "Resume Tips":
    resume_tips.main()
    if callable(show_footer):
        show_footer()
    st.stop()
elif st.session_state.current_page == "Resume Builder":
    show_resume_builder()
    if callable(show_footer):
        show_footer()
    st.stop()

# ✅ ANALYZER PAGE - Continue to show analysis UI
if st.session_state.current_page != "Analyzer":
    # If we reach here and it's not Analyzer, something went wrong
    st.warning("Page not found. Redirecting to Landing page...")
    st.session_state.current_page = "Landing"
    st.rerun()

# --- ANALYZER PAGE CONTENT ---
# Show Resume History in Sidebar
show_history_ui()

st.markdown("<h1 style='background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800; margin-bottom: 20px;'>📊 Resume Analyzer</h1>", unsafe_allow_html=True)

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
    with st.expander(f"📌 {selected_role} - Required Skills & Info", expanded=True):
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

# --- HANDLE FILE FROM LANDING PAGE ---
if "uploaded_file_temp" in st.session_state and st.session_state.uploaded_file_temp:
    uploaded_file = st.session_state.uploaded_file_temp
    # Keep it persistent? Or clear it?
    # For now, let's just use it.
else:
    # Fallback uploader on Analyzer page with validation
    from components.upload_card import validate_uploaded_file, ALLOWED_FILE_TYPES, MAX_FILE_SIZE_MB

    uploaded_file_temp = st.file_uploader(
        "Upload Resume (PDF, DOCX, TXT)",
        type=ALLOWED_FILE_TYPES,
        help=f"Upload a resume file (max {MAX_FILE_SIZE_MB} MB) to analyze"
    )

    # Validate the uploaded file
    if uploaded_file_temp:
        is_valid, error_message = validate_uploaded_file(uploaded_file_temp)
        if not is_valid:
            st.error(error_message)
            uploaded_file = None
        else:
            uploaded_file = uploaded_file_temp
    else:
        uploaded_file = None

# --- ANALYSIS DASHBOARD ---
if uploaded_file:
    current_file_id = _file_id(uploaded_file)
    if st.session_state.last_file_id != current_file_id:
        st.session_state.last_file_id = current_file_id
        
        with st.spinner("⏳ Analysis in progress..."):
            time.sleep(1) # Simulated delay for effect

        # PARSE
        parsed = parse_resume(uploaded_file)
        plain_text = parsed.get("plain_text", "")
        
        # Get job description and experience level from session state
        job_description = st.session_state.get("job_description", "")
        experience_level = st.session_state.get("experience_level", "Mid Level")
        
        # ANALYZE
        suggestions, resume_score, keyword_match, predicted_role = get_resume_feedback(
            plain_text, 
            selected_role, 
            job_description=job_description, 
            experience_level=experience_level
        )
        
        # Save results to session state to prevent re-running on interaction
        st.session_state.analysis_results = {
            "plain_text": plain_text,
            "suggestions": suggestions,
            "score": resume_score,
            "keyword_match": keyword_match,
            "predicted_role": predicted_role
        }

# --- DASHBOARD UI ---
results = st.session_state.get("analysis_results", None)

# Ensure history session exists
if "review_history" not in st.session_state:
    st.session_state.review_history = []

# =====================================================
#                IF RESULTS EXIST
# =====================================================
if results:

    plain_text = results["plain_text"]
    resume_score = results["score"]
    suggestions = results["suggestions"]
    keyword_match = results["keyword_match"]
    predicted_role = results.get("predicted_role", "Unknown")

    # --- SAVE HISTORY ---
    try:
        save_review(
            role=selected_role,
            score=int(resume_score),
            predicted_role=predicted_role,
            suggestions=suggestions
        )
    except Exception as e:
        print("History Save Failed:", e)

    # ---------------- 📊 COMPARISON SECTION ----------------
    st.markdown("### 📊 Resume Version Comparison")

    if len(st.session_state.review_history) >= 2:
        reviews = st.session_state.review_history

        r1 = st.selectbox(
            "Select Resume 1",
            reviews,
            format_func=lambda x: x["time"],
            key="cmp1"
        )

        r2 = st.selectbox(
            "Select Resume 2",
            reviews,
            format_func=lambda x: x["time"],
            key="cmp2"
        )

        c1, c2 = st.columns(2)
        c1.metric("Resume 1 Score", r1["score"])
        c2.metric("Resume 2 Score", r2["score"])

        st.info("Comparison completed — Score difference shown above.")

    else:
        st.warning("Upload at least 2 resumes to compare.")


    # ========= 📈 VISUAL ANALYTICS =========
    import pandas as pd
    st.markdown("## 📈 Resume Progress Insights")

    if len(st.session_state.review_history) >= 1:
        df = pd.DataFrame(st.session_state.review_history)
        df["index"] = range(1, len(df) + 1)

        st.markdown("### 📉 Resume Score Trend")
        st.line_chart(df.set_index("index")["score"])

        st.markdown("### 📊 Score Comparison Bar Chart")
        st.bar_chart(df.set_index("index")["score"])

        st.markdown("### 🧠 Insights Summary")
        c1, c2, c3 = st.columns(3)
        c1.metric("Highest Score", max(df["score"]))
        c2.metric("Lowest Score", min(df["score"]))
        c3.metric("Total Uploads", len(df))

        if len(df) >= 2:
            growth = df["score"].iloc[-1] - df["score"].iloc[0]
            if growth > 0:
                st.success(f"🚀 Your resume improved by +{growth} points!")
            elif growth < 0:
                st.warning(f"⚠️ Your score dropped {growth} points.")
            else:
                st.info("ℹ️ No change since first submission.")
    else:
        st.info("📄 Upload at least one resume to see analytics.")

    # ========= MAIN 2 COLUMN UI =========
    d_col1, d_col2 = st.columns([1, 1.2])

    # ================= LEFT PANEL =================
    with d_col1:
        with st.expander("⚙️ Tailor Your Analysis", expanded=False):
            job_description = st.text_area(
                "Paste Job Description:",
                height=100,
                value=st.session_state.get("job_description", ""),
                key="job_desc_input"
            )

            exp_levels = ["Entry Level", "Mid Level", "Senior", "Executive"]
            current_exp = st.session_state.get("experience_level", "Mid Level")
            default_index = exp_levels.index(current_exp) if current_exp in exp_levels else 1

            experience_level = st.selectbox(
                "Experience Level:",
                exp_levels,
                index=default_index,
                key="exp_level_input"
            )

            if st.button("Re-Analyze"):
                st.session_state.job_description = job_description
                st.session_state.experience_level = experience_level
                if "analysis_results" in st.session_state:
                    del st.session_state.analysis_results
                st.rerun()

        # Resume Preview
        st.markdown(f"""
        <div style="
            background:white;
            padding:30px;
            border-radius:12px;
            height:800px;
            overflow-y:auto;
            border:1px solid #E5E7EB;
        ">
            <h3>{st.session_state.get("user", {}).get("name", "Candidate Name")}</h3>
            <p><strong>Target Role:</strong> {selected_role}</p>
            <p><strong>AI Predicted Role:</strong> {predicted_role}</p>
            <hr>
            <div style="white-space: pre-wrap;">{plain_text[:3000]}...</div>
        </div>
        """, unsafe_allow_html=True)


    # ================= RIGHT PANEL =================
    with d_col2:
        st.subheader("Resume Review")

        # SCORE BADGE
        st.metric("Resume Score", f"{int(resume_score)}/100")

        # PROGRESS BARS
        def progress_bar(label, value):
            st.markdown(f"""
            <div style="margin-bottom:10px;">
                <b>{label}:</b> {value}/100
                <div style="height:8px;background:#eee;border-radius:4px;">
                    <div style="width:{value}%;height:8px;background:#EC4899;border-radius:4px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        progress_bar("Content Quality", int(resume_score))
        progress_bar("Skills Match", int(keyword_match))

        # SUGGESTIONS
        with st.expander("Resume Improvement Checklist", expanded=True):
            if suggestions:
                for s in suggestions[:5]:
                    st.warning(s)
            else:
                st.success("Great! No major issues found 👍")
        
        # detailed description for improvement skills (LLM-powered)
        with st.expander("Why these improvements matter", expanded=False):
            import os
            from langchain_google_genai import ChatGoogleGenerativeAI
            from langchain_core.prompts import ChatPromptTemplate
            os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY" # add your api key here
            if "improvement_explanations" not in st.session_state:
                st.session_state.improvement_explanations = None

            model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite", temperature = 0)

            prompt_template = ChatPromptTemplate.from_messages([
                ("system", "you are a helpful assistant that explains resume improvement suggestions clearly and like a teacher to a student , explain every suggestion seperately") ,
                ("human" , "{suggestions}")
            ])
            generate = st.button("Generate Explanation")

            if generate and st.session_state.improvement_explanations is None:
                with st.spinner("🔄 Generating detailed explanations..."):

                    # small delay to avoid rate-limit spikes
                    time.sleep(2)

                    joined = "\n".join(f"- {s}" for s in suggestions)
                    prompt = prompt_template.invoke({"suggestions": joined})

                    response = model.invoke(prompt)
                    st.session_state.improvement_explanations = response.content

            explanation_text = st.session_state.improvement_explanations

            if explanation_text:
                st.markdown("""
                <style>
                .explanation-container {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 12px;
                    padding: 20px;
                    margin: 15px 0;
                    color: white;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                .explanation-content {
                    background: rgba(255, 255, 255, 0.1);
                    border-left: 4px solid #ffd700;
                    padding: 15px;
                    border-radius: 8px;
                    line-height: 1.6;
                    font-size: 14px;
                }
                </style>
                """, unsafe_allow_html=True)

                # Header
                col1, col2 = st.columns([0.1, 0.9])
                with col1:
                    st.markdown("💡")
                with col2:
                    st.markdown("### Why These Improvements Matter")

                # Content
                st.markdown("""
                <div class="explanation-container">
                    <div class="explanation-content">
                """, unsafe_allow_html=True)

                st.markdown(explanation_text)

                st.markdown("""
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Footer
                st.markdown("""
                <div style="margin-top: 15px; padding: 10px; background-color: #f0f2f6;
                border-radius: 8px; text-align: center; font-size: 12px; color: #666;">
                💬 <b>Pro Tip:</b> Implementing these improvements will significantly
                enhance your resume's effectiveness and increase your chances of landing interviews.
                </div>
                """, unsafe_allow_html=True)

            else:
                st.info("Click **Generate Explanation** to get detailed insights.")
            
# =====================================================
#                IF NO RESULTS
# =====================================================
else:
    st.info("📄 Please upload a PDF resume to see the analysis.")
