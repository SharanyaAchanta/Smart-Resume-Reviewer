import streamlit as st
import language_tool_python

def get_grammar_suggestions(resume_text, max_errors=5):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(resume_text)

    grammar_suggestions = []
    for match in matches[:max_errors]:
        grammar_suggestions.append(
            f"Grammar issue: {match.message}. "
            f"Suggestion: {', '.join(match.replacements)}"
        )

    return grammar_suggestions


def show_suggestions(suggestions, resume_score, keyword_match, resume_text=None):
    st.markdown("## ⭐ Resume Review Summary")

    # Resume Score Bar
    st.progress(resume_score / 100)
    st.write(f"**Resume Score:** {resume_score}/100")

    # Keyword Match
    st.write(f"**Keyword Match:** {keyword_match}%")

    st.markdown("## 🔍 Suggestions")

    if resume_text:
        grammar_suggestions = get_grammar_suggestions(resume_text)
        suggestions = suggestions + grammar_suggestions

    for s in suggestions:
        # RED for missing sections
        if "Missing important sections" in s:
            st.markdown(
                f"""
                <div class='fade-in' style='background-color:#ff4d4d;padding:12px;border-radius:8px;color:white;margin-bottom:10px;'>
                    {s}
                </div>
                """,
                unsafe_allow_html=True
            )

        elif "Grammar issue:" in s:
            st.markdown(
                f"""
                <div style='background-color:#4da6ff;padding:12px;
                            border-radius:8px;color:white;margin-bottom:10px;'>
                    {s}
                </div>
                """,
                unsafe_allow_html=True
            )

        # YELLOW for general suggestions
        elif "Missing role-specific keywords" in s:
            st.markdown(
                f"""
                <div style='background-color:#ffcc00;padding:12px;border-radius:8px;color:black;margin-bottom:10px;'>
                    {s}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            st.markdown(
                f"""
                <div style='background-color:#bfbf4d;padding:12px;border-radius:8px;color:black;margin-bottom:10px;'>
                    {s}
                </div>
                """,
                unsafe_allow_html=True
            )


