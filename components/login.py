import streamlit as st
import re


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
    """Standalone, full-page auth UI (Login + Signup tabs)."""

    # ---- BASIC PAGE LAYOUT CSS ----
    st.markdown(
        """
        <style>
        .auth-wrapper {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px 16px;
            background: radial-gradient(circle at top, #1e293b 0, #020617 45%, #000000 100%);
        }
        .auth-card {
            width: 100%;
            max-width: 480px;
            background: linear-gradient(145deg, #020617 0%, #0b1120 60%, #020617 100%);
            border-radius: 20px;
            padding: 28px 26px 26px;
            box-shadow: 0 24px 60px rgba(0,0,0,0.75);
            border: 1px solid rgba(148,163,184,0.3);
        }
        .auth-title {
            font-size: 28px;
            font-weight: 800;
            text-align: center;
            margin-bottom: 6px;
            background: linear-gradient(135deg, #4f46e5 0%, #22c55e 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .auth-sub {
            text-align: center;
            color: #9ca3af;
            font-size: 14px;
            margin-bottom: 22px;
        }
        .auth-tabs {
            display: flex;
            gap: 6px;
            margin-bottom: 18px;
            background: rgba(15,23,42,0.8);
            padding: 4px;
            border-radius: 999px;
            border: 1px solid rgba(55,65,81,0.8);
        }
        .auth-tab {
            flex: 1;
            text-align: center;
            padding: 8px 0;
            font-size: 14px;
            font-weight: 600;
            border-radius: 999px;
            cursor: pointer;
            color: #9ca3af;
        }
        .auth-tab.active {
            background: linear-gradient(135deg, #4f46e5 0%, #22c55e 100%);
            color: #f9fafb;
        }
        .auth-footer {
            margin-top: 18px;
            text-align: center;
            font-size: 12px;
            color: #6b7280;
        }
        .auth-footer a {
            color: #22c55e;
            text-decoration: none;
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
        st.experimental_rerun()

    # ---- WRAPPER & CARD ----
    st.markdown("<div class='auth-wrapper'><div class='auth-card'>", unsafe_allow_html=True)

    st.markdown("<div class='auth-title'>Smart Resume Analyzer</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='auth-sub'>Sign in to access your AI resume insights, or create a new account.</div>",
        unsafe_allow_html=True,
    )

    # ---- TABS (LOGIN / SIGNUP) ----
    col_login, col_signup = st.columns(2)
    with col_login:
        st.markdown(
            f"<div class='auth-tabs'><div class='auth-tab {'active' if st.session_state.auth_tab=='login' else ''}' "
            f"onclick=\"window.location.reload()\">Login</div></div>",
            unsafe_allow_html=True,
        )
    with col_signup:
        pass  # purely visual; the actual switching is done with buttons below

    # Real tab switch buttons (no layout issues)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Login", key="auth_tab_login", use_container_width=True):
            switch_tab("login")
    with c2:
        if st.button("Sign up", key="auth_tab_signup", use_container_width=True):
            switch_tab("signup")

    st.markdown("---")

    # ---- LOGIN FORM ----
    if st.session_state.auth_tab == "login":
        email = st.text_input("Email", key="login_email_page")
        password = st.text_input("Password", type="password", key="login_password_page")

        if email:
            ok, msg = is_valid_email(email)
            if not ok:
                st.markdown(f"<div class='field-error'>{msg}</div>", unsafe_allow_html=True)

        if password:
            score, strength, feedback = get_password_strength(password)
            st.markdown(
                f"<div class='password-strength'><b>Password: {strength}</b></div>",
                unsafe_allow_html=True,
            )
            if feedback:
                st.caption(f"Needs: {', '.join(feedback)}")
            else:
                st.caption("✅ Strong password!")

        if st.button("Login", key="login_submit_page", use_container_width=True):
            if not email or not password:
                st.error("Please fill in all fields.")
            else:
                ok, msg = is_valid_email(email)
                if not ok:
                    st.error(msg)
                else:
                    st.session_state.logged_in = True
                    st.session_state.auth_mode = False   # leave auth page
                    st.session_state.current_page = "Home"
                    st.success("Logged in successfully!")
                    st.experimental_rerun()

        st.markdown(
            "<div class='auth-footer'>Don't have an account? Use the signup tab above.</div>",
            unsafe_allow_html=True,
        )

    # ---- SIGNUP FORM ----
    else:
        name = st.text_input("Full Name", key="signup_name_page")
        email = st.text_input("Email", key="signup_email_page")
        password = st.text_input("Password", type="password", key="signup_password_page")
        confirm = st.text_input("Confirm Password", type="password", key="signup_confirm_page")

        if email:
            ok, msg = is_valid_email(email)
            if not ok:
                st.markdown(f"<div class='field-error'>{msg}</div>", unsafe_allow_html=True)

        if password:
            score, strength, feedback = get_password_strength(password)
            st.markdown(
                f"<div class='password-strength'><b>Password: {strength}</b></div>",
                unsafe_allow_html=True,
            )
            if feedback:
                st.caption(f"Needs: {', '.join(feedback)}")

        if password and confirm and password != confirm:
            st.markdown("<div class='field-error'>Passwords do not match</div>", unsafe_allow_html=True)

        if st.button("Create Account", key="signup_submit_page", use_container_width=True):
            if not all([name, email, password, confirm]):
                st.error("Please fill in all fields.")
            elif password != confirm:
                st.error("Passwords do not match.")
            else:
                ok, msg = is_valid_email(email)
                if not ok:
                    st.error(msg)
                else:
                    st.session_state.logged_in = True
                    st.session_state.auth_mode = False   # leave auth page
                    st.session_state.current_page = "Home"
                    st.success("Account created successfully!")
                    st.experimental_rerun()

        st.markdown(
            "<div class='auth-footer'>Already have an account? Switch to the login tab above.</div>",
            unsafe_allow_html=True,
        )

    # ---- WRAPPER CLOSE ----
    st.markdown(
        "<div class='auth-footer'>By continuing you agree to our <a href='#'>Terms</a> and <a href='#'>Privacy Policy</a>.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div></div>", unsafe_allow_html=True)
