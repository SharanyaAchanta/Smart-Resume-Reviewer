"""
Resume Preview Component
Displays preview of uploaded resume files
"""

import streamlit as st
from utils.preview_generator import (
    generate_pdf_preview,
    generate_text_preview,
    generate_docx_preview,
    resize_preview_image
)


def show_resume_preview(uploaded_file, show_full_preview=False):
    """
    Display preview of uploaded resume file

    Args:
        uploaded_file: Streamlit uploaded file object
        show_full_preview: If True, show expanded preview

    Returns:
        bool: True if preview was generated successfully
    """
    if not uploaded_file:
        return False

    try:
        # Get file details
        file_name = uploaded_file.name
        file_extension = file_name.split('.')[-1].lower() if '.' in file_name else ''
        file_size_mb = uploaded_file.size / (1024 * 1024)

        # Read file bytes
        uploaded_file.seek(0)
        file_bytes = uploaded_file.read()
        uploaded_file.seek(0)

        # Create preview card
        st.markdown('<div class="streamlit-card fade-in">', unsafe_allow_html=True)
        st.subheader("📄 Resume Preview")

        # Show file info
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("File Name", file_name)
        with col2:
            st.metric("Type", file_extension.upper())
        with col3:
            st.metric("Size", f"{file_size_mb:.2f} MB")

        st.divider()

        # Generate preview based on file type
        if file_extension == 'pdf':
            preview_success = _show_pdf_preview(file_bytes, show_full_preview)

        elif file_extension == 'txt':
            preview_success = _show_text_preview(file_bytes)

        elif file_extension in ['docx', 'doc']:
            preview_success = _show_docx_preview(file_bytes)

        else:
            st.warning(f"Preview not available for {file_extension.upper()} files")
            preview_success = False

        st.markdown('</div>', unsafe_allow_html=True)

        return preview_success

    except Exception as e:
        st.error(f"Error generating preview: {str(e)}")
        return False


def _show_pdf_preview(pdf_bytes, show_full=False):
    """Display PDF preview"""
    try:
        st.info("🔍 Generating PDF preview...")

        # Generate preview image
        preview_img = generate_pdf_preview(pdf_bytes, page_number=0, zoom=2.0)

        if preview_img:
            # Resize for display
            preview_img = resize_preview_image(preview_img, max_width=800)

            # Display image
            st.image(
                preview_img,
                caption="First Page Preview",
                use_container_width=True
            )

            if not show_full:
                st.caption("ℹ️ Showing first page only")

            return True
        else:
            st.warning("Unable to generate PDF preview")
            return False

    except Exception as e:
        st.error(f"PDF preview error: {str(e)}")
        return False


def _show_text_preview(text_bytes):
    """Display TXT file preview"""
    try:
        # Generate text preview
        preview_text = generate_text_preview(text_bytes, max_chars=1500)

        if preview_text:
            # Display in text area
            st.text_area(
                "Text Content Preview",
                preview_text,
                height=400,
                disabled=True
            )

            return True
        else:
            st.warning("Unable to generate text preview")
            return False

    except Exception as e:
        st.error(f"Text preview error: {str(e)}")
        return False


def _show_docx_preview(docx_bytes):
    """Display DOCX file preview"""
    try:
        # Generate DOCX preview
        preview_text = generate_docx_preview(docx_bytes)

        # Display preview
        st.info(preview_text)

        st.caption("ℹ️ DOCX preview feature is under development")

        return True

    except Exception as e:
        st.error(f"DOCX preview error: {str(e)}")
        return False


def show_preview_card_compact(uploaded_file):
    """
    Show compact preview card (thumbnail only)

    Args:
        uploaded_file: Streamlit uploaded file object
    """
    if not uploaded_file:
        return

    file_name = uploaded_file.name
    file_extension = file_name.split('.')[-1].lower() if '.' in file_name else ''

    with st.expander("📄 Resume Preview", expanded=False):
        if file_extension == 'pdf':
            uploaded_file.seek(0)
            file_bytes = uploaded_file.read()
            uploaded_file.seek(0)

            preview_img = generate_pdf_preview(file_bytes, zoom=1.5)
            if preview_img:
                preview_img = resize_preview_image(preview_img, max_width=400)
                st.image(preview_img, caption="Preview", use_container_width=True)
            else:
                st.info("Preview not available")

        elif file_extension == 'txt':
            uploaded_file.seek(0)
            file_bytes = uploaded_file.read()
            uploaded_file.seek(0)

            preview_text = generate_text_preview(file_bytes, max_chars=500)
            st.text_area("Preview", preview_text, height=200, disabled=True)

        else:
            st.info(f"Preview for {file_extension.upper()} files coming soon!")
