import json

def detect_sections(text):
    text_lower = text.lower()

    sections = {
        "Education": ["education", "qualification", "academics"],
        "Skills": ["skills", "technical skills", "skills summary"],
        "Projects": ["projects", "project experience"],
        "Experience": ["experience", "work experience", "employment"],
        "Certifications": ["certification", "certifications", "courses"],
        "Achievements": ["achievements", "awards", "honors"],
    }

    missing_sections = []

    for section, keywords in sections.items():
        if not any(keyword in text_lower for keyword in keywords):
            missing_sections.append(section)

    return missing_sections


def get_resume_feedback(text, selected_role):
    text_lower = text.lower()
    suggestions = []

    if "project" not in text.lower():
        suggestions.append("Add a 'Projects' section to highlight your work.")
    if "internship" not in text.lower():
        suggestions.append("Include details of any internships you've completed.")
    if "github" not in text.lower() and "portfolio" not in text.lower():
        suggestions.append("Add your GitHub or portfolio link.")
    if "objective" not in text.lower():
        suggestions.append("Consider adding an objective or summary at the top.")


    # --- Detect Missing Sections ---
    missing_sections = detect_sections(text)
    if missing_sections:
        suggestions.append(
            f"Missing important sections: {', '.join(missing_sections)}."
        )

    # load role keywords
    with open("utils/job_roles.json", "r") as f:
        job_roles = json.load(f)

    role_keywords = job_roles.get(selected_role, [])

    missing_keywords = []
    for keyword in role_keywords:
        if keyword.lower() not in text_lower:
            missing_keywords.append(keyword)

    if missing_keywords:
        suggestions.append(
            f"Missing role-specific keywords for {selected_role}: {', '.join(missing_keywords)}."
        )

    # Calculate resume score
    total_keywords = len(role_keywords)
    matched_keywords = total_keywords - len(missing_keywords)

    keyword_match = int((matched_keywords / total_keywords) * 100) if total_keywords else 100

    # Simple resume score formula
    resume_score = 50
    resume_score += keyword_match * 0.4

    if len(missing_sections) == 0:
        resume_score += 10

    resume_score = min(100, int(resume_score))

    return suggestions, resume_score, keyword_match
