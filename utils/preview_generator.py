"""
Resume Preview Generator
Generates previews for different file types (PDF, DOCX, TXT)
"""

import fitz  # PyMuPDF
from io import BytesIO
from PIL import Image


def generate_pdf_preview(file_bytes, page_number=0, zoom=2.0):
    """
    Generate preview image of a PDF page

    Args:
        file_bytes: PDF file bytes
        page_number: Page number to preview (default: 0 = first page)
        zoom: Zoom factor for preview quality (default: 2.0)

    Returns:
        bytes: PNG image bytes of the PDF page
    """
    try:
        # Open PDF from bytes
        doc = fitz.open(stream=file_bytes, filetype="pdf")

        # Check if page exists
        if page_number >= len(doc):
            page_number = 0

        # Get the specified page
        page = doc[page_number]

        # Create transformation matrix for zoom
        mat = fitz.Matrix(zoom, zoom)

        # Render page to pixmap
        pix = page.get_pixmap(matrix=mat)

        # Convert to PNG bytes
        img_bytes = pix.tobytes("png")

        doc.close()

        return img_bytes

    except Exception as e:
        print(f"Error generating PDF preview: {e}")
        return None


def generate_text_preview(file_bytes, max_chars=1000, encoding='utf-8'):
    """
    Generate text preview for TXT files

    Args:
        file_bytes: Text file bytes
        max_chars: Maximum characters to preview
        encoding: Text encoding (default: utf-8)

    Returns:
        str: Preview text
    """
    try:
        # Try UTF-8 first
        text = file_bytes.decode(encoding, errors='ignore')

        # Limit to max_chars
        if len(text) > max_chars:
            text = text[:max_chars] + "\n\n... (preview truncated)"

        return text

    except Exception as e:
        print(f"Error generating text preview: {e}")
        # Fallback to latin-1
        try:
            text = file_bytes.decode('latin-1', errors='ignore')
            if len(text) > max_chars:
                text = text[:max_chars] + "\n\n... (preview truncated)"
            return text
        except:
            return "Error: Unable to generate text preview"


def generate_docx_preview(file_bytes, max_chars=1000):
    """
    Generate text preview for DOCX files

    Args:
        file_bytes: DOCX file bytes
        max_chars: Maximum characters to preview

    Returns:
        str: Preview text extracted from DOCX
    """
    try:
        # For DOCX, we'll first convert to PDF using PyMuPDF
        # Or extract text directly if possible
        # For now, return a placeholder
        return "DOCX preview: First page content will be displayed here.\n\nNote: Full DOCX text extraction coming soon!"

    except Exception as e:
        print(f"Error generating DOCX preview: {e}")
        return "Error: Unable to generate DOCX preview"


def get_preview_dimensions(img_bytes):
    """
    Get dimensions of preview image

    Args:
        img_bytes: Image bytes

    Returns:
        tuple: (width, height) or None
    """
    try:
        img = Image.open(BytesIO(img_bytes))
        return img.size
    except:
        return None


def resize_preview_image(img_bytes, max_width=800):
    """
    Resize preview image to fit max width

    Args:
        img_bytes: Original image bytes
        max_width: Maximum width in pixels

    Returns:
        bytes: Resized image bytes
    """
    try:
        img = Image.open(BytesIO(img_bytes))

        # Calculate new dimensions
        width, height = img.size
        if width > max_width:
            ratio = max_width / width
            new_width = max_width
            new_height = int(height * ratio)

            # Resize image
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Convert back to bytes
        output = BytesIO()
        img.save(output, format='PNG')
        return output.getvalue()

    except Exception as e:
        print(f"Error resizing image: {e}")
        return img_bytes  # Return original if resize fails
