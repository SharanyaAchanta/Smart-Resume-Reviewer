import streamlit as st
import streamlit.components.v1 as components

def show_contributors_page():
    """COMPLETE contributors page - navbar + content + footer ALL INSIDE"""
    
    # Configure page
    st.set_page_config(page_title="Contributors - Smart Resume Reviewer", 
                      page_icon="👥", layout="wide")
    
    # ========================================
    # NAVBAR (same as your header.py)
    # ========================================
    st.markdown("""
    <style>
    .navbar { 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
        padding: 1rem 2rem; 
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
        box-shadow: 0 4px 20px rgba(102,126,234,0.3); 
        position: sticky; 
        top: 0; 
        z-index: 1000;
    }
    .navbar h3 { margin: 0; color: white; font-weight: 700; }
    .nav-links { display: flex; gap: 2rem; align-items: center; }
    .nav-links a { color: white; text-decoration: none; font-weight: 600; padding: 0.5rem 1rem; border-radius: 25px; transition: all 0.3s; }
    .nav-links a:hover { background: rgba(255,255,255,0.2); transform: translateY(-2px); }
    .active { background: rgba(255,255,255,0.3) !important; }
    </style>
    <div class="navbar">
        <div style="display: flex; align-items: center; gap: 1rem;">
            <i class="fas fa-users" style="font-size: 2rem; color: white;"></i>
            <h3>Smart Resume Reviewer</h3>
        </div>
        <div class="nav-links">
            <a href="/">🏠 Home</a>
            <a href="/Home">📤 Resume Analyzer</a>
            <a href="#" class="active">👥 Contributors</a>
            <a href="https://github.com/SharanyaAchanta/Smart-Resume-Reviewer" target="_blank">
                <i class="fab fa-github"></i> GitHub
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # ========================================
    # FULL CONTRIBUTORS DASHBOARD
    # ========================================
    contributors_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
        :root{--primary:#667eea;--primary-dark:#764ba2;--dark:#1a1b1e;--text:#ffffff;--text-light:#b8bcc5;--accent:#2ecc71;--glass:rgba(255,255,255,0.05);--glass-border:rgba(255,255,255,0.1);}
        *{margin:0;padding:0;box-sizing:border-box;}
        body{font-family:'Segoe UI',sans-serif;background:var(--dark);color:var(--text);padding-top:80px;}
        .container{max-width:1400px;margin:0 auto;padding:2rem;}
        .hero{text-align:center;padding:3rem 2rem;background:linear-gradient(135deg,var(--primary),var(--primary-dark));border-radius:20px;margin-bottom:3rem;}
        .hero h1{font-size:3rem;background:linear-gradient(45deg,var(--text),#ffd700);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:1rem;}
        .stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:2rem;margin-bottom:3rem;}
        .stat-box{background:var(--glass);backdrop-filter:blur(20px);border:1px solid var(--glass-border);border-radius:20px;padding:2rem;text-align:center;transition:all 0.3s;}
        .stat-box:hover{transform:translateY(-10px);border-color:var(--primary);}
        .stat-value{font-size:3rem;font-weight:800;color:var(--primary);margin-bottom:0.5rem;}
        .controls{display:flex;gap:1rem;margin-bottom:2rem;flex-wrap:wrap;justify-content:center;}
        .search-input,.filter-select{padding:1rem 1.5rem;border:2px solid var(--glass-border);border-radius:50px;background:var(--glass);color:var(--text);min-width:250px;}
        .search-input:focus,.filter-select:focus{outline:none;border-color:var(--primary);background:rgba(255,255,255,0.15);}
        .loading{text-align:center;padding:4rem;color:var(--text-light);}
        .spinner{width:60px;height:60px;border:4px solid var(--glass);border-top:4px solid var(--primary);border-radius:50%;animation:spin 1s linear infinite;margin:0 auto 1rem;}
        @keyframes spin{0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}
        .contributors-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:2rem;margin-bottom:3rem;}
        .contributor-card{background:var(--glass);backdrop-filter:blur(20px);border:1px solid var(--glass-border);border-radius:20px;padding:2rem;cursor:pointer;transition:all 0.3s;position:relative;}
        .contributor-card:hover{transform:translateY(-10px);border-color:var(--primary);}
        .avatar{width:80px;height:80px;border-radius:50%;border:4px solid rgba(255,255,255,0.2);margin-bottom:1.5rem;display:block;}
        .contributor-card:hover .avatar{transform:scale(1.1);}
        .info h3{font-size:1.5rem;margin-bottom:0.5rem;text-align:center;}
        .info .contributions{text-align:center;color:var(--accent);font-weight:600;font-size:1.1rem;}
        .badge{position:absolute;top:1rem;right:1rem;padding:0.5rem 1rem;border-radius:20px;font-size:0.8rem;font-weight:600;}
        .badge.user{background:rgba(46,204,113,0.2);color:var(--accent);}
        .badge.org{background:rgba(102,126,234,0.2);color:var(--primary);}
        .pagination{display:flex;justify-content:center;gap:0.5rem;flex-wrap:wrap;}
        .page-btn{padding:0.8rem 1.2rem;border:2px solid var(--glass-border);background:var(--glass);color:var(--text-light);border-radius:25px;cursor:pointer;transition:all 0.3s;font-weight:600;}
        .page-btn:hover,.page-btn.active{background:var(--primary);border-color:var(--primary);color:white;}
        .modal{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);z-index:1000;align-items:center;justify-content:center;}
        .modal-content{background:rgba(26,27,30,0.95);border:1px solid var(--glass-border);border-radius:20px;max-width:500px;width:90%;max-height:80vh;overflow-y:auto;padding:2rem;position:relative;}
        .close-btn{position:absolute;top:1rem;right:1rem;background:none;border:none;font-size:2rem;color:var(--text-light);cursor:pointer;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;}
        .close-btn:hover{background:rgba(255,255,255,0.1);color:var(--text);}
        .btn{display:inline-block;padding:1rem 2rem;background:linear-gradient(45deg,var(--primary),var(--primary-dark));color:white;text-decoration:none;border-radius:50px;font-weight:600;width:100%;text-align:center;margin-top:1rem;}
        .error{text-align:center;color:#ff6b6b;padding:3rem;font-size:1.2rem;}
        @media(max-width:768px){.container{padding:1rem;}.hero h1{font-size:2rem;}.stats{grid-template-columns:repeat(2,1fr);}.controls{flex-direction:column;}.contributors-grid{grid-template-columns:1fr;}}
        .footer{padding:2rem;background:linear-gradient(135deg,var(--primary-dark),var(--dark));text-align:center;color:var(--text-light);border-top:1px solid var(--glass-border);}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="hero">
                <h1>👥 Contributors</h1>
                <p>Live data from <strong>SharanyaAchanta/Smart-Resume-Reviewer</strong></p>
            </div>
            
            <div class="stats" id="stats"></div>
            
            <div class="controls">
                <input type="text" id="search" placeholder="🔍 Search contributors..." class="search-input">
                <select id="filter" class="filter-select">
                    <option value="all">All Contributors</option>
                    <option value="top10">Top 10</option>
                    <option value="new">New Contributors</option>
                </select>
            </div>
            
            <div class="loading" id="loading" style="display:none;">
                <div class="spinner"></div>
                <p>Fetching live GitHub data...</p>
            </div>
            
            <div class="contributors-grid" id="contributors-cards"></div>
            <div class="pagination" id="pagination"></div>
        </div>
        
        <div class="modal" id="contributor-modal">
            <div class="modal-content" id="modal-content"></div>
        </div>
        
        <div class="footer">
            <p>© 2025 Smart Resume Reviewer | Data from <i class="fab fa-github"></i> GitHub API | Made with ❤️</p>
        </div>
        
        <script>
        const REPO_OWNER="SharanyaAchanta",REPO_NAME="Smart-Resume-Reviewer",API_BASE=`https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}`;
        let allContributors=[],filteredContributors=[],currentPage=1,ITEMS_PER_PAGE=12;
        
        async function fetchContributors(){
            const stats=document.getElementById('stats'),cards=document.getElementById('contributors-cards'),loading=document.getElementById('loading');
            try{
                loading.style.display='block';cards.innerHTML='';
                const[contributorsRes,repoRes]=await Promise.all([fetch(`${API_BASE}/contributors?per_page=100`),fetch(API_BASE)]);
                const contributors=await contributorsRes.json(),repo=await repoRes.json();
                allContributors=contributors.filter(c=>c.contributions>0).map(c=>({login:c.login,avatar_url:c.avatar_url,contributions:c.contributions,html_url:c.html_url,type:c.type==='User'?'User':'Organization'})).sort((a,b)=>b.contributions-a.contributions);
                filteredContributors=[...allContributors];
                stats.innerHTML=`<div class="stat-box"><div class="stat-value">${allContributors.length}</div><div class="stat-label">Contributors</div></div><div class="stat-box"><div class="stat-value">${repo.stargazers_count}⭐</div><div class="stat-label">Stars</div></div><div class="stat-box"><div class="stat-value">${repo.forks_count}🍴</div><div class="stat-label">Forks</div></div>`;
                renderContributors();setupEventListeners();
            }catch(e){cards.innerHTML='<div class="error">Failed to load contributors</div>';}finally{loading.style.display='none';}
        }
        
        function renderContributors(){
            const cards=document.getElementById('contributors-cards'),start=(currentPage-1)*ITEMS_PER_PAGE,end=start+ITEMS_PER_PAGE,pageContributors=filteredContributors.slice(start,end);
            cards.innerHTML=pageContributors.map(c=>`<div class="contributor-card" onclick="showModal('${c.login}')"><img src="${c.avatar_url}" alt="${c.login}" class="avatar"><div class="info"><h3>${c.login}</h3><p class="contributions">${c.contributions} contributions</p></div><div class="badge ${c.type.toLowerCase()}">${c.type}</div></div>`).join('');
            const totalPages=Math.ceil(filteredContributors.length/ITEMS_PER_PAGE);
            document.getElementById('pagination').innerHTML=Array.from({length:totalPages},(_,i)=>i+1).map(i=>`<button class="page-btn ${i===currentPage?'active':''}" onclick="changePage(${i})">${i}</button>`).join('');
        }
        
        function showModal(login){
            const contributor=allContributors.find(c=>c.login===login),modalContent=document.getElementById('modal-content');
            modalContent.innerHTML=`<button class="close-btn" onclick="closeModal()">&times;</button><img src="${contributor.avatar_url}" alt="${contributor.login}" style="width:100px;height:100px;border-radius:50%;margin:1rem auto;display:block;border:4px solid var(--primary);"><h2>${contributor.login}</h2><p><strong>${contributor.contributions}</strong> contributions</p><a href="${contributor.html_url}" target="_blank" class="btn">View GitHub Profile</a>`;
            document.getElementById('contributor-modal').style.display='flex';
        }
        
        function closeModal(){document.getElementById('contributor-modal').style.display='none';}
        function changePage(page){currentPage=page;renderContributors();}
        
        function setupEventListeners(){
            document.getElementById('search').addEventListener('input',e=>{const query=e.target.value.toLowerCase();filteredContributors=allContributors.filter(c=>c.login.toLowerCase().includes(query));currentPage=1;renderContributors();});
            document.getElementById('filter').addEventListener('change',e=>{const value=e.target.value;if(value==='top10')filteredContributors=allContributors.slice(0,10);else if(value==='new')filteredContributors=allContributors.filter(c=>c.contributions<=5);else filteredContributors=[...allContributors];currentPage=1;renderContributors();});
            document.getElementById('contributor-modal').addEventListener('click',e=>{if(e.target.id==='contributor-modal')closeModal();});
        }
        
        fetchContributors();
        </script>
    </body>
    </html>
    """
    
    components.html(contributors_html, height=1600, scrolling=True)

# END OF FILE
