import streamlit as st
from datetime import datetime

# -------- INITIALIZE HISTORY --------
def init_history():
    if "review_history" not in st.session_state:
        st.session_state.review_history = []

# -------- SAVE A REVIEW --------
def save_review(role, score, predicted_role, suggestions):
    init_history()

    entry = {
        "time": datetime.now().strftime("%d-%m-%Y  %I:%M %p"),
        "role": role,
        "score": score,
        "predicted": predicted_role,
        "suggestions": suggestions[:3] if suggestions else []
    }

    st.session_state.review_history.append(entry)

# -------- SHOW SIDEBAR UI --------
def show_history_ui():
    init_history()

    st.sidebar.markdown("### 🕒 Resume Review History")

    if len(st.session_state.review_history) == 0:
        st.sidebar.info("No resume analyzed yet.")
        return

    for item in st.session_state.review_history[::-1]:
        with st.sidebar.expander(f"{item['role']} • Score: {item['score']}"):
            st.write(f"**Time:** {item['time']}")
            st.write(f"**AI Predicted:** {item['predicted']}")
            if item["suggestions"]:
                st.write("**Key Suggestions:**")
                for s in item["suggestions"]:
                    st.write("- ", s)
