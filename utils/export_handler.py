# utils/export_handler.py
import pandas as pd
from fpdf import FPDF
from datetime import datetime
import io


def export_to_csv(results: list) -> bytes:
    """
    Exports batch analysis results to CSV format.

    Args:
        results: List of analysis result dictionaries

    Returns:
        bytes: CSV file content as bytes
    """
    if not results:
        return b""

    # Filter successful results
    successful = [r for r in results if r["status"] == "success"]

    if not successful:
        return b""

    # Create DataFrame
    df = pd.DataFrame([
        {
            "Filename": r["filename"],
            "Score": r["score"],
            "Keyword Match (%)": r["keyword_match"],
            "Predicted Role": r["predicted_role"],
            "Word Count": r["word_count"],
            "Issues Found": len(r["suggestions"]),
            "Suggestions": " | ".join(r["suggestions"]),
            "Analysis Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        for r in successful
    ])

    # Convert to CSV bytes
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_bytes = csv_buffer.getvalue().encode('utf-8')

    return csv_bytes


def export_to_pdf(results: list, summary: dict, selected_role: str) -> bytes:
    """
    Exports batch analysis results to PDF format with summary and details.

    Args:
        results: List of analysis result dictionaries
        summary: Dictionary containing batch summary statistics
        selected_role: Target job role for analysis

    Returns:
        bytes: PDF file content as bytes
    """
    if not results:
        return b""

    # Initialize PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 10, "Batch Resume Analysis Report", ln=True, align="C")
    pdf.ln(5)

    # Date and Role
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 6, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.cell(0, 6, f"Target Role: {selected_role}", ln=True)
    pdf.ln(5)

    # Summary Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "Summary Statistics", ln=True)
    pdf.ln(2)

    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 6, f"Total Files Analyzed: {summary['total_files']}", ln=True)
    pdf.cell(0, 6, f"Successful Analyses: {summary['successful']}", ln=True)
    pdf.cell(0, 6, f"Failed Analyses: {summary['failed']}", ln=True)
    pdf.cell(0, 6, f"Average Score: {summary['average_score']:.1f}/100", ln=True)
    pdf.cell(0, 6, f"Highest Score: {summary['highest_score']}/100", ln=True)
    pdf.cell(0, 6, f"Lowest Score: {summary['lowest_score']}/100", ln=True)
    pdf.cell(0, 6, f"Average Keyword Match: {summary['average_keyword_match']:.1f}%", ln=True)

    if summary.get("best_resume"):
        pdf.cell(0, 6, f"Best Resume: {summary['best_resume']}", ln=True)
    if summary.get("worst_resume"):
        pdf.cell(0, 6, f"Needs Improvement: {summary['worst_resume']}", ln=True)

    pdf.ln(8)

    # Detailed Results Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "Detailed Results", ln=True)
    pdf.ln(3)

    successful = [r for r in results if r["status"] == "success"]

    for idx, result in enumerate(successful, 1):
        # Resume header
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 7, f"{idx}. {result['filename']}", ln=True)

        pdf.set_font("Arial", "", 9)
        pdf.cell(0, 5, f"Score: {result['score']}/100 | Keyword Match: {result['keyword_match']}% | Predicted Role: {result['predicted_role']}", ln=True)

        # Suggestions
        if result["suggestions"]:
            pdf.set_font("Arial", "I", 9)
            pdf.cell(0, 5, "Suggestions:", ln=True)
            pdf.set_font("Arial", "", 8)

            for suggestion in result["suggestions"][:5]:  # Limit to 5 suggestions
                # Clean text for PDF
                clean_suggestion = suggestion.encode('latin-1', 'replace').decode('latin-1')
                pdf.multi_cell(0, 4, f"  - {clean_suggestion}")

        else:
            pdf.set_font("Arial", "", 9)
            pdf.cell(0, 5, "No major issues found!", ln=True)

        pdf.ln(4)

        # Add page break if needed
        if pdf.get_y() > 250:
            pdf.add_page()

    # Failed analyses (if any)
    failed = [r for r in results if r["status"] == "error"]
    if failed:
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 8, "Failed Analyses", ln=True)
        pdf.ln(3)

        pdf.set_font("Arial", "", 9)
        for fail in failed:
            pdf.cell(0, 6, f"- {fail['filename']}: {fail.get('error', 'Unknown error')}", ln=True)

    # Get PDF bytes
    pdf_bytes = pdf.output(dest='S').encode('latin-1')

    return pdf_bytes


def get_export_filename(format: str = "csv") -> str:
    """
    Generates a timestamped filename for export.

    Args:
        format: File format ("csv" or "pdf")

    Returns:
        str: Filename with timestamp
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"batch_analysis_{timestamp}.{format}"
