import streamlit as st

def show_suggestions(suggestions):
    st.subheader("Suggestions 💡")
    for suggestion in suggestions:
        st.warning(suggestion)
