# test_batch_upload.py
"""
Test suite for batch upload functionality.
Tests batch upload validation, batch analysis, and export features.
"""

import sys
import io
from unittest.mock import Mock


class MockUploadedFile:
    """Mock Streamlit UploadedFile for testing"""

    def __init__(self, name, size, content=b"Sample content"):
        self.name = name
        self.size = size
        self._content = content
        self._position = 0

    def read(self):
        return self._content

    def seek(self, position):
        self._position = position


def test_batch_validation():
    """Test batch upload file validation"""
    from components.batch_upload import validate_batch_files, MIN_BATCH_FILES, MAX_BATCH_FILES, MAX_FILE_SIZE_BYTES

    print("Test 1: Valid batch upload (3 files)")
    files = [
        MockUploadedFile("resume1.pdf", 1024 * 100),  # 100 KB
        MockUploadedFile("resume2.pdf", 1024 * 200),  # 200 KB
        MockUploadedFile("resume3.docx", 1024 * 150),  # 150 KB
    ]
    is_valid, error, valid_files = validate_batch_files(files)
    assert is_valid == True, "Should accept 3 valid files"
    assert len(valid_files) == 3, "Should return 3 valid files"
    print("✅ Passed")

    print("\nTest 2: Too few files (1 file)")
    files = [MockUploadedFile("resume1.pdf", 1024 * 100)]
    is_valid, error, valid_files = validate_batch_files(files)
    assert is_valid == False, "Should reject < 2 files"
    assert "at least" in error.lower(), "Error message should mention minimum"
    print("✅ Passed")

    print("\nTest 3: Too many files (11 files)")
    files = [MockUploadedFile(f"resume{i}.pdf", 1024 * 100) for i in range(11)]
    is_valid, error, valid_files = validate_batch_files(files)
    assert is_valid == False, "Should reject > 10 files"
    assert "maximum" in error.lower(), "Error message should mention maximum"
    print("✅ Passed")

    print("\nTest 4: File too large")
    files = [
        MockUploadedFile("resume1.pdf", 1024 * 100),
        MockUploadedFile("resume2.pdf", MAX_FILE_SIZE_BYTES + 1),  # Over limit
    ]
    is_valid, error, valid_files = validate_batch_files(files)
    assert "exceeds" in error.lower(), "Error message should mention size limit"
    print("✅ Passed")

    print("\nTest 5: Invalid file type")
    files = [
        MockUploadedFile("resume1.pdf", 1024 * 100),
        MockUploadedFile("resume2.exe", 1024 * 100),  # Invalid type
    ]
    is_valid, error, valid_files = validate_batch_files(files)
    assert "invalid type" in error.lower(), "Error message should mention invalid type"
    print("✅ Passed")

    print("\nTest 6: Mixed valid/invalid files")
    files = [
        MockUploadedFile("resume1.pdf", 1024 * 100),  # Valid
        MockUploadedFile("resume2.exe", 1024 * 100),  # Invalid type
        MockUploadedFile("resume3.txt", 1024 * 50),   # Valid
    ]
    is_valid, error, valid_files = validate_batch_files(files)
    assert len(valid_files) == 2, "Should return only valid files"
    assert is_valid == True, "Should be valid if at least 2 files are valid"
    print("✅ Passed")


def test_batch_analyzer():
    """Test batch resume analysis"""
    from utils.batch_analyzer import get_batch_summary, sort_results

    print("\nTest 7: Batch summary calculation")
    results = [
        {"filename": "r1.pdf", "status": "success", "score": 75, "keyword_match": 80, "word_count": 500},
        {"filename": "r2.pdf", "status": "success", "score": 85, "keyword_match": 90, "word_count": 600},
        {"filename": "r3.pdf", "status": "error", "score": 0, "keyword_match": 0, "word_count": 0},
    ]

    summary = get_batch_summary(results)
    assert summary["total_files"] == 3, "Should count all files"
    assert summary["successful"] == 2, "Should count successful analyses"
    assert summary["failed"] == 1, "Should count failed analyses"
    assert summary["average_score"] == 80, "Should calculate correct average"
    assert summary["highest_score"] == 85, "Should identify highest score"
    assert summary["lowest_score"] == 75, "Should identify lowest score"
    print("✅ Passed")

    print("\nTest 8: Sorting results")
    sorted_by_score = sort_results(results, sort_by="score", ascending=False)
    assert sorted_by_score[0]["score"] >= sorted_by_score[1]["score"], "Should sort by score descending"

    sorted_by_filename = sort_results(results, sort_by="filename", ascending=True)
    assert sorted_by_filename[0]["filename"] <= sorted_by_filename[1]["filename"], "Should sort by filename ascending"
    print("✅ Passed")


def test_export():
    """Test export functionality"""
    from utils.export_handler import export_to_csv, get_export_filename
    import pandas as pd

    print("\nTest 9: CSV export")
    results = [
        {
            "filename": "resume1.pdf",
            "status": "success",
            "score": 75,
            "keyword_match": 80,
            "predicted_role": "Software Engineer",
            "word_count": 500,
            "suggestions": ["Add projects", "Include skills"]
        },
        {
            "filename": "resume2.pdf",
            "status": "success",
            "score": 85,
            "keyword_match": 90,
            "predicted_role": "Data Scientist",
            "word_count": 600,
            "suggestions": ["Add certifications"]
        },
    ]

    csv_data = export_to_csv(results)
    assert len(csv_data) > 0, "Should generate CSV data"
    assert b"Filename" in csv_data, "CSV should have header"
    assert b"resume1.pdf" in csv_data, "CSV should contain data"
    print("✅ Passed")

    print("\nTest 10: Export filename generation")
    filename = get_export_filename("csv")
    assert filename.endswith(".csv"), "Should have .csv extension"
    assert "batch_analysis_" in filename, "Should have correct prefix"
    print("✅ Passed")


def run_all_tests():
    """Run all test functions"""
    print("=" * 60)
    print("BATCH UPLOAD FEATURE TEST SUITE")
    print("=" * 60)

    try:
        test_batch_validation()
        test_batch_analyzer()
        test_export()

        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED (10/10)")
        print("=" * 60)
        return True

    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
