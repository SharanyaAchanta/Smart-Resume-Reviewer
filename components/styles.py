import streamlit as st

def local_css():
    st.markdown("""
        <style>
        /* IMPORT FONTS */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

        /* RESET & VARS - PINK THEME */
        :root {
            /* PINK PALETTE */
            --primary-gradient: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
            --secondary-gradient: linear-gradient(135deg, #F472B6 0%, #EC4899 100%);
            --accent-gradient: linear-gradient(135deg, #F9A8D4 0%, #F472B6 100%);
            --bg-gradient: linear-gradient(180deg, #FDF2F8 0%, #FCE7F3 100%);
            
            /* GLASSMORPHISM */
            --glass-bg: rgba(255, 255, 255, 0.7);
            --glass-border: rgba(255, 255, 255, 0.5);
            --glass-shadow: 0 8px 32px 0 rgba(236, 72, 153, 0.1);
            
            /* TEXT COLORS */
            --text-primary: #1E293B;
            --text-secondary: #64748B;
        }

        /* GLOBAL STYLES */
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
            color: var(--text-primary);
            background: var(--bg-gradient);
            scroll-behavior: smooth;
        }

        /* HIDE DEFAULT STREAMLIT ELEMENTS */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;} 
        [data-testid="stSidebar"] {display: none;}

        /* REMOVE TOP SPACING - AGGRESSIVE */
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 5rem !important;
            max-width: 100%;
        }
        
        div[data-testid="stAppViewContainer"] > .main {
            padding-top: 0 !important;
        }

        header[data-testid="stHeader"] {
            display: none !important;
        }
        
        .stApp {
            margin-top: -60px !important;
        }

        /* UTILITIES */
        .gradient-text {
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }

        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid var(--glass-border);
            box-shadow: var(--glass-shadow);
            border-radius: 20px;
            padding: 30px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px 0 rgba(236, 72, 153, 0.15);
        }
        
        /* FILLED CARD VARIANT */
        .filled-card {
            background: white;
            border: 1px solid #FBCFE8;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        .filled-card:hover {
            border-color: #EC4899;
            transform: translateY(-3px);
            box-shadow: 0 10px 15px -3px rgba(236, 72, 153, 0.15);
        }

        /* CUSTOM BUTTONS - PINK */
        .stButton > button {
            background: var(--primary-gradient) !important;
            color: white !important;
            border: none !important;
            padding: 12px 30px !important;
            border-radius: 50px !important;
            font-weight: 600 !important;
            letter-spacing: 0.5px !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3) !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(236, 72, 153, 0.45) !important;
            filter: brightness(1.1) !important;
        }
        
        /* INPUT FIELDS - PINK FOCUS */
        .stTextInput > div > div > input, 
        .stTextArea > div > div > textarea, 
        .stSelectbox > div > div > div {
            background: white !important;
            border: 2px solid #FBCFE8 !important;
            border-radius: 12px !important;
            padding: 10px 15px !important;
            font-size: 15px !important;
            transition: all 0.2s !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: #EC4899 !important;
            box-shadow: 0 0 0 4px rgba(236, 72, 153, 0.1) !important;
        }

        /* FILE UPLOADER - PINK */
        [data-testid="stFileUploader"] {
            border: 2px dashed #F472B6 !important;
            background: rgba(244, 114, 182, 0.05) !important;
            border-radius: 20px !important;
            padding: 40px !important;
        }
        
        [data-testid="stFileUploader"]:hover {
            background: rgba(244, 114, 182, 0.1) !important;
            border-color: #EC4899 !important;
        }
        
        </style>
    """, unsafe_allow_html=True)
