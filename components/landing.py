import streamlit as st

def show_landing_page():
    """Professional landing page with modern design."""
    
    # Professional landing page CSS
    st.markdown("""
        <style>
        .landing-hero {
            background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
            padding: 80px 40px;
            border-radius: 24px;
            margin: 0 0 40px 0;
            position: relative;
            overflow: hidden;
            box-shadow: 0 20px 40px -10px rgba(236, 72, 153, 0.4);
        }
        
        .landing-hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at top right, rgba(255,255,255,0.2), transparent 40%);
            opacity: 0.8;
        }
        
        .hero-content {
            position: relative;
            z-index: 1;
            text-align: center;
        }
        
        .hero-title {
            font-size: 4rem;
            font-weight: 800;
            color: white;
            margin-bottom: 20px;
            line-height: 1.1;
            font-family: 'Outfit', sans-serif;
            text-shadow: 0 4px 20px rgba(0,0,0,0.1);
            animation: fadeInUp 0.8s ease-out;
        }
        
        .hero-subtitle {
            font-size: 1.4rem;
            color: rgba(255, 255, 255, 0.9);
            line-height: 1.6;
            margin-bottom: 40px;
            font-weight: 400;
            font-family: 'Outfit', sans-serif;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            animation: fadeInUp 1s ease-out;
        }
        
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .feature-card {
            background: white;
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0 10px 30px -5px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
            border: 1px solid #F1F5F9;
            text-align: center;
            height: 100%;
        }
        
        .feature-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px -10px rgba(236, 72, 153, 0.15);
            border-color: #FBCFE8;
        }
        
        .feature-icon {
            font-size: 48px;
            margin-bottom: 20px;
            display: inline-block;
            background: rgba(236, 72, 153, 0.05);
            padding: 15px;
            border-radius: 16px;
        }
        
        .feature-title {
            font-size: 20px;
            font-weight: 700;
            color: #1E293B;
            margin-bottom: 12px;
            font-family: 'Outfit', sans-serif;
        }
        
        .feature-desc {
            color: #64748B;
            font-size: 15px;
            line-height: 1.6;
            font-family: 'Outfit', sans-serif;
        }
        
        .section-title {
            font-size: 2.5rem;
            font-weight: 800;
            text-align: center;
            margin: 80px 0 50px 0;
            background: #1E293B; /* fallback */
            background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: 'Outfit', sans-serif;
        }
        
        .stats-container {
            display: flex;
            justify-content: space-around;
            margin: 80px 0;
            padding: 50px;
            background: white;
            border-radius: 24px;
            box-shadow: 0 20px 40px -10px rgba(236, 72, 153, 0.1);
            border: 1px solid #FBCFE8;
        }
        
        .stat-number {
            font-size: 3.5rem;
            font-weight: 800;
            color: #EC4899;
            font-family: 'Outfit', sans-serif;
            margin-bottom: 5px;
        }
        
        .stat-label {
            font-size: 1.1rem;
            color: #64748B;
            font-weight: 500;
            font-family: 'Outfit', sans-serif;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # --- HERO SECTION ---
    # --- HERO SECTION ---
    hero_col1, hero_col2 = st.columns([1.2, 1])
    
    with hero_col1:
        st.markdown("""
            <div class="landing-hero-text">
                <h1 class="hero-title">Transform Your Resume<br>with AI-Powered Insights</h1>
                <p class="hero-subtitle">
                    Get instant feedback on your resume, optimize for ATS systems, 
                    and land your dream job faster. Trusted by thousands of job seekers.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # CTA Buttons
        col_cta1, col_cta2 = st.columns([1, 1.5])
        with col_cta1:
            if st.button("🚀 Analyze Resume", key="land_analyze", use_container_width=True, type="primary"):
                if st.session_state.get("logged_in", False):
                    st.session_state.current_page = "Analyzer"
                    st.rerun()
                else:
                    st.session_state.auth_mode = True
                    st.session_state.auth_tab = "login"
                    st.rerun()
        with col_cta2:
            if st.button("✨ Build Resume", key="land_build", use_container_width=True, type="secondary"):
                if st.session_state.get("logged_in", False):
                    st.session_state.current_page = "Resume Builder"
                    st.rerun()
                else:
                    st.session_state.auth_mode = True
                    st.session_state.auth_tab = "signup"
                    st.rerun()

    with hero_col2:
        try:
            st.image("assets/hero_image.png", use_container_width=True)
        except:
            # Fallback if image doesn't exist
            st.markdown("""
                <div style="
                    background: rgba(255,255,255,0.2); 
                    border-radius: 20px; 
                    height: 400px; 
                    display: flex; 
                    align-items: center; 
                    justify-content: center;
                    border: 2px dashed rgba(255,255,255,0.5);
                ">
                    <span style="color: white; font-size: 50px;">🚀</span>
                </div>
            """, unsafe_allow_html=True)
    

    
    # Stats Section
    st.markdown("""
        <div class="stats-container">
            <div class="stat-item">
                <div class="stat-number">10K+</div>
                <div class="stat-label">Resumes Analyzed</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">95%</div>
                <div class="stat-label">Success Rate</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">4.9★</div>
                <div class="stat-label">User Rating</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # --- FEATURES SECTION ---
    st.markdown("<h2 class='section-title'>Why Choose Us?</h2>", unsafe_allow_html=True)
    
    f1, f2, f3 = st.columns(3)
    
    features = [
        {
            "icon": "🤖",
            "title": "AI-Powered Analysis",
            "desc": "Advanced machine learning algorithms analyze your resume for ATS compatibility, keyword optimization, and content quality."
        },
        {
            "icon": "⚡",
            "title": "Instant Results",
            "desc": "Get comprehensive feedback and actionable suggestions in seconds. No waiting, no delays - just instant insights."
        },
        {
            "icon": "🔒",
            "title": "100% Secure & Private",
            "desc": "Your data is processed securely and never stored. We respect your privacy and ensure complete confidentiality."
        }
    ]
    
    for idx, feature in enumerate(features):
        with [f1, f2, f3][idx]:
            st.markdown(f"""
                <div class="feature-card">
                    <span class="feature-icon">{feature['icon']}</span>
                    <div class="feature-title">{feature['title']}</div>
                    <div class="feature-desc">{feature['desc']}</div>
                </div>
            """, unsafe_allow_html=True)
    
    # Additional Features
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    f4, f5, f6 = st.columns(3)
    
    additional_features = [
        {
            "icon": "📊",
            "title": "Detailed Analytics",
            "desc": "Get comprehensive scores for structure, content, and keyword matching with visual breakdowns."
        },
        {
            "icon": "🎯",
            "title": "Role-Specific Insights",
            "desc": "Tailor your resume for specific job roles with targeted keyword suggestions and industry best practices."
        },
        {
            "icon": "💼",
            "title": "Career Growth",
            "desc": "Track your resume improvements over time and see how your profile evolves with our analytics dashboard."
        }
    ]
    
    for idx, feature in enumerate(additional_features):
        with [f4, f5, f6][idx]:
            st.markdown(f"""
                <div class="feature-card">
                    <span class="feature-icon">{feature['icon']}</span>
                    <div class="feature-title">{feature['title']}</div>
                    <div class="feature-desc">{feature['desc']}</div>
                </div>
            """, unsafe_allow_html=True)
