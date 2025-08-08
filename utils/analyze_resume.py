def get_resume_feedback(text):
    suggestions = []

    if "project" not in text.lower():
        suggestions.append("Add a 'Projects' section to highlight your work.")
    if "internship" not in text.lower():
        suggestions.append("Include details of any internships you've completed.")
    if "github" not in text.lower() and "portfolio" not in text.lower():
        suggestions.append("Add your GitHub or portfolio link.")
    if "objective" not in text.lower():
        suggestions.append("Consider adding an objective or summary at the top.")

    if not suggestions:
        suggestions.append("Great resume! No major issues found.")

    return suggestions
