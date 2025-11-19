import json

def get_resume_feedback(text, selected_role):
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
    

    text_lower = text.lower()

    # load role keywords
    with open("utils/job_roles.json", "r") as f:
        job_roles = json.load(f)

    role_keywords = job_roles.get(selected_role, [])

    missing_keywords = []
    for keyword in role_keywords:
        if keyword.lower() not in text_lower:
            missing_keywords.append(keyword)

    feedback = []

    if missing_keywords:
        feedback.append(
            {
                "title": f"Missing Keywords for {selected_role}",
                "details": f"Consider adding these keywords to strengthen your resume: {', '.join(missing_keywords)}"
            }
        )
    else:
        feedback.append(
            {
                "title": "Great Work!",
                "details": "Your resume already contains most of the important keywords!"
            }
        )

    return feedback
