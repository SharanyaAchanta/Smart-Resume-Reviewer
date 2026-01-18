import streamlit as st
import re
import time
import components.login
import utils.db as db


def is_valid_email(email: str):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        return False, "Invalid email format"

    fake_domains = ["gml.cm", "test.com", "example.com", "fake.com"]
    domain = email.lower().split("@")[-1]
    if domain in fake_domains:
        return False, "Invalid email domain"

    real_domains = [
        "gmail.com", "yahoo.com", "outlook.com", "hotmail.com",
        "icloud.com", "protonmail.com", "aol.com",
    ]
    if not any(domain.endswith(real_domain) for real_domain in real_domains):
        return False, "❌ Only Gmail, Yahoo, Outlook, etc. allowed"

    return True, ""


def get_password_strength(password: str):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("≥8 chars")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Uppercase")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Lowercase")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Special char")

    strength = ["🔴 Very Weak", "🟡 Weak", "🟠 Medium", "🟢 Strong", "🟣 Very Strong"][min(score, 4)]
    return score, strength, feedback if feedback else []


def show_login_page():
    """Professional standalone auth UI with modern design."""

    # ---- PROFESSIONAL AUTH UI CSS ----
    st.markdown(
        """
        <style>
        .auth-wrapper {
            min-height: 85vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            background: transparent; /* Handled by global body gradient */
        }
        
        .auth-card {
            width: 100%;
            max-width: 460px;
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.6);
            border-radius: 28px;
            padding: 40px;
            box-shadow: 0 20px 60px -12px rgba(236, 72, 153, 0.15);
            position: relative;
            z-index: 10;
        }
        
        .auth-logo-icon {
            width: 64px;
            height: 64px;
            background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            margin: 0 auto 20px;
            color: white;
            box-shadow: 0 10px 25px -5px rgba(236, 72, 153, 0.3);
        }
        
        .auth-title {
            font-size: 28px;
            font-weight: 800;
            text-align: center;
            margin-bottom: 8px;
            background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: 'Outfit', sans-serif;
        }
        
        .auth-sub {
            text-align: center;
            color: #64748B;
            font-size: 15px;
            margin-bottom: 32px;
            line-height: 1.5;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ---- STATE ----
    if "auth_tab" not in st.session_state:
        st.session_state.auth_tab = "login"

    def switch_tab(tab: str):
        st.session_state.auth_tab = tab
        st.rerun()

    # ---- WRAPPER & CARD ----
    st.markdown("<div class='auth-wrapper'><div class='auth-card'>", unsafe_allow_html=True)

    # Logo and Title
    st.markdown("""
        <div class='auth-logo'>
            <div class='auth-logo-icon'>📄</div>
        </div>
        <div class='auth-title'>Smart Resume Analyzer</div>
        <div class='auth-sub'>Sign in to access AI-powered resume insights</div>
    """, unsafe_allow_html=True)

    # ---- TABS (LOGIN / SIGNUP) ----
    col_login, col_signup = st.columns(2)
    with col_login:
        if st.button("Login", key="auth_tab_login", width="stretch"):
            switch_tab("login")
    with col_signup:
        if st.button("Sign Up", key="auth_tab_signup", width="stretch"):
            switch_tab("signup")

    st.markdown("<div style='height: 24px'></div>", unsafe_allow_html=True)

    # ---- LOGIN FORM ----
    if st.session_state.auth_tab == "login":
        email = st.text_input("Email Address", key="login_email_page", placeholder="your.email@example.com")
        password = st.text_input("Password", type="password", key="login_password_page", placeholder="Enter your password")

        # Forgot password link
        st.markdown("""
            <div style="text-align: right; margin-top: -10px; margin-bottom: 20px;">
                <a href="#" style="color: #EC4899; text-decoration: none; font-size: 14px; font-weight: 500;">Forgot password?</a>
            </div>
        """, unsafe_allow_html=True)

        if st.button("Sign In", key="login_submit_page", width="stretch", type="primary"):
            if not email or not password:
                st.error("⚠️ Please fill in all fields.")
            else:
                with st.spinner("Signing you in..."):
                    user = db.verify_user(email, password)
                    if user:
                        st.session_state.logged_in = True
                        st.session_state.user = user
                        st.session_state.auth_mode = False
                        
                        # Handle Redirect
                        target = st.session_state.get("redirect_target", "Landing")
                        st.session_state.current_page = target
                        st.session_state.redirect_target = None
                        
                        st.success(f"✅ Welcome back, {user['name']}!")
                        time.sleep(0.8)
                        st.rerun()
                    else:
                        st.error("❌ Invalid email or password. Please try again.")

        st.markdown(
            "<div class='auth-footer'>Don't have an account? <a href='#'>Sign up</a> to get started.</div>",
            unsafe_allow_html=True,
        )

    # ---- SIGNUP FORM ----
    else:
        name = st.text_input("Full Name", key="signup_name_page", placeholder="John Doe")
        email = st.text_input("Email Address", key="signup_email_page", placeholder="your.email@example.com")
        password = st.text_input("Password", type="password", key="signup_password_page", placeholder="Create a strong password")
        confirm = st.text_input("Confirm Password", type="password", key="signup_confirm_page", placeholder="Confirm your password")

        # Password strength indicator
        if password:
            score, strength, feedback = get_password_strength(password)
            strength_class = "strength-weak" if score < 3 else "strength-medium" if score < 4 else "strength-strong"
            st.markdown(f"""
                <div class="password-strength {strength_class}">
                    Password Strength: {strength}
                </div>
            """, unsafe_allow_html=True)
            if feedback:
                st.caption(f"Add: {', '.join(feedback)}")

        if st.button("Create Account", key="signup_submit_page", width="stretch", type="primary"):
            if not all([name, email, password, confirm]):
                st.error("⚠️ Please fill in all fields.")
            elif password != confirm:
                st.error("❌ Passwords do not match. Please try again.")
            elif len(password) < 8:
                st.error("❌ Password must be at least 8 characters long.")
            else:
                ok, msg = is_valid_email(email)
                if not ok:
                    st.error(f"❌ {msg}")
                else:
                    with st.spinner("Creating your account..."):
                        success, msg = db.create_user(email, password, name)
                        if success:
                            # Auto-login
                            user = db.verify_user(email, password)
                            st.session_state.logged_in = True
                            st.session_state.user = user
                            st.session_state.auth_mode = False
                            
                            # Handle Redirect
                            target = st.session_state.get("redirect_target", "Landing")
                            st.session_state.current_page = target
                            st.session_state.redirect_target = None
                            
                            st.success("🎉 Account created successfully!")
                            time.sleep(0.8)
                            st.rerun()
                        else:
                            st.error(f"❌ {msg}")

        st.markdown(
            "<div class='auth-footer'>Already have an account? <a href='#'>Sign in</a> instead.</div>",
            unsafe_allow_html=True,
        )

    st.markdown("</div></div>", unsafe_allow_html=True)

# Alias for app.py import compatibility
show_login = show_login_page
