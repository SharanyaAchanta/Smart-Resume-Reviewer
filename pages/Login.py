import streamlit as st

st.set_page_config(page_title="Login", layout="centered")

# ---- PAGE SWITCHING ----
if "auth_page" not in st.session_state:
    st.session_state.auth_page = "login"


def switch_to_signup():
    st.session_state.auth_page = "signup"
    st.rerun()

def switch_to_login():
    st.session_state.auth_page = "login"
    st.rerun()


# ---- CSS ----
st.markdown("""
<style>

.auth-title {
    text-align: center;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 6px;
}

.auth-sub {
    text-align: center;
    color: #667085;
    margin-bottom: 28px;
}

input, .stTextInput > div > input {
    border-radius: 10px !important;
    padding: 12px !important;
    border: 1.5px solid #d0d5dd !important;
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

/* hyperlink-style buttons */
.hyper-btn button {
    background: none !important;
    color: #6366f1 !important;
    border: none !important;
    padding: 0 !important;
    font-size: 14px !important;
    text-decoration: underline !important;
    width: auto !important;
}

.center-text {
    text-align: center;
    margin-top: 14px;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

</style>
""", unsafe_allow_html=True)

# ---- LOGIN PAGE ----
if st.session_state.auth_page == "login":
    st.markdown("<h2 class='auth-title'>Welcome Back 👋</h2>", unsafe_allow_html=True)
    st.markdown("<p class='auth-sub'>Login to continue</p>", unsafe_allow_html=True)

    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        if not email or not password:
            st.error("Please fill in all fields.")
        else:
            st.success("Logged in successfully!")

    st.markdown("<div class='center-text'>Don't have an account?</div>", unsafe_allow_html=True)

    # hyperlink-style signup button
    if st.button("Sign up", key="go_signup", help="Go to Signup", type="secondary", use_container_width=False):
        switch_to_signup()

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


# ---- SIGNUP PAGE ----
if st.session_state.auth_page == "signup":
    st.markdown("<h2 class='auth-title'>Create Account ✨</h2>", unsafe_allow_html=True)
    st.markdown("<p class='auth-sub'>Fill in your details</p>", unsafe_allow_html=True)

    name = st.text_input("Full Name", key="signup_name")
    email = st.text_input("Email", key="signup_email")
    password = st.text_input("Password", type="password", key="signup_password")
    confirm = st.text_input("Confirm Password", type="password", key="signup_confirm")

    if st.button("Create Account"):
        if not name or not email or not password or not confirm:
            st.error("All fields are required.")
        elif password != confirm:
            st.error("Passwords do not match.")
        else:
            st.success("Account created successfully!")

    st.markdown("<div class='center-text'>Already have an account?</div>", unsafe_allow_html=True)

    # hyperlink-style login button
    if st.button("Login", key="go_login", type="secondary", use_container_width=False):
        switch_to_login()

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

