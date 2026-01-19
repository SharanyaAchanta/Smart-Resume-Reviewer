import streamlit as st
from datetime import datetime

# -------- INITIALIZE HISTORY --------
def init_history():
    if "review_history" not in st.session_state:
        st.session_state.review_history = []
    if "selected_review" not in st.session_state:
        st.session_state.selected_review = None


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

    st.sidebar.title("📂 Resume History")

    # If no history yet
    if len(st.session_state.review_history) == 0:
        st.sidebar.info("No resume reviews yet")
        return

    # --- CLEAR HISTORY BUTTON ---
    if st.sidebar.button("🧹 Clear All History"):
        st.session_state.review_history = []
        st.session_state.selected_review = None
        st.rerun()

    st.sidebar.markdown("---")

    # Show each review
    for idx, review in enumerate(st.session_state.review_history):

        # Button Label
        label = f"{review['time']} | {review['role']} ({review['score']}/100)"

        # Highlight selected button
        if (
            st.session_state.selected_review
            and st.session_state.selected_review == review
        ):
            st.sidebar.success(label)
        else:
            if st.sidebar.button(
                label,
                key=f"history_btn_{idx}",
                width="stretch"
            ):
                st.session_state.selected_review = review

        # --- DELETE SINGLE REVIEW ---
        if st.sidebar.button(
            f"❌ Delete {review['role']}",
            key=f"del_{idx}"
        ):
            st.session_state.review_history.pop(idx)
            st.session_state.selected_review = None
            st.rerun()

    # --- SHOW SELECTED REVIEW DETAILS ---
    if st.session_state.selected_review:
        st.sidebar.markdown("---")
        r = st.session_state.selected_review

        st.sidebar.subheader("📌 Selected Review")
        st.sidebar.write(f"**Role:** {r['role']}")
        st.sidebar.write(f"**Score:** `{r['score']}/100`")
        st.sidebar.write(f"**Predicted Role:** {r['predicted']}")

        if r["suggestions"]:
            st.sidebar.write("**Top Suggestions:**")
            for s in r["suggestions"]:
                st.sidebar.warning(s)
