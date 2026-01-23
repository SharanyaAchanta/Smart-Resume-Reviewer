# components/upload_card.py
import streamlit as st
import magic

# Validation constants
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024  # 5MB in bytes
ALLOWED_FILE_TYPES = ['pdf', 'docx', 'txt']

# MIME type mappings
ALLOWED_MIME_TYPES = {
    'application/pdf': 'pdf',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
    'application/msword': 'doc',  # Older DOC format
    'text/plain': 'txt',
    'application/octet-stream': None  # Generic binary - will check extension
}

def validate_mime_type(uploaded_file):
    """
    Validates the uploaded file's MIME type matches its extension.

    Returns:
        tuple: (is_valid: bool, error_message: str or None, detected_mime: str)
    """
    if not uploaded_file:
        return True, None, None

    try:
        # Read first 2048 bytes for MIME detection
        uploaded_file.seek(0)
        file_header = uploaded_file.read(2048)
        uploaded_file.seek(0)

        # Detect MIME type
        mime_type = magic.from_buffer(file_header, mime=True)

        # Get file extension
        file_name = uploaded_file.name
        file_extension = file_name.split('.')[-1].lower() if '.' in file_name else ''

        # Check if MIME type is allowed
        if mime_type not in ALLOWED_MIME_TYPES:
            return False, f"❌ Security Warning: File content type '{mime_type}' is not allowed. Only PDF, DOCX, and TXT files are permitted.", mime_type

        # Special handling for application/octet-stream (check extension)
        if mime_type == 'application/octet-stream':
            if file_extension not in ALLOWED_FILE_TYPES:
                return False, f"❌ Invalid file type '.{file_extension}'. Only PDF, DOCX, TXT files are allowed.", mime_type
            return True, None, mime_type

        # Verify MIME type matches extension
        expected_extension = ALLOWED_MIME_TYPES[mime_type]
        if expected_extension and file_extension != expected_extension:
            return False, f"❌ Security Warning: File extension '.{file_extension}' doesn't match actual content type ({mime_type}). Upload rejected for security.", mime_type

        return True, None, mime_type

    except Exception as e:
        return False, f"❌ Error validating file: {str(e)}", None

def validate_uploaded_file(uploaded_file):
    """
    Validates the uploaded file for size, type, and MIME type.

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

    # Validate MIME type (content-based validation)
    is_valid_mime, mime_error, detected_mime = validate_mime_type(uploaded_file)
    if not is_valid_mime:
        return False, mime_error

    return True, None

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
    Includes file size, type, and MIME type validation for security.
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
            st.success(f" File received ({file_size_mb:.2f} MB) — processing...")
    else:
        st.info(" No file uploaded yet.")

    st.markdown('</div>', unsafe_allow_html=True)

    return uploaded
