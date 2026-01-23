"""
Test script for resume preview functionality
Tests preview generation for PDF, TXT, and DOCX files
"""

from utils.preview_generator import (
    generate_pdf_preview,
    generate_text_preview,
    generate_docx_preview,
    get_preview_dimensions,
    resize_preview_image
)
import os


def test_pdf_preview():
    """Test PDF preview generation"""
    print("\n" + "="*60)
    print("Test 1: PDF Preview Generation")
    print("="*60)

    # Create a simple test PDF content (header)
    pdf_header = b"%PDF-1.4\n%\xE2\xE3\xCF\xD3\n"
    pdf_content = pdf_header + b"\nSample PDF resume content"

    try:
        preview = generate_pdf_preview(pdf_content)
        if preview:
            print("✅ PDF preview generated successfully")
            print(f"   Preview size: {len(preview)} bytes")

            # Test dimensions
            dims = get_preview_dimensions(preview)
            if dims:
                print(f"   Dimensions: {dims[0]}x{dims[1]} pixels")
            return True
        else:
            print("❌ Failed to generate PDF preview")
            return False
    except Exception as e:
        print(f"❌ Error in PDF preview: {e}")
        return False


def test_text_preview():
    """Test TXT preview generation"""
    print("\n" + "="*60)
    print("Test 2: Text Preview Generation")
    print("="*60)

    test_text = b"""JOHN DOE
Senior Software Engineer
Email: john@example.com | Phone: +1-234-567-8900

SUMMARY
Experienced software engineer with 8+ years in full-stack development.

EXPERIENCE
Senior Software Engineer | Tech Corp | 2020-Present
- Led development of microservices architecture
- Improved API performance by 60%
- Mentored team of 5 developers

SKILLS
Python, JavaScript, React, Node.js, Docker, AWS
"""

    try:
        preview = generate_text_preview(test_text, max_chars=500)
        if preview:
            print("✅ Text preview generated successfully")
            print(f"   Preview length: {len(preview)} characters")
            print("\n   Preview snippet:")
            print("   " + "-"*50)
            print("   " + preview[:200].replace("\n", "\n   "))
            print("   " + "-"*50)
            return True
        else:
            print("❌ Failed to generate text preview")
            return False
    except Exception as e:
        print(f"❌ Error in text preview: {e}")
        return False


def test_long_text_preview():
    """Test text preview with truncation"""
    print("\n" + "="*60)
    print("Test 3: Text Preview with Truncation")
    print("="*60)

    # Create long text
    long_text = b"A" * 2000  # 2000 characters

    try:
        preview = generate_text_preview(long_text, max_chars=500)
        if preview and len(preview) <= 550:  # 500 + truncation message
            print("✅ Text truncation working correctly")
            print(f"   Original: 2000 chars, Preview: {len(preview)} chars")
            return True
        else:
            print("❌ Text truncation not working")
            return False
    except Exception as e:
        print(f"❌ Error in truncation test: {e}")
        return False


def test_docx_preview():
    """Test DOCX preview generation"""
    print("\n" + "="*60)
    print("Test 4: DOCX Preview Generation")
    print("="*60)

    # Placeholder DOCX content
    docx_content = b"Placeholder DOCX content"

    try:
        preview = generate_docx_preview(docx_content)
        if preview:
            print("✅ DOCX preview generated successfully")
            print(f"   Preview: {preview[:100]}...")
            return True
        else:
            print("❌ Failed to generate DOCX preview")
            return False
    except Exception as e:
        print(f"❌ Error in DOCX preview: {e}")
        return False


def test_with_real_files():
    """Test with real files if available"""
    print("\n" + "="*60)
    print("Test 5: Real Files Test")
    print("="*60)

    test_files_dir = "test_files"

    if os.path.exists(test_files_dir):
        files = os.listdir(test_files_dir)
        print(f"Found {len(files)} test files")

        for filename in files:
            filepath = os.path.join(test_files_dir, filename)
            ext = filename.split('.')[-1].lower()

            print(f"\n   Testing: {filename}")

            try:
                with open(filepath, 'rb') as f:
                    content = f.read()

                if ext == 'pdf':
                    preview = generate_pdf_preview(content)
                    print(f"   ✅ PDF preview: {len(preview) if preview else 0} bytes")
                elif ext == 'txt':
                    preview = generate_text_preview(content)
                    print(f"   ✅ TXT preview: {len(preview) if preview else 0} chars")
                else:
                    print(f"   ⚠️  Skipped {ext} file")

            except Exception as e:
                print(f"   ❌ Error: {e}")

        return True
    else:
        print("   ℹ️  No test_files directory found, skipping real file tests")
        return True


def test_image_resize():
    """Test image resizing functionality"""
    print("\n" + "="*60)
    print("Test 6: Image Resize Functionality")
    print("="*60)

    # Create a simple test image (1x1 pixel PNG)
    simple_png = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'

    try:
        resized = resize_preview_image(simple_png, max_width=100)
        if resized:
            print("✅ Image resize working")
            print(f"   Resized image size: {len(resized)} bytes")
            return True
        else:
            print("❌ Image resize failed")
            return False
    except Exception as e:
        print(f"❌ Error in resize test: {e}")
        return False


def run_all_tests():
    """Run all preview tests"""
    print("\n" + "#"*60)
    print("# Resume Preview Functionality Tests")
    print("#"*60)

    tests = [
        test_pdf_preview,
        test_text_preview,
        test_long_text_preview,
        test_docx_preview,
        test_image_resize,
        test_with_real_files,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            result = test()
            if result:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"\n❌ Test crashed: {test.__name__} - {e}")
            failed += 1

    print("\n" + "="*60)
    print(f"Test Summary: {passed} passed, {failed} failed")
    print("="*60)

    if failed == 0:
        print("\n🎉 All tests passed! Preview feature is ready!")
    else:
        print(f"\n⚠️  {failed} test(s) failed. Please review.")

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
