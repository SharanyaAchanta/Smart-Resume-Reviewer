import streamlit as st
from components.header import show_sidebar_navbar, show_header



def main():
   
    # Custom CSS
    st.markdown("""
    <style>
    .resume-tip-card {
        background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(236, 72, 153, 0.3);
    }
    .tip-level {
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
    }
    .tip-item {
        background: rgba(255,255,255,0.1);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    .tip-icon {
        font-size: 2rem;
        margin-right: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
    <div style='text-align: center; padding: 3rem 0;'>
        <h1 style='color: #EC4899; font-size: 3rem;'>📝 Resume Tips by Experience Level</h1>
        <p style='color: #666; font-size: 1.2rem; max-width: 600px; margin: 0 auto;'>
            Tailored advice for every career stage - from Freshers to Senior Professionals
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Experience Level Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🎓 Fresher/Entry-Level",
        "🧑‍💼 Junior (0-2 yrs)",
        "👨‍💼 Mid-Level (3-5 yrs)",
        "👴 Senior (5+ yrs)"
    ])

    # Fresher Tips
    with tab1:
        st.markdown("""
        <div class="resume-tip-card">
            <h2 class="tip-level">🎓 Fresher/Entry-Level Tips</h2>
            <div class="tip-item">
                <span class="tip-icon">📚</span>
                <strong>Highlight Projects & Internships:</strong> Your college projects, hackathons, and internships are your experience. 
                Quantify results instead of writing generic lines.
            </div>
            <div class="tip-item">
                <span class="tip-icon">⭐</span>
                <strong>Skills Section First:</strong> Put technical skills (Python, React, AWS) at the top. 
                Recruiters scan for keywords in the first few seconds.
            </div>
            <div class="tip-item">
                <span class="tip-icon">📈</span>
                <strong>Quantify Achievements:</strong> Use numbers to show impact wherever possible.
            </div>
            <div class="tip-item">
                <span class="tip-icon">🎯</span>
                <strong>1-Page Resume:</strong> Keep it concise and focused on relevant projects and skills.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Junior Tips
    with tab2:
        st.markdown("""
        <div class="resume-tip-card">
            <h2 class="tip-level">🧑‍💼 Junior (0-2 Years Experience)</h2>
            <div class="tip-item">
                <span class="tip-icon">🚀</span>
                <strong>Show Impact:</strong> Describe how your work improved performance, UX, or processes.
            </div>
            <div class="tip-item">
                <span class="tip-icon">🔧</span>
                <strong>Tech Stack Progression:</strong> Highlight how your skills and tools evolved over time.
            </div>
            <div class="tip-item">
                <span class="tip-icon">🤝</span>
                <strong>Team Contributions:</strong> Mention cross-team work, code reviews, and collaboration.
            </div>
            <div class="tip-item">
                <span class="tip-icon">📊</span>
                <strong>Metrics Matter:</strong> Use measurable outcomes like response time, error rate, or users.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Mid-Level Tips
    with tab3:
        st.markdown("""
        <div class="resume-tip-card">
            <h2 class="tip-level">👨‍💼 Mid-Level (3-5 Years Experience)</h2>
            <div class="tip-item">
                <span class="tip-icon">🏗️</span>
                <strong>Architecture Decisions:</strong> Mention system design, patterns, and scalability decisions.
            </div>
            <div class="tip-item">
                <span class="tip-icon">👥</span>
                <strong>Leadership:</strong> Include mentoring, leading features, or owning modules.
            </div>
            <div class="tip-item">
                <span class="tip-icon">⚡</span>
                <strong>Optimization:</strong> Talk about performance, cost, and reliability improvements.
            </div>
            <div class="tip-item">
                <span class="tip-icon">📈</span>
                <strong>Business Impact:</strong> Connect your work to product KPIs or business goals.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Senior Tips
    with tab4:
        st.markdown("""
        <div class="resume-tip-card">
            <h2 class="tip-level">👴 Senior (5+ Years Experience)</h2>
            <div class="tip-item">
                <span class="tip-icon">🎯</span>
                <strong>Strategic Impact:</strong> Highlight long-term technical direction and major initiatives.
            </div>
            <div class="tip-item">
                <span class="tip-icon">🏢</span>
                <strong>Team Leadership:</strong> Describe team building, ownership, and delivery at scale.
            </div>
            <div class="tip-item">
                <span class="tip-icon">💰</span>
                <strong>Business Results:</strong> Show cost savings, revenue impact, or major growth outcomes.
            </div>
            <div class="tip-item">
                <span class="tip-icon">🔮</span>
                <strong>Future Vision:</strong> Mention roadmaps, tech strategy, and cross-org influence.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Contribution Call
    st.markdown("""
    <div style='text-align: center; padding: 3rem; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                border-radius: 20px; margin: 3rem 0; color: white;'>
        <h2 style='margin-bottom: 1rem;'>🚀 Want to Contribute More Tips?</h2>
        <p style='font-size: 1.1rem; margin-bottom: 2rem;'>
            Add tips for new roles, industries, or experience levels!
        </p>
        <a href='https://github.com/SharanyaAchanta/Smart-Resume-Reviewer/issues/new?template=feature_request.md' 
           target='_blank' 
           style='background: white; color: #f5576c; padding: 1rem 2rem; 
                  border-radius: 50px; text-decoration: none; 
                  font-weight: 600; font-size: 1.1rem; 
                  box-shadow: 0 10px 30px rgba(0,0,0,0.2);'>
            💡 Suggest New Tips → 
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #666; font-size: 0.9rem;'>💡 Tips curated from hiring managers & ATS insights</p>",
        unsafe_allow_html=True,
    )
