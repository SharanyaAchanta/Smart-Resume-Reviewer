# components/batch_upload.py
import streamlit as st

# Constants for batch upload
MIN_BATCH_FILES = 2
MAX_BATCH_FILES = 10
ALLOWED_FILE_TYPES = ['pdf', 'docx', 'txt']
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024


def validate_batch_files(uploaded_files):
    """
    Validates a list of uploaded files for batch processing.

    Args:
        uploaded_files: List of Streamlit UploadedFile objects

    Returns:
        tuple: (is_valid: bool, error_message: str or None, valid_files: list)
    """
    if not uploaded_files:
        return False, "❌ No files uploaded.", []

    # Check minimum and maximum file count
    file_count = len(uploaded_files)
    if file_count < MIN_BATCH_FILES:
        return False, f"❌ Please upload at least {MIN_BATCH_FILES} files for batch processing.", []

    if file_count > MAX_BATCH_FILES:
        return False, f"❌ Maximum {MAX_BATCH_FILES} files allowed. You uploaded {file_count} files.", []

    valid_files = []
    errors = []

    for uploaded_file in uploaded_files:
        # Check file size
        file_size = uploaded_file.size
        if file_size > MAX_FILE_SIZE_BYTES:
            size_mb = file_size / (1024 * 1024)
            errors.append(f"❌ {uploaded_file.name}: Size ({size_mb:.2f} MB) exceeds {MAX_FILE_SIZE_MB} MB limit")
            continue

        # Check file extension
        file_name = uploaded_file.name
        file_extension = file_name.split('.')[-1].lower() if '.' in file_name else ''

        if file_extension not in ALLOWED_FILE_TYPES:
            allowed_types_str = ', '.join([f.upper() for f in ALLOWED_FILE_TYPES])
            errors.append(f"❌ {uploaded_file.name}: Invalid type '.{file_extension}'. Allowed: {allowed_types_str}")
            continue

        # File is valid
        valid_files.append(uploaded_file)

    # If we have errors, return them
    if errors:
        error_message = "\n".join(errors)
        if valid_files:
            error_message += f"\n\n✅ {len(valid_files)} file(s) are valid."
        return len(valid_files) >= MIN_BATCH_FILES, error_message, valid_files

    return True, None, valid_files


def batch_upload_card():
    """
    Batch upload card component for uploading multiple resumes.

    Returns:
        list: List of valid uploaded files, or None if validation fails
    """
    st.markdown('<div class="streamlit-card fade-in">', unsafe_allow_html=True)
    st.subheader("📦 Batch Upload Resumes")
    st.write(f"Upload {MIN_BATCH_FILES}-{MAX_BATCH_FILES} resumes to analyze and compare them side-by-side.")

    # Info box with requirements
    st.info(
        f"**Requirements:**\n"
        f"- Upload {MIN_BATCH_FILES} to {MAX_BATCH_FILES} files\n"
        f"- Supported formats: {', '.join([t.upper() for t in ALLOWED_FILE_TYPES])}\n"
        f"- Maximum file size: {MAX_FILE_SIZE_MB} MB per file"
    )

    # Multiple file uploader
    uploaded_files = st.file_uploader(
        "Choose resume files",
        type=ALLOWED_FILE_TYPES,
        accept_multiple_files=True,
        key="batch_resume_uploader",
        label_visibility="collapsed"
    )

    if uploaded_files:
        # Validate the uploaded files
        is_valid, error_message, valid_files = validate_batch_files(uploaded_files)

        if error_message:
            if is_valid:
                st.warning(error_message)
            else:
                st.error(error_message)

        if is_valid and valid_files:
            st.success(f"✅ {len(valid_files)} file(s) ready for batch processing!")

            # Show file list preview
            with st.expander("📄 View uploaded files", expanded=False):
                for idx, file in enumerate(valid_files, 1):
                    file_size_kb = file.size / 1024
                    st.text(f"{idx}. {file.name} ({file_size_kb:.1f} KB)")

            st.markdown('</div>', unsafe_allow_html=True)
            return valid_files
        else:
            st.markdown('</div>', unsafe_allow_html=True)
            return None
    else:
        st.info("No files uploaded yet. Please upload resume files to begin batch analysis.")
        st.markdown('</div>', unsafe_allow_html=True)
        return None
