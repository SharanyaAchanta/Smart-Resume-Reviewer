# components/contributors.py
import streamlit as st
import streamlit.components.v1 as components


def show_contributors_page():
    """Full-screen contributors dashboard embedded in Streamlit."""

    # Optional: ensure wide layout when opened directly via this page
    st.set_page_config(page_title="Contributors - Smart Resume Reviewer",
                       page_icon="👥", layout="wide")

    # Main container (Streamlit)
    st.markdown(
        "<div style='margin-top: 1rem;'></div>",
        unsafe_allow_html=True,
    )

    # NOTE: This is your HTML+CSS+JS dashboard, slightly adapted:
    # - Repo owner/name changed to SharanyaAchanta / Smart-Resume-Reviewer
    # - All assets (CSS/JS) kept inline so it works inside Streamlit iframe

    contributors_html = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Contributors | Smart Resume Reviewer</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />

<style>
/* === CSS from your contributors page === */

/* Contributors Page Styles */

:root {
  --primary: #ff6347;
  --primary-dark: #ff4500;
  --dark: #2b2b2b;
  --dark-light: #333;
  --text: #ffffff;
  --text-light: #cccccc;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  background-color: var(--dark);
  color: var(--text);
  line-height: 1.6;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.main-content {
  margin-top: 40px;
}

/* Hero Section */
.contributors-hero {
  padding: 3rem 0 2rem 0;
  text-align: center;
  background: linear-gradient(135deg, var(--dark) 0%, var(--dark-light) 100%);
}

.contributors-hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.contributors-hero p {
  font-size: 1.1rem;
  color: var(--text-light);
  max-width: 600px;
  margin: 0 auto;
}

/* Search and Filters */
.search-contributor {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
  gap: 1rem;
  flex-wrap: wrap;
}

/* Loading Spinner */
#spinner {
  display: none;
  justify-content: center;
  align-items: center;
  height: 100px;
}

.spinner-circle {
  border: 5px solid #ccc;
  border-top: 5px solid var(--primary);
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

/* Footer */
.footer {
  background: var(--dark-light);
  padding: 3rem 0;
  text-align: center;
  border-top: 3px solid var(--primary);
}

.footer p { color: var(--text-light); }

.contributor-container h1 {
  text-align: center;
  background: linear-gradient(90deg, var(--primary), var(--text), var(--primary-dark));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  background-size: 300%;
  animation: flow 6s linear infinite;
  margin-bottom: 25px;
}

@keyframes flow { to { background-position: 300%; } }

/* --- STATS GRID (6 Columns) --- */
#stats {
  display: grid;
  grid-template-columns: repeat(6, 1fr); 
  gap: 15px;
  margin-bottom: 40px;
  width: 100%;
  overflow-x: auto;
  padding-bottom: 10px; 
}

/* Hide scrollbar for cleaner look */
#stats::-webkit-scrollbar { height: 6px; }
#stats::-webkit-scrollbar-thumb { background: var(--primary-dark); border-radius: 3px; }

.stat-box {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 14px;
  padding: 15px 5px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  transition: transform 0.25s ease, background 0.3s, border-color 0.3s;
  text-align: center;
  min-width: 120px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* Hover Colors for Stats */
.stat-box:nth-child(1):hover { border-color: #4a90e2; box-shadow: 0 0 15px rgba(74, 144, 226, 0.4); }
.stat-box:nth-child(2):hover { border-color: #2ecc71; box-shadow: 0 0 15px rgba(46, 204, 113, 0.4); }
.stat-box:nth-child(3):hover { border-color: #9b59b6; box-shadow: 0 0 15px rgba(155, 89, 182, 0.4); }
.stat-box:nth-child(4):hover { border-color: #f1c40f; box-shadow: 0 0 15px rgba(241, 196, 15, 0.4); }
.stat-box:nth-child(5):hover { border-color: #e67e22; box-shadow: 0 0 15px rgba(230, 126, 34, 0.4); }
.stat-box:nth-child(6):hover { border-color: #e74c3c; box-shadow: 0 0 15px rgba(231, 76, 60, 0.4); }

.stat-box:hover { transform: translateY(-4px); }

.stat-box h3 {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #aaa;
  margin-bottom: 5px;
  white-space: nowrap;
}

.stat-box p {
  font-size: 1.5rem;
  color: #fff;
  font-weight: 700;
  margin: 0;
  text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}

/* Controls */
#controls {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 15px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

#searchInput, .filter-select {
  padding: 10px 16px;
  border-radius: 10px;
  border: 1px solid rgba(247, 57, 9, 0.5);
  background: rgba(252, 58, 10, 0.05);
  color: #fff !important;
  transition: all 0.3s;
}

/* --- FIX FOR DROPDOWN OPTION VISIBILITY --- */
.filter-select option {
  background-color: #2b2b2b;
  color: #ffffff;
  padding: 10px;
}

#searchInput { width: 250px; }
.filter-select { cursor: pointer; }

#searchInput:focus, .filter-select:focus {
  border-color: var(--primary);
  outline: none;
  box-shadow: 0 0 8px var(--primary-dark);
}

button {
  background: #ff5321;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 8px 14px;
  cursor: pointer;
  font-weight: 500;
  transition: background 0.2s;
}

button:hover { background: #0056b3; }

/* Contributors List */
#contributorsList {
  max-width: 80%;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 20px;
  margin: 2rem auto;
}

/* Contributor Cards & Splatter Effect */
.contributor {
  background: #222;
  border: 1px solid #333;
  border-radius: 15px;
  padding: 20px;
  text-align: center;
  cursor: pointer;
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.27);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.contributor::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  background: radial-gradient(circle, rgba(255, 99, 71, 0.2) 0%, rgba(255, 99, 71, 0) 70%);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  transition: width 0.4s ease, height 0.4s ease;
  z-index: -1;
}

.contributor:hover::before {
  width: 300px;
  height: 300px;
}

.contributor:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.4);
  border-color: var(--primary);
}

.contributor img {
  border-radius: 50%;
  width: 80px;
  height: 80px;
  object-fit: cover;
  border: 3px solid rgba(255,255,255,0.1);
  transition: border-color 0.3s;
}

.contributor:hover img {
  border-color: var(--primary);
}

.contributor .cont-name {
  display: block;
  color: white;
  font-weight: bold;
  font-size: 1.1rem;
  text-decoration: none;
}

.contributor-stats {
  font-size: 0.9rem;
  color: #ccc;
  margin-top: 5px;
  background: rgba(0,0,0,0.2);
  padding: 5px 10px;
  border-radius: 20px;
}

/* Tier Styles */
.tier-gold { border: 2px solid #FFD700; background: linear-gradient(145deg, rgba(255, 215, 0, 0.05), #1a1a1a); }
.tier-silver { border: 2px solid #C0C0C0; background: linear-gradient(145deg, rgba(192, 192, 192, 0.05), #1a1a1a); }
.tier-bronze { border: 2px solid #CD7F32; background: linear-gradient(145deg, rgba(205, 127, 50, 0.05), #1a1a1a); }
.tier-contributor { border: 1px solid #444; }

.badge-gold { color: #FFD700; text-shadow: 0 0 10px rgba(255, 215, 0, 0.3); }
.badge-silver { color: #C0C0C0; text-shadow: 0 0 10px rgba(192, 192, 192, 0.3); }
.badge-bronze { color: #CD7F32; text-shadow: 0 0 10px rgba(205, 127, 50, 0.3); }
.badge-contributor { color: #4a90e2; }

/* Modal Styles */
.contributor-modal {
  display: none;
  position: fixed;
  z-index: 10000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(5px);
  overflow-y: auto;
  justify-content: center;
  align-items: center;
}

.contributor-modal.active { display: flex; }

.modal-content {
  background: linear-gradient(135deg, var(--dark), var(--dark-light));
  padding: 30px;
  border-radius: 20px;
  width: 90%;
  max-width: 500px;
  box-shadow: 0 10px 50px rgba(255, 99, 71, 0.3);
  border: 1px solid rgba(255, 99, 71, 0.2);
  animation: modalSlideIn 0.3s ease-out;
  text-align: center;
}

@keyframes modalSlideIn {
  from { transform: translateY(30px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

.modal-close {
  color: var(--text-light);
  float: right;
  font-size: 35px;
  font-weight: bold;
  cursor: pointer;
  transition: color 0.3s;
  line-height: 20px;
}

.modal-close:hover { color: var(--primary); }

.modal-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.modal-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 3px solid var(--primary);
  margin-bottom: 10px;
}

.modal-info h2 { margin: 0; color: var(--primary); font-size: 1.5rem; }
.modal-subtitle { color: var(--text-light); font-size: 0.9rem; margin: 5px 0; }

.modal-stats {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
  margin-bottom: 25px;
}

.modal-stat {
  text-align: center;
  padding: 15px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.modal-stat i {
  font-size: 1.5rem;
  color: var(--primary);
  margin-bottom: 8px;
  display: block;
}

.modal-stat span { display: block; font-size: 1.4rem; font-weight: bold; color: var(--text); }
.modal-stat p { color: var(--text-light); font-size: 0.85rem; margin: 0; }

.modal-actions {
    display: flex;
    gap: 15px;
    justify-content: center;
    margin-top: 20px;
    flex-wrap: wrap;
}

.modal-btn {
    padding: 10px 20px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: transform 0.2s;
}

.modal-btn:hover { transform: translateY(-2px); }
.modal-btn.primary { background: var(--primary); color: white; }
.modal-btn.secondary { border: 1px solid #ccc; color: white; }

.special-lead {
  background: linear-gradient(135deg, #b5722f, #5c6515);
  color: #222;
  border: 2px solid gold;
  box-shadow: 0 0 25px rgba(255, 215, 0, 0.5);
  transform: scale(1.05);
}

/* Timeline */
.timeline-container {
  max-width: 100%;
  margin: 3rem auto 0;
  padding: 20px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
}

.timeline-container h2 {
  text-align: center;
  margin-bottom: 20px;
  color: var(--primary);
  font-size: 1.8rem;
}

.timeline-content {
  max-height: 350px;
  overflow-y: auto;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.timeline-content::-webkit-scrollbar { width: 6px; }
.timeline-content::-webkit-scrollbar-thumb { background: var(--primary-dark); border-radius: 3px; }
.timeline-content::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.05); }

.timeline-item {
  display: flex;
  align-items: flex-start;
  gap: 15px;
  padding: 15px;
  background: rgba(255, 255, 255, 0.05);
  border-left: 4px solid var(--primary);
  border-radius: 8px;
  transition: transform 0.2s, background 0.2s;
}

.timeline-item:hover {
  transform: translateX(5px);
  background: rgba(255, 255, 255, 0.08);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.timeline-info { flex: 1; color: var(--text-light); font-size: 0.95rem; line-height: 1.4; }
.timeline-info strong { color: var(--primary); font-weight: 600; }
.timeline-info small { display: block; margin-top: 4px; font-size: 0.8rem; color: #888; }

.step-card {
    border: 1px solid #333;
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 20px;
    width: 200px;
    text-align: center;
    transition: transform 0.3s;
}
.step-card:hover {
    transform: translateY(-5px);
    border-color: var(--primary);
}
.step-icon { font-size: 36px; margin-bottom: 10px; color: var(--primary); }
</style>
</head>

<body>
  <main class="main-content">
    <section class="contributors-hero">
      <div class="container">
        <h1>Our Amazing Contributors</h1>
        <p>
          Meet the talented developers and contributors who help make Smart Resume Reviewer better every day.
        </p>
      </div>
      
      <div class="contributor-container">
        <h1>🌟 GitHub Contributors Dashboard</h1>
        
        <div id="stats">
          <div class="stat-box">
            <h3>Contributors</h3>
            <p id="totalContributors">0</p>
          </div>
          <div class="stat-box">
            <h3>Commits</h3>
            <p id="totalCommits">0</p>
          </div>
          <div class="stat-box">
            <h3>Total PRs</h3>
            <p id="totalPRs">0</p>
          </div>
          <div class="stat-box">
            <h3>Total Points</h3>
            <p id="totalPoints">0</p>
          </div>
          <div class="stat-box">
            <h3>Stars</h3>
            <p id="totalStars">0</p>
          </div>
          <div class="stat-box">
            <h3>Forks</h3>
            <p id="totalForks">0</p>
          </div>
        </div>

        <div id="projectLeadContainer" style="display: flex; justify-content: center; margin: 3rem 0;">
          <div class="contributor special-lead">
            <div class="lead-badge" style="margin-bottom: 10px;">👑 Project Lead</div>
            <img src="https://avatars.githubusercontent.com/SharanyaAchanta" alt="Project Lead">
            <h3 style="margin: 10px 0;">SharanyaAchanta</h3>
            <p>Leading the Smart Resume Reviewer vision.</p>
            <a href="https://github.com/SharanyaAchanta" target="_blank"><i class="fab fa-github"></i> View Profile</a>
          </div>
        </div>

        <div class="search-contributor">
          <input type="text" id="searchInput" placeholder="Search contributor..." />
          <select id="sortBy" class="filter-select">
            <option value="contributions">Most Contributions</option>
            <option value="alphabetical">Alphabetical</option>
            <option value="recent">Recent Activity</option>
          </select>
          <select id="filterLevel" class="filter-select">
            <option value="all">All Contributors</option>
            <option value="top10">Top 10</option>
            <option value="gold">🥇 Gold League</option>
            <option value="silver">🥈 Silver League</option>
            <option value="bronze">🥉 Bronze League</option>
            <option value="new">New Contributors</option>
          </select>
        </div>

        <div id="spinner">
          <div class="spinner-circle"></div>
        </div>

        <div id="contributorsList" class="contributors-grid"></div>

        <div id="controls">
          <button id="prevPage">⬅️ Prev</button>
          <span>Page <span id="currentPage">1</span> of <span id="totalPages">1</span></span>
          <button id="nextPage">Next ➡️</button>
          <button id="refreshData" title="Refresh data">🔄 Refresh</button>
        </div>

        <div id="activityTimeline" class="timeline-container">
          <h2>Recent Activity</h2>
          <div id="timelineContent" class="timeline-content"></div>
        </div>

        <p id="errorMessage"></p>
      </div>
    </section>

    <section class="contribute-section" style="padding: 50px 0; text-align: center">
      <div class="container">
        <div class="section-header" style="margin-bottom: 40px">
          <h2>Want to Contribute?</h2>
          <p>Join our community and help improve Smart Resume Reviewer.</p>
        </div>

        <div class="contribute-steps" style="display: flex; justify-content: center; flex-wrap: wrap; gap: 25px;">
          <div class="step-card">
            <div class="step-icon"><i class="fas fa-clipboard-list"></i></div>
            <h3>Create an Issue</h3>
            <p>Start by creating an issue describing your change.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fab fa-github"></i></div>
            <h3>Fork the Repo</h3>
            <p>Fork the repository to your GitHub account.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fas fa-code-branch"></i></div>
            <h3>Create Branch</h3>
            <p>Create a feature branch for your changes.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fas fa-code"></i></div>
            <h3>Make Changes</h3>
            <p>Implement your features or bug fixes.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fas fa-upload"></i></div>
            <h3>Submit PR</h3>
            <p>Create a pull request for review.</p>
          </div>
        </div>
      </div>
    </section>
  </main>

  <div id="contributorModal" class="contributor-modal">
    <div class="modal-content">
      <span class="modal-close">&times;</span>
      <div class="modal-header">
        <img id="modalAvatar" class="modal-avatar" src="" alt="">
        <div class="modal-info">
          <h2 id="modalName">Username</h2>
          <p id="modalLeague" class="modal-subtitle">League</p>
        </div>
      </div>
      <div class="modal-stats">
        <div class="modal-stat">
          <i class="fas fa-trophy"></i>
          <span id="modalRank">#0</span>
          <p>Rank</p>
        </div>
        <div class="modal-stat">
          <i class="fas fa-star"></i>
          <span id="modalPoints">0</span>
          <p>Points</p>
        </div>
        <div class="modal-stat">
          <i class="fas fa-code-branch"></i>
          <span id="modalPRs">0</span>
          <p>PRs</p>
        </div>
        <div class="modal-stat">
          <i class="fas fa-code"></i>
          <span id="modalCommits">0</span>
          <p>Commits</p>
        </div>
      </div>
      <div class="modal-actions">
          <a id="viewPrBtn" href="#" target="_blank" class="modal-btn primary">
              <i class="fas fa-code-branch"></i> View Pull Requests
          </a>
          <a id="modalGithubLink" href="#" target="_blank" class="modal-btn secondary">
              <i class="fab fa-github"></i> GitHub Profile
          </a>
      </div>
    </div>
  </div>

<script>
// ===== JS logic adapted to Smart Resume Reviewer repo =====

// GitHub Repository Configuration
const REPO_OWNER = "SharanyaAchanta";
const REPO_NAME = "Smart-Resume-Reviewer";
const API_BASE = `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}`;

// Project Lead to exclude from contributors list (lowercase)
const PROJECT_LEAD = "sharanyaachanta";

// State Management
let allContributors = []; 
let filteredContributors = [];
let currentPage = 1;
const itemsPerPage = 15;

// Point System Weights
const POINTS = {
    L3: 11,
    L2: 5,
    L1: 2,
    DEFAULT: 1,
    COMMIT: 1
};

document.addEventListener('DOMContentLoaded', () => {
    initData();
    fetchRecentActivity();
    setupEventListeners();
});

// 1. Data Fetching & Initialization
async function initData() {
    const grid = document.getElementById('contributorsList');
    const errorMessage = document.getElementById('errorMessage');
    
    try {
        document.getElementById('spinner').style.display = 'flex';
        if(grid) grid.innerHTML = '';
        if(errorMessage) errorMessage.innerText = '';

        const [repoRes, contributorsRes] = await Promise.all([
            fetch(API_BASE),
            fetch(`${API_BASE}/contributors?per_page=100`)
        ]);

        if (!repoRes.ok || !contributorsRes.ok) throw new Error("API Limit Exceeded or Network Error");

        const repoData = await repoRes.json();
        const rawContributors = await contributorsRes.json();

        const rawPulls = await fetchAllPulls();
        processData(repoData, rawContributors, rawPulls);

    } catch (error) {
        console.error('Error initializing data:', error);
        document.getElementById('spinner').style.display = 'none';
        if(grid) grid.innerHTML = '';
        if(errorMessage) errorMessage.innerText = 'Failed to load data. GitHub API limit may be exceeded. Please try again later.';
    }
}

async function fetchAllPulls() {
    let pulls = [];
    let page = 1;
    while (page <= 3) {
        try {
            const res = await fetch(`${API_BASE}/pulls?state=all&per_page=100&page=${page}`);
            if (!res.ok) break;
            const data = await res.json();
            if (!data.length) break;
            pulls = pulls.concat(data);
            page++;
        } catch (e) { break; }
    }
    return pulls;
}

// 2. Data Processing
function processData(repoData, contributors, pulls) {
    const statsMap = {};
    let totalProjectPRs = 0;
    let totalProjectPoints = 0;
    let totalProjectCommits = 0;

    // A. Calculate Points from PRs
    pulls.forEach(pr => {
        if (!pr.merged_at) return; 

        const user = pr.user.login.toLowerCase();
        if (!statsMap[user]) statsMap[user] = { prs: 0, points: 0 };

        statsMap[user].prs++;
        totalProjectPRs++;

        let prPoints = 0;
        let hasLevel = false;

        pr.labels.forEach(label => {
            const name = label.name.toLowerCase();
            if (name.includes('level 3')) { prPoints += POINTS.L3; hasLevel = true; }
            else if (name.includes('level 2')) { prPoints += POINTS.L2; hasLevel = true; }
            else if (name.includes('level 1')) { prPoints += POINTS.L1; hasLevel = true; }
        });

        if (!hasLevel) prPoints += POINTS.DEFAULT;

        statsMap[user].points += prPoints;
        totalProjectPoints += prPoints;
    });

    // B. Filter out project lead and merge with profile data
    allContributors = contributors
        .filter(c => c.login.toLowerCase() !== PROJECT_LEAD)
        .map(c => {
            const login = c.login.toLowerCase();
            const userStats = statsMap[login] || { prs: 0, points: 0 };
            
            totalProjectCommits += c.contributions;

            let finalPoints = userStats.points;
            if (finalPoints === 0) {
                finalPoints = c.contributions * POINTS.COMMIT; 
            }

            return {
                login: c.login,
                id: c.id,
                avatar_url: c.avatar_url,
                html_url: c.html_url,
                contributions: c.contributions,
                prs: userStats.prs,
                points: finalPoints
            };
        });

    // C. Initial Sort
    allContributors.sort((a, b) => b.points - a.points);

    // D. Update Stats
    updateGlobalStats(
        contributors.length - 1,
        totalProjectPRs,
        totalProjectPoints,
        repoData.stargazers_count,
        repoData.forks_count,
        totalProjectCommits
    );

    // E. Initialize Filtered Data & Render
    filteredContributors = [...allContributors];
    document.getElementById('spinner').style.display = 'none';
    renderContributors(1);
}

function updateGlobalStats(count, prs, points, stars, forks, commits) {
    safeSetText('totalContributors', count);
    safeSetText('totalCommits', commits);
    safeSetText('totalPRs', prs);
    safeSetText('totalPoints', points);
    safeSetText('totalStars', stars);
    safeSetText('totalForks', forks);
}

// 3. Event Listeners
function setupEventListeners() {
    const searchInput = document.getElementById('searchInput');
    const sortBy = document.getElementById('sortBy');
    const filterLevel = document.getElementById('filterLevel');
    const refreshBtn = document.getElementById('refreshData');
    const prevBtn = document.getElementById('prevPage');
    const nextBtn = document.getElementById('nextPage');

    if (searchInput) {
        searchInput.addEventListener('input', (e) => applyFilters(e.target.value, sortBy.value, filterLevel.value));
    }
    if (sortBy) {
        sortBy.addEventListener('change', (e) => applyFilters(searchInput.value, e.target.value, filterLevel.value));
    }
    if (filterLevel) {
        filterLevel.addEventListener('change', (e) => applyFilters(searchInput.value, sortBy.value, e.target.value));
    }
    if (refreshBtn) {
        refreshBtn.addEventListener('click', () => {
            allContributors = [];
            initData();
        });
    }
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            if (currentPage > 1) { currentPage--; renderContributors(currentPage); }
        });
    }
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            const maxPage = Math.ceil(filteredContributors.length / itemsPerPage);
            if (currentPage < maxPage) { currentPage++; renderContributors(currentPage); }
        });
    }
}

// 4. Filtering
function applyFilters(searchTerm, sortType, levelType) {
    let result = [...allContributors];

    if (searchTerm) {
        const term = searchTerm.toLowerCase();
        result = result.filter(c => c.login.toLowerCase().includes(term));
    }

    if (levelType !== 'all') {
        result = result.filter(c => {
            const league = getLeagueData(c.points);
            if (levelType === 'top10') return true; 
            if (levelType === 'gold') return league.tier === 'tier-gold';
            if (levelType === 'silver') return league.tier === 'tier-silver';
            if (levelType === 'bronze') return league.tier === 'tier-bronze';
            if (levelType === 'new') return c.contributions < 5;
            return true;
        });
    }

    if (sortType === 'contributions') {
        result.sort((a, b) => b.points - a.points);
    } else if (sortType === 'alphabetical') {
        result.sort((a, b) => a.login.localeCompare(b.login));
    } else if (sortType === 'recent') {
        result.sort((a, b) => b.contributions - a.contributions);
    }

    if (levelType === 'top10') {
        result.sort((a, b) => b.points - a.points);
        result = result.slice(0, 10);
    }

    filteredContributors = result;
    currentPage = 1;
    renderContributors(1);
}

// 5. Rendering
function renderContributors(page) {
    const grid = document.getElementById('contributorsList');
    if (!grid) return;
    grid.innerHTML = '';

    const start = (page - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    const itemsToShow = filteredContributors.slice(start, end);

    if (itemsToShow.length === 0) {
        grid.innerHTML = '<p style="grid-column: 1/-1; text-align: center;">No contributors match your search.</p>';
        updatePaginationUI();
        return;
    }

    itemsToShow.forEach((c, index) => {
        const rank = start + index + 1;
        const league = getLeagueData(c.points);

        const card = document.createElement('div');
        card.className = `contributor ${league.tier}`;
        card.onclick = () => openContributorModal(c, league, rank);

        card.innerHTML = `
            <img src="${c.avatar_url}" alt="${c.login}" loading="lazy">
            <span class="cont-name">${c.login}</span>
            <div class="contributor-badges">
                <span class="tier-badge ${league.class}">${league.text}</span>
            </div>
            <div class="contributor-stats">
                 <i class="fas fa-star" style="color:gold"></i> ${c.points} Pts
                 <span style="margin: 0 5px">|</span>
                 <i class="fas fa-code-branch" style="color:#4a90e2"></i> ${c.prs} PRs
            </div>
        `;
        grid.appendChild(card);
    });

    updatePaginationUI();
}

function updatePaginationUI() {
    const maxPage = Math.ceil(filteredContributors.length / itemsPerPage) || 1;
    safeSetText('currentPage', currentPage);
    safeSetText('totalPages', maxPage);
    
    const prev = document.getElementById('prevPage');
    const next = document.getElementById('nextPage');
    if(prev) {
        prev.disabled = currentPage === 1;
        prev.style.opacity = currentPage === 1 ? '0.5' : '1';
    }
    if(next) {
        next.disabled = currentPage === maxPage;
        next.style.opacity = currentPage === maxPage ? '0.5' : '1';
    }
}

// 6. Modal & Utilities
function getLeagueData(points) {
    if (points > 150) return { text: 'Gold 🏆', class: 'badge-gold', tier: 'tier-gold', label: 'Gold League' };
    if (points > 75) return { text: 'Silver 🥈', class: 'badge-silver', tier: 'tier-silver', label: 'Silver League' };
    if (points > 30) return { text: 'Bronze 🥉', class: 'badge-bronze', tier: 'tier-bronze', label: 'Bronze League' };
    return { text: 'Contributor', class: 'badge-contributor', tier: 'tier-contributor', label: 'Contributor' };
}

function openContributorModal(c, league, rank) {
    const modal = document.getElementById('contributorModal');
    if (!modal) return;

    document.getElementById('modalAvatar').src = c.avatar_url;
    document.getElementById('modalName').textContent = c.login;
    document.getElementById('modalGithubLink').href = c.html_url;
    
    safeSetText('modalRank', `#${rank}`);
    safeSetText('modalPoints', c.points);
    safeSetText('modalLeague', league.label);
    safeSetText('modalCommits', c.contributions);
    safeSetText('modalPRs', c.prs);

    const prLink = document.getElementById('viewPrBtn');
    if(prLink) prLink.href = `https://github.com/${REPO_OWNER}/${REPO_NAME}/pulls?q=is%3Apr+author%3A${c.login}`;

    modal.classList.add('active');
}

document.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal-close') ||
        e.target.classList.contains('contributor-modal')) {
        document.getElementById('contributorModal')?.classList.remove('active');
    }
});

function safeSetText(id, text) {
    const el = document.getElementById(id);
    if (el) el.innerText = text;
}

// 7. Recent Activity
async function fetchRecentActivity() {
    try {
        const response = await fetch(`${API_BASE}/commits?per_page=10`);
        if(!response.ok) return;
        const commits = await response.json();
        const container = document.getElementById("timelineContent");
        if (!container) return;
        
        container.innerHTML = commits.map(c => {
            const msg = c.commit.message.split('\n')[0];
            const author = c.commit.author.name;
            const date = new Date(c.commit.author.date).toLocaleDateString();
            return `
                <div class="timeline-item">
                    <div class="timeline-info">
                        <strong>${author}</strong>: ${msg} 
                        <small>${date}</small>
                    </div>
                </div>
            `;
        }).join('');
    } catch (e) { console.error('Timeline error:', e); }
}
</script>

</body>
</html>
    """

    components.html(contributors_html, height=1600, scrolling=True)
