# pages/how_it_works.py
import streamlit as st

def render():

    # --- CUSTOM CSS ---
    st.markdown("""
    <style>

    /* Center the whole content area */
    .how-it-works-container {
        max-width: 900px;
        margin: auto;
        padding: 20px 40px;
        text-align: center;
        animation: fadeIn 0.6s ease-in-out;
    }

    /* Fade animation */
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(10px);}
        to {opacity: 1; transform: translateY(0);}
    }

    /* Section card styling */
    .how-card {
        background: #ffffff10;
        padding: 22px 28px;
        margin-top: 20px;
        border-radius: 14px;
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 0 25px rgba(0,0,0,0.12);
        transition: 0.2s ease;
    }
    .how-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 30px rgba(0,0,0,0.22);
    }

    h1, h2, h3, p {
        text-align: center !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # --- CONTENT WRAPPER ---
    st.markdown("<div class='how-it-works-container'>", unsafe_allow_html=True)

    st.markdown("<h1>📘 How It Works</h1>", unsafe_allow_html=True)
    st.markdown("Welcome to the <b>Smart Resume Reviewer</b>!<br>Here’s how your resume is analyzed step by step 🔍", unsafe_allow_html=True)

    # --- SECTION 1 ---
    st.markdown("""
    <div class='how-card'>
        <h2>🔄 1. Upload Resume</h2>
        <p>You upload a resume in <b>PDF</b> or <b>image (JPG/PNG)</b> format.  
        Our system reads and prepares it for extraction.</p>
    </div>
    """, unsafe_allow_html=True)

    # --- SECTION 2 ---
    st.markdown("""
    <div class='how-card'>
        <h2>🔍 2. Extract Information</h2>
        <p>The parser extracts key resume sections:</p>
        <p>🎓 Education • 💼 Experience • 🛠 Skills • 📁 Projects • 🏅 Certifications</p>
    </div>
    """, unsafe_allow_html=True)

    # --- SECTION 3 ---
    st.markdown("""
    <div class='how-card'>
        <h2>🧠 3. Analyze Content</h2>
        <p>We analyze your content for missing sections, weak areas, keywords,  
        formatting quality, and industry best practices.</p>
    </div>
    """, unsafe_allow_html=True)

    # --- SECTION 4 ---
    st.markdown("""
    <div class='how-card'>
        <h2>💡 4. Get Suggestions</h2>
        <p>You get actionable feedback, improvements, formatting tips,  
        keyword suggestions, and ATS-friendly recommendations.</p>
    </div>
    """, unsafe_allow_html=True)

    # --- ENDING ---
    st.markdown("""
    <div class='how-card'>
        <h3>🚀 That's it!</h3>
        <p>You now understand exactly how your resume is reviewed — fast, accurate, and effective.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    #button to go main page
    st.markdown(
        """
        <div style='text-align:center; margin-bottom: 20px;'>
          <a href="/?page=home">
            <button style="
              background-color:#4CAF50;
              color:white;
              padding:10px 18px;
              border:none;
              border-radius:8px;
              cursor:pointer;
              font-size:16px;">
              ⬅ Go to Main Page
            </button>
          </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Main container (Streamlit)
    st.markdown(
        "<div style='margin-top: 1rem;'></div>",
        unsafe_allow_html=True,
    )
