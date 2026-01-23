# components/upload_card.py
import streamlit as st

# Validation constants
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024  # 5MB in bytes
ALLOWED_FILE_TYPES = ['pdf', 'docx', 'txt']

def validate_uploaded_file(uploaded_file):
    """
    Validates the uploaded file for size and type.

    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    if not uploaded_file:
        return True, None

    # Check file size
    file_size = uploaded_file.size
    if file_size > MAX_FILE_SIZE_BYTES:
        size_mb = file_size / (1024 * 1024)
        return False, f"❌ File size ({size_mb:.2f} MB) exceeds the maximum limit of {MAX_FILE_SIZE_MB} MB. Please upload a smaller file."

    # Check file type by extension
    file_name = uploaded_file.name
    file_extension = file_name.split('.')[-1].lower() if '.' in file_name else ''

    if file_extension not in ALLOWED_FILE_TYPES:
        allowed_types_str = ', '.join([f.upper() for f in ALLOWED_FILE_TYPES])
        return False, f"❌ Invalid file type '.{file_extension}'. Only {allowed_types_str} files are allowed."

    return True, None

def upload_card():
    """
    Modern upload card that returns the uploaded file object (or None).
    Uses a non-empty label to avoid Streamlit accessibility warnings.
    Includes file size and type validation.
    """
    st.markdown('<div class="streamlit-card fade-in">', unsafe_allow_html=True)
    st.subheader("Upload Your Resume")
    st.write(f"Please upload a PDF, DOCX, or TXT resume (max {MAX_FILE_SIZE_MB} MB) to get detailed feedback.")

    uploaded = st.file_uploader(
        "Choose a resume file",     # <- non-empty label fixes warning
        type=ALLOWED_FILE_TYPES,
        key="resume_uploader",
        label_visibility="collapsed"  # keeps UI clean but accessible
    )

    # Validate the uploaded file
    if uploaded:
        is_valid, error_message = validate_uploaded_file(uploaded)

        if not is_valid:
            st.error(error_message)
            st.markdown('</div>', unsafe_allow_html=True)
            return None
        else:
            file_size_mb = uploaded.size / (1024 * 1024)
            st.success(f"✅ File received ({file_size_mb:.2f} MB) — processing...")
    else:
        st.info("ℹ️ No file uploaded yet.")

    st.markdown('</div>', unsafe_allow_html=True)

    return uploaded
