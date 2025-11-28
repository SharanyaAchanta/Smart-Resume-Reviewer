# components/upload_card.py
import streamlit as st

def upload_card():
    """
    Modern upload card that returns the uploaded file object (or None).
    Uses a non-empty label to avoid Streamlit accessibility warnings.
    """
    st.markdown('<div class="streamlit-card">', unsafe_allow_html=True)
    st.subheader("Upload Your Resume")
    st.write("Please upload a PDF or DOCX resume to get detailed feedback.")

    uploaded = st.file_uploader(
        "Choose a resume file",     # <- non-empty label fixes warning
        type=['pdf', 'docx'],
        key="resume_uploader",
        label_visibility="collapsed"  # keeps UI clean but accessible
    )

    if uploaded:
        st.success("File received — processing...")
    else:
        st.info("No file uploaded yet.")
    st.markdown('</div>', unsafe_allow_html=True)

    return uploaded
