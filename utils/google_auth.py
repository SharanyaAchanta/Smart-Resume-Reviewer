import streamlit as st
import requests
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

# Configuration (Replace with your details from Step 1)
CLIENT_ID = "YOUR_CLIENT_ID.apps.googleusercontent.com"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDIRECT_URI = "http://localhost:8502"

def login_with_google():
    # 1. Create the Flow
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        scopes=["openid", "https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email"],
        redirect_uri=REDIRECT_URI
    )

    # 2. Check if we are returning from Google (URL has a 'code' parameter)
    query_params = st.query_params
    if "code" in query_params:
        try:
            flow.fetch_token(code=query_params["code"])
            credentials = flow.credentials
            
            # Verify the token
            info = id_token.verify_oauth2_token(
                credentials.id_token, google_requests.Request(), CLIENT_ID
            )

            # Store in session state
            st.session_state.logged_in = True
            st.session_state.user = {
                "uid": info.get("sub"),
                "name": info.get("name"),
                "email": info.get("email"),
                "photo": info.get("picture"),
                "auth_provider": "google"
            }
            # Clear the code from URL
            st.query_params.clear()
            st.rerun()
            
        except Exception as e:
            st.error(f"Login failed: {e}")

    # 3. If not logged in, show the button
    else:
        auth_url, _ = flow.authorization_url(prompt='consent')
        
        st.markdown(f"""
            <a href="{auth_url}" target="_self" style="text-decoration: none;">
                <div style="
                    display: flex; align-items: center; justify-content: center;
                    padding: 10px; border: 1px solid #ddd; border-radius: 8px;
                    background-color: white; color: #444; font-weight: bold; cursor: pointer;">
                    <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" width="20" style="margin-right: 10px;"/>
                    Continue with Google
                </div>
            </a>
        """, unsafe_allow_html=True)