# utils/batch_analyzer.py
import time
from typing import List, Dict
from utils.resume_parser import parse_resume
from utils.analyze_resume import get_resume_feedback


def analyze_single_resume(uploaded_file, selected_role, job_description="", experience_level="Mid Level"):
    """
    Analyzes a single resume file.

    Args:
        uploaded_file: Streamlit UploadedFile object
        selected_role: Target job role for analysis
        job_description: Optional job description for enhanced matching
        experience_level: Experience level (Entry Level, Mid Level, Senior, Executive)

    Returns:
        dict: Analysis results containing filename, parsed text, suggestions, score, etc.
    """
    try:
        # Parse resume
        uploaded_file.seek(0)  # Reset file pointer
        parsed = parse_resume(uploaded_file)
        plain_text = parsed.get("plain_text", "")

        if not plain_text or len(plain_text.strip()) < 50:
            return {
                "filename": uploaded_file.name,
                "status": "error",
                "error": "Failed to extract text from resume",
                "plain_text": "",
                "suggestions": [],
                "score": 0,
                "keyword_match": 0,
                "predicted_role": "Unknown",
                "file_size": uploaded_file.size
            }

        # Analyze resume
        suggestions, resume_score, keyword_match, predicted_role = get_resume_feedback(
            plain_text,
            selected_role,
            job_description=job_description,
            experience_level=experience_level
        )

        return {
            "filename": uploaded_file.name,
            "status": "success",
            "plain_text": plain_text,
            "suggestions": suggestions,
            "score": int(resume_score),
            "keyword_match": int(keyword_match),
            "predicted_role": predicted_role,
            "file_size": uploaded_file.size,
            "word_count": len(plain_text.split())
        }

    except Exception as e:
        return {
            "filename": uploaded_file.name,
            "status": "error",
            "error": str(e),
            "plain_text": "",
            "suggestions": [],
            "score": 0,
            "keyword_match": 0,
            "predicted_role": "Unknown",
            "file_size": uploaded_file.size
        }


def batch_analyze_resumes(
    uploaded_files: List,
    selected_role: str,
    job_description: str = "",
    experience_level: str = "Mid Level",
    progress_callback=None
) -> List[Dict]:
    """
    Analyzes multiple resume files in batch.

    Args:
        uploaded_files: List of Streamlit UploadedFile objects
        selected_role: Target job role for analysis
        job_description: Optional job description for enhanced matching
        experience_level: Experience level (Entry Level, Mid Level, Senior, Executive)
        progress_callback: Optional callback function for progress updates (receives current_index, total)

    Returns:
        list: List of analysis result dictionaries, one per file
    """
    results = []
    total_files = len(uploaded_files)

    for idx, uploaded_file in enumerate(uploaded_files, 1):
        # Call progress callback if provided
        if progress_callback:
            progress_callback(idx, total_files)

        # Analyze single resume
        result = analyze_single_resume(
            uploaded_file,
            selected_role,
            job_description,
            experience_level
        )

        results.append(result)

        # Small delay to prevent overwhelming the system
        if idx < total_files:
            time.sleep(0.1)

    return results


def get_batch_summary(results: List[Dict]) -> Dict:
    """
    Generates summary statistics from batch analysis results.

    Args:
        results: List of analysis result dictionaries

    Returns:
        dict: Summary statistics
    """
    if not results:
        return {
            "total_files": 0,
            "successful": 0,
            "failed": 0,
            "average_score": 0,
            "highest_score": 0,
            "lowest_score": 0,
            "average_keyword_match": 0
        }

    successful_results = [r for r in results if r["status"] == "success"]
    failed_results = [r for r in results if r["status"] == "error"]

    scores = [r["score"] for r in successful_results] if successful_results else [0]
    keyword_matches = [r["keyword_match"] for r in successful_results] if successful_results else [0]

    return {
        "total_files": len(results),
        "successful": len(successful_results),
        "failed": len(failed_results),
        "average_score": sum(scores) / len(scores) if scores else 0,
        "highest_score": max(scores) if scores else 0,
        "lowest_score": min(scores) if scores else 0,
        "average_keyword_match": sum(keyword_matches) / len(keyword_matches) if keyword_matches else 0,
        "best_resume": max(successful_results, key=lambda x: x["score"])["filename"] if successful_results else None,
        "worst_resume": min(successful_results, key=lambda x: x["score"])["filename"] if successful_results else None
    }


def sort_results(results: List[Dict], sort_by: str = "score", ascending: bool = False) -> List[Dict]:
    """
    Sorts batch analysis results by specified criterion.

    Args:
        results: List of analysis result dictionaries
        sort_by: Sort criterion ("score", "keyword_match", "filename", "word_count")
        ascending: Sort in ascending order (default: False for descending)

    Returns:
        list: Sorted list of results
    """
    if not results:
        return []

    valid_keys = ["score", "keyword_match", "filename", "word_count", "file_size"]
    if sort_by not in valid_keys:
        sort_by = "score"

    return sorted(
        results,
        key=lambda x: x.get(sort_by, 0),
        reverse=not ascending
    )
