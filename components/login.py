import streamlit as st
import re

def show_login():
    # ---- BOTTOM POPUP MODAL CSS ----
    st.markdown("""
    <style>
    .login-modal {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 450px;
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border-radius: 20px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        border: 1px solid #e2e8f0;
        z-index: 1000;
        padding: 2rem;
        max-height: 90vh;
        overflow-y: auto;
    }
    .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.1);
        z-index: 999;
        pointer-events: none;
    }
    .auth-title {
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 6px;
        color: #1e293b;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .auth-sub {
        text-align: center;
        color: #64748b;
        margin-bottom: 28px;
        font-size: 15px;
    }
    input, .stTextInput > div > input {
        border-radius: 12px !important;
        padding: 14px !important;
        border: 2px solid #e2e8f0 !important;
        font-size: 15px !important;
    }
    .stButton > button {
        width: 100% !important;
        padding: 12px !important;
        border-radius: 10px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border: none !important;
        color: white !important;
        margin-top: 8px;
    }
    .center-text {
        text-align: center;
        margin-top: 14px;
    }
    .password-strength {
        margin-top: 8px;
        font-size: 14px;
    }
    .field-error {
        color: #ef4444 !important;
        font-size: 13px !important;
        margin-top: 4px !important;
        font-weight: 500 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Modal Overlay
    st.markdown('<div class="modal-overlay"></div>', unsafe_allow_html=True)
    st.markdown('<div class="login-modal">', unsafe_allow_html=True)

    # ---- PAGE SWITCHING ----
    if "auth_page" not in st.session_state:
        st.session_state.auth_page = "login"

    def switch_to_signup():
        st.session_state.auth_page = "signup"
        st.rerun()

    def switch_to_login():
        st.session_state.auth_page = "login"
        st.rerun()

    # ---- VALIDATION FUNCTIONS ----
    def is_valid_email(email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            return False, "Invalid email format"

        fake_domains = ['gml.cm', 'test.com', 'example.com', 'fake.com']
        domain = email.lower().split('@')[-1]
        if domain in fake_domains:
            return False, "Invalid email domain"

        real_domains = [
            'gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com',
            'icloud.com', 'protonmail.com', 'aol.com'
        ]
        if not any(domain.endswith(real_domain) for real_domain in real_domains):
            return False, "❌ Only Gmail, Yahoo, Outlook, etc. allowed"

        return True, ""

    def get_password_strength(password):
        score = 0
        feedback = []

        if len(password) >= 8: 
            score += 1
        else: 
            feedback.append("≥8 chars")

        if re.search(r'[A-Z]', password): 
            score += 1
        else: 
            feedback.append("Uppercase")

        if re.search(r'[a-z]', password): 
            score += 1
        else: 
            feedback.append("Lowercase")

        if re.search(r'\d', password): 
            score += 1
        else: 
            feedback.append("Number")

        if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password): 
            score += 1
        else: 
            feedback.append("Special char")

        strength = ["🔴 Very Weak", "🟡 Weak", "🟠 Medium", "🟢 Strong", "🟣 Very Strong"][min(score, 4)]
        return score, strength, feedback if feedback else []

    # ---- LOGIN PAGE ----
    if st.session_state.auth_page == "login":
        st.markdown("<h2 class='auth-title'>Welcome Back 👋</h2>", unsafe_allow_html=True)
        st.markdown("<p class='auth-sub'>Login to continue</p>", unsafe_allow_html=True)

        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if email:
            email_valid, email_msg = is_valid_email(email)
            if not email_valid:
                st.markdown(f'<div class="field-error">{email_msg}</div>', unsafe_allow_html=True)

        if password:
            score, strength, feedback = get_password_strength(password)
            st.markdown(
                f'<div class="password-strength"><b>Password: {strength}</b></div>',
                unsafe_allow_html=True,
            )
            if feedback:
                st.caption(f"Needs: {', '.join(feedback)}")
            else:
                st.caption("✅ Strong password!")

        if st.button("Login"):
            if not email or not password:
                st.error("Please fill in all fields.")
            else:
                email_valid, email_msg = is_valid_email(email)
                if not email_valid:
                    st.error(email_msg)
                else:
                    st.session_state.login_success = True
                    st.success("Logged in successfully!")

        st.markdown("<div class='center-text'>Don't have an account?</div>", unsafe_allow_html=True)
        if st.button("Sign up", key="go_signup", help="Go to Signup", type="secondary"):
            switch_to_signup()

    # ---- SIGNUP PAGE ----
    elif st.session_state.auth_page == "signup":
        st.markdown("<h2 class='auth-title'>Create Account ✨</h2>", unsafe_allow_html=True)
        st.markdown("<p class='auth-sub'>Fill in your details</p>", unsafe_allow_html=True)

        name = st.text_input("Full Name", key="signup_name")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")
        confirm = st.text_input("Confirm Password", type="password", key="signup_confirm")

        if email:
            email_valid, email_msg = is_valid_email(email)
            if not email_valid:
                st.markdown(f'<div class="field-error">{email_msg}</div>', unsafe_allow_html=True)

        if password:
            score, strength, feedback = get_password_strength(password)
            st.markdown(
                f'<div class="password-strength"><b>Password: {strength}</b></div>',
                unsafe_allow_html=True,
            )
            if feedback:
                st.caption(f"Needs: {', '.join(feedback)}")

        if password and confirm and password != confirm:
            st.markdown('<div class="field-error">Passwords do not match</div>', unsafe_allow_html=True)

        if st.button("Create Account"):
            if not all([name, email, password, confirm]):
                st.error("Please fill in all fields.")
            elif password != confirm:
                st.error("Passwords do not match.")
            else:
                email_valid, email_msg = is_valid_email(email)
                if not email_valid:
                    st.error(email_msg)
                else:
                    st.success("Account created successfully!")
                    st.session_state.auth_page = "login"
                    st.rerun()

        st.markdown("<div class='center-text'>Already have an account?</div>", unsafe_allow_html=True)
        if st.button("Log in", key="go_login", help="Go to Login", type="secondary"):
            switch_to_login()

    # Close modal containers
    st.markdown("</div>", unsafe_allow_html=True)  # Close login-modal
