# Testing Checklist - File Upload Validation

## Automated Tests ✅
```bash
python3 test_validation.py
```
**Result**: All 8 tests passed ✅

---

## Manual Testing in Browser

### Setup
1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Open browser: `http://localhost:8501`

---

## Test Cases

### ✅ Test 1: Valid PDF File (Small)
- **File**: `test_files/small_resume.pdf` (100 KB)
- **Expected Result**:
  - File uploads successfully
  - Green success message: "✅ File received (0.10 MB) — processing..."
  - Resume analysis proceeds normally
- **Status**: [ ] Pass [ ] Fail

---

### ✅ Test 2: Valid TXT File
- **File**: `test_files/sample_resume.txt` (750 bytes)
- **Expected Result**:
  - File uploads successfully
  - Green success message: "✅ File received (0.00 MB) — processing..."
  - Text content is parsed correctly
- **Status**: [ ] Pass [ ] Fail

---

### ✅ Test 3: Valid DOCX File
- **File**: Create or use existing DOCX resume
- **Expected Result**:
  - File uploads successfully
  - Green success message with file size
  - Resume analysis proceeds normally
- **Status**: [ ] Pass [ ] Fail

---

### ❌ Test 4: File Too Large (>5MB)
- **File**: `test_files/large_file.pdf` (6 MB)
- **Expected Result**:
  - Red error message: "❌ File size (6.00 MB) exceeds the maximum limit of 5 MB. Please upload a smaller file."
  - File is NOT processed
  - No resume analysis occurs
- **Status**: [ ] Pass [ ] Fail

---

### ❌ Test 5: Invalid File Type
- **File**: `test_files/invalid_file.exe`
- **Expected Result**:
  - Red error message: "❌ Invalid file type '.exe'. Only PDF, DOCX, TXT files are allowed."
  - File is NOT processed
- **Status**: [ ] Pass [ ] Fail

---

### ❌ Test 6: File Without Extension
- **File**: Create file without extension: `resume` (no .pdf, .txt, etc.)
- **Expected Result**:
  - Red error message about invalid file type
  - File is NOT processed
- **Status**: [ ] Pass [ ] Fail

---

### ✅ Test 7: Boundary Case (Exactly 5MB)
- **File**: Create exactly 5MB file
  ```bash
  dd if=/dev/zero of=test_files/exactly_5mb.pdf bs=1M count=5
  ```
- **Expected Result**:
  - File uploads successfully
  - Success message shown
- **Status**: [ ] Pass [ ] Fail

---

### ✅ Test 8: Multiple Uploads
- **Test**: Upload valid file → Upload invalid file → Upload valid file again
- **Expected Result**:
  - First valid file: Success
  - Invalid file: Error message
  - Second valid file: Success again
- **Status**: [ ] Pass [ ] Fail

---

### ✅ Test 9: Landing Page Upload
- **Location**: Main landing page (if applicable)
- **Test**: Upload file from landing page, then navigate to Analyzer
- **Expected Result**:
  - File persists across page navigation
  - Validation applies on landing page too
- **Status**: [ ] Pass [ ] Fail

---

### ✅ Test 10: Fallback Uploader on Analyzer Page
- **Location**: Resume Analyzer page
- **Test**: Upload file directly on Analyzer page (not from landing page)
- **Expected Result**:
  - Same validation applies
  - Error messages display correctly
- **Status**: [ ] Pass [ ] Fail

---

## UI/UX Checks

### Visual Elements
- [ ] Success message is green with ✅ emoji
- [ ] Error message is red with ❌ emoji
- [ ] Info message is blue with ℹ️ emoji
- [ ] File size is displayed in MB with 2 decimal places
- [ ] Instruction text mentions "PDF, DOCX, or TXT"
- [ ] Instruction text mentions "max 5 MB"

### User Experience
- [ ] Error messages are clear and actionable
- [ ] No console errors in browser DevTools
- [ ] Validation is instant (no delay)
- [ ] File size calculation is accurate
- [ ] Valid files process without issues

---

## Edge Cases

### Edge Case 1: Very Small File
- **File**: 1 byte text file
- **Expected**: Uploads successfully (but may not have enough content to analyze)
- **Status**: [ ] Pass [ ] Fail

### Edge Case 2: File Name with Special Characters
- **File**: `resume @#$%.pdf`
- **Expected**: File type validation works correctly
- **Status**: [ ] Pass [ ] Fail

### Edge Case 3: File Name with Multiple Dots
- **File**: `my.resume.v2.pdf`
- **Expected**: Correctly identifies `.pdf` extension
- **Status**: [ ] Pass [ ] Fail

### Edge Case 4: Uppercase Extension
- **File**: `resume.PDF` or `resume.DOCX`
- **Expected**: Uploads successfully (case-insensitive check)
- **Status**: [ ] Pass [ ] Fail

---

## Performance Tests

### Test 1: Large Valid File (~4.9MB)
- **Expected**: Uploads without timeout
- **Status**: [ ] Pass [ ] Fail

### Test 2: Rapid Multiple Uploads
- **Test**: Upload several files quickly one after another
- **Expected**: Validation works correctly for each
- **Status**: [ ] Pass [ ] Fail

---

## Cross-Component Testing

### Landing Page → Analyzer Transition
1. Upload valid file on landing page
2. Navigate to Analyzer
3. **Expected**: File persists and validation was applied
- **Status**: [ ] Pass [ ] Fail

### Direct Analyzer Upload
1. Go directly to Analyzer page
2. Upload file using fallback uploader
3. **Expected**: Same validation as landing page
- **Status**: [ ] Pass [ ] Fail

---

## Regression Testing

### Existing Functionality
- [ ] PDF parsing still works
- [ ] DOCX parsing still works
- [ ] Resume analysis produces correct results
- [ ] Resume scoring works
- [ ] Download functionality works
- [ ] Review history saves correctly
- [ ] Resume builder still functional

---

## Test Files Location
All test files are in: `test_files/`

### Create Additional Test Files (if needed):
```bash
# Create 4.9MB file (valid)
dd if=/dev/zero of=test_files/valid_large.pdf bs=1M count=4.9

# Create exactly 5MB file (boundary)
dd if=/dev/zero of=test_files/exactly_5mb.pdf bs=1M count=5

# Create 5.1MB file (invalid)
dd if=/dev/zero of=test_files/slightly_over.pdf bs=1M count=5.1
```

---

## Browser Compatibility Testing
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

---

## Mobile Testing (if applicable)
- [ ] Mobile browser upload works
- [ ] Error messages display correctly on mobile
- [ ] Touch interactions work

---

## Notes
- Keep browser DevTools console open during testing
- Check for any JavaScript errors
- Verify network requests if needed
- Test with real resume files for best results

---

## Final Checklist
- [ ] All automated tests pass (8/8)
- [ ] All manual test cases pass
- [ ] No console errors
- [ ] UI looks correct
- [ ] Error messages are helpful
- [ ] Valid files process correctly
- [ ] Invalid files are rejected appropriately

---

**Tested By**: _______________
**Date**: _______________
**All Tests Passed**: [ ] Yes [ ] No
