import streamlit as st
import base64

def show_header():
    """Professional header/navbar with modern design."""
    current = st.session_state.get("current_page", "Landing")
    is_logged_in = st.session_state.get("logged_in", False)
    user_name = st.session_state.get("user", {}).get("name", "") if is_logged_in else ""
    
    # Professional header CSS with Outfit font
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
        
        .header-container {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border-bottom: 1px solid rgba(226, 232, 240, 0.8);
            padding: 18px 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            transition: all 0.3s ease;
        }
        
        .header-container:hover {
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        
        /* Navigation Links Styling */
        .stButton > button {
            white-space: nowrap !important;
            background: transparent !important;
            border: none !important;
            color: #64748B !important;
            font-weight: 500 !important;
            font-size: 15px !important;
            font-family: 'Outfit', sans-serif !important;
            padding: 10px 18px !important;
            border-radius: 10px !important;
            cursor: pointer !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: none !important;
        }
        
        .stButton > button:hover {
            background: rgba(236, 72, 153, 0.08) !important;
            color: #EC4899 !important;
            transform: translateY(-1px);
        }
        
        /* Hide hidden logo button */
        button[key="logo_btn_hidden"] {
            display: none !important;
        }
        
        /* Auth Buttons - PINK */
        .stButton > button[type="primary"] {
            background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 10px 22px !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            font-family: 'Outfit', sans-serif !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 4px 12px rgba(236, 72, 153, 0.3) !important;
        }
        
        .stButton > button[type="primary"]:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(236, 72, 153, 0.4) !important;
            filter: brightness(1.05);
        }
        
        .stButton > button[type="secondary"] {
            background: white !important;
            color: #EC4899 !important;
            border: 2px solid #EC4899 !important;
            border-radius: 12px !important;
            padding: 8px 20px !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            font-family: 'Outfit', sans-serif !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button[type="secondary"]:hover {
            background: rgba(236, 72, 153, 0.05) !important;
            transform: translateY(-1px);
        }
        
        /* User Greeting - PINK */
        .user-greeting {
            color: #1E293B;
            font-size: 15px;
            font-weight: 600;
            font-family: 'Outfit', sans-serif;
            padding: 8px 16px;
            background: rgba(236, 72, 153, 0.05);
            border-radius: 10px;
            display: inline-block;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .header-container {
                padding: 12px 0;
            }
        }
        </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='header-container'>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1.8, 4.2, 2])
        
        # --- LEFT: LOGO ---
        with c1:
            if st.button("📄 RESULYZE", key="logo_btn", width="content"):
                st.session_state.current_page = "Landing"
                st.rerun()
            # Style the logo button - PINK
            st.markdown("""
                <style>
                button[key="logo_btn"] {
                    background: transparent !important;
                    border: none !important;
                    font-size: 26px !important;
                    font-weight: 800 !important;
                    font-family: 'Outfit', sans-serif !important;
                    padding: 0 !important;
                    color: transparent !important;
                    background-image: linear-gradient(135deg, #EC4899 0%, #DB2777 100%) !important;
                    -webkit-background-clip: text !important;
                    background-clip: text !important;
                    box-shadow: none !important;
                    transition: all 0.3s ease !important;
                }
                button[key="logo_btn"]:hover {
                    transform: scale(1.05) !important;
                    filter: brightness(1.1) !important;
                }
                </style>
            """, unsafe_allow_html=True)
        
        # --- CENTER: NAVIGATION LINKS ---
        with c2:
            nav_items = [
                ("Home", "Landing"),
                ("Services", "Services"),
                ("Blogs", "Blogs"),
                ("Resume Tips", "Resume Tips"),
                ("About", "About"),
                ("Pricing", "Pricing"),
                ("FAQ", "FAQ")
            ]
            
            cols = st.columns(len(nav_items))
            for idx, (label, page) in enumerate(nav_items):
                with cols[idx]:
                    is_active = current == page
                    # Style buttons based on active state - PINK
                    if is_active:
                        st.markdown(f"""
                            <style>
                            button[key="nav_{label.lower()}"] {{
                                background: linear-gradient(135deg, rgba(236, 72, 153, 0.1) 0%, rgba(219, 39, 119, 0.1) 100%) !important;
                                color: #EC4899 !important;
                                font-weight: 600 !important;
                                border: 1px solid rgba(236, 72, 153, 0.2) !important;
                            }}
                            </style>
                            
                        """, unsafe_allow_html=True)
                    
                    if st.button(label, key=f"nav_{label.lower()}", width="stretch"):
                        st.session_state.current_page = page
                        st.rerun() 
        
        # --- RIGHT: AUTH & USER INFO ---
        with c3:
            if is_logged_in:
                col_user, col_logout = st.columns([2.2, 1])
                with col_user:
                    st.markdown(f"""
                        <div class="user-greeting">
                            👋 Hi, {user_name.split()[0] if user_name else 'User'}
                        </div>
                    """, unsafe_allow_html=True)
                with col_logout:
                    if st.button("Logout", key="nav_logout", width="stretch", type="secondary"):
                        st.session_state.logged_in = False
                        st.session_state.user = None
                        st.session_state.auth_mode = False
                        st.session_state.current_page = "Landing"
                        st.rerun()
            else:
                col_login, col_signup = st.columns([1, 1])
                with col_login:
                    if st.button("Login", key="nav_login", width="stretch", type="primary"):
                        st.session_state.auth_mode = True
                        st.rerun()
                with col_signup:
                    if st.button("Sign Up", key="nav_signup", width="stretch", type="secondary"):
                        st.session_state.auth_mode = True
                        st.session_state.auth_tab = "signup"
                        st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Elegant gradient separator - PINK
    st.markdown("""
        <div style='
            height: 3px; 
            background: linear-gradient(90deg, 
                transparent 0%, 
                rgba(236, 72, 153, 0.3) 20%, 
                rgba(219, 39, 119, 0.5) 50%, 
                rgba(236, 72, 153, 0.3) 80%, 
                transparent 100%
            ); 
            margin: 0 0 10px 0;
            border-radius: 2px;
        '></div>
    """, unsafe_allow_html=True)
    
def show_sidebar_navbar(active_page):
    # We use top navbar instead of sidebar
    pass
