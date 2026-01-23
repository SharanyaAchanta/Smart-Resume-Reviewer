"""
Test script for file upload validation
Tests file size and file type validation logic
"""

from components.upload_card import validate_uploaded_file, MAX_FILE_SIZE_BYTES, ALLOWED_FILE_TYPES
from io import BytesIO


class MockUploadedFile:
    """Mock Streamlit uploaded file for testing"""

    def __init__(self, name, size, content=b"test content"):
        self.name = name
        self.size = size
        self.content = content

    def read(self):
        return self.content

    def seek(self, position):
        pass


def test_valid_pdf():
    """Test valid PDF file"""
    mock_file = MockUploadedFile("resume.pdf", 1024 * 1024)  # 1MB
    is_valid, error = validate_uploaded_file(mock_file)
    assert is_valid, f"Expected valid PDF to pass, but got error: {error}"
    print("✅ Test passed: Valid PDF file")


def test_valid_docx():
    """Test valid DOCX file"""
    mock_file = MockUploadedFile("resume.docx", 2 * 1024 * 1024)  # 2MB
    is_valid, error = validate_uploaded_file(mock_file)
    assert is_valid, f"Expected valid DOCX to pass, but got error: {error}"
    print("✅ Test passed: Valid DOCX file")


def test_valid_txt():
    """Test valid TXT file"""
    mock_file = MockUploadedFile("resume.txt", 500 * 1024)  # 500KB
    is_valid, error = validate_uploaded_file(mock_file)
    assert is_valid, f"Expected valid TXT to pass, but got error: {error}"
    print("✅ Test passed: Valid TXT file")


def test_file_too_large():
    """Test file exceeding size limit"""
    mock_file = MockUploadedFile("resume.pdf", MAX_FILE_SIZE_BYTES + 1)  # Over 5MB
    is_valid, error = validate_uploaded_file(mock_file)
    assert not is_valid, "Expected file size validation to fail"
    assert "exceeds the maximum limit" in error, f"Expected size error message, got: {error}"
    print("✅ Test passed: File too large rejected")


def test_invalid_file_type():
    """Test invalid file type"""
    mock_file = MockUploadedFile("resume.exe", 1024)
    is_valid, error = validate_uploaded_file(mock_file)
    assert not is_valid, "Expected file type validation to fail"
    assert "Invalid file type" in error, f"Expected file type error message, got: {error}"
    print("✅ Test passed: Invalid file type rejected")


def test_no_extension():
    """Test file with no extension"""
    mock_file = MockUploadedFile("resume", 1024)
    is_valid, error = validate_uploaded_file(mock_file)
    assert not is_valid, "Expected file with no extension to fail"
    print("✅ Test passed: File with no extension rejected")


def test_none_file():
    """Test None file (no upload)"""
    is_valid, error = validate_uploaded_file(None)
    assert is_valid, "Expected None file to be valid (no upload yet)"
    assert error is None, "Expected no error for None file"
    print("✅ Test passed: None file handled correctly")


def test_boundary_file_size():
    """Test file at exact size limit"""
    mock_file = MockUploadedFile("resume.pdf", MAX_FILE_SIZE_BYTES)
    is_valid, error = validate_uploaded_file(mock_file)
    assert is_valid, f"Expected file at exact size limit to pass, but got error: {error}"
    print("✅ Test passed: File at exact size limit accepted")


def run_all_tests():
    """Run all validation tests"""
    print("\n" + "=" * 50)
    print("Running File Upload Validation Tests")
    print("=" * 50 + "\n")

    tests = [
        test_valid_pdf,
        test_valid_docx,
        test_valid_txt,
        test_file_too_large,
        test_invalid_file_type,
        test_no_extension,
        test_none_file,
        test_boundary_file_size,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"❌ Test failed: {test.__name__} - {e}")
            failed += 1
        except Exception as e:
            print(f"❌ Test error: {test.__name__} - {e}")
            failed += 1

    print("\n" + "=" * 50)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 50 + "\n")

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
