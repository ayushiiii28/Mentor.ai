import streamlit as st
from core.orchestrator import run_mentor_ai, run_resume_ai
from pypdf import PdfReader
import re

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="MENTOR.AI",
    page_icon="🧠",
    layout="wide"
)

# -------------------- GLOBAL STYLING --------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    color: white;
}

/* Titles */
h1, h2, h3 {
    background: linear-gradient(90deg, #a78bfa, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Agent cards */
div.stButton > button {
    height: 95px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.15);
    font-size: 17px;
    font-weight: 700;
    background: linear-gradient(135deg, #1e1b4b, #0f172a);
    color: #e5e7eb;
    box-shadow: 0 0 20px rgba(167,139,250,0.15);
    transition: all 0.25s ease-in-out;
}
div.stButton > button:hover {
    border: 1px solid #22d3ee;
    box-shadow: 0 0 25px rgba(34,211,238,0.5);
    transform: scale(1.04);
    color: white;
}

/* Chat bubbles */
[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.04);
    border-radius: 16px;
    padding: 12px;
    margin-bottom: 10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #020617, #0f172a);
    border-right: 1px solid rgba(255,255,255,0.1);
}

/* Inputs */
textarea, input {
    background-color: rgba(255,255,255,0.05) !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Active agent badge */
.active-agent {
    background: linear-gradient(90deg, #22d3ee, #a78bfa);
    color: black;
    padding: 10px 16px;
    border-radius: 999px;
    font-weight: 700;
    display: inline-block;
    margin-top: 10px;
}

/* Footer */
.footer {
    text-align: center;
    opacity: 0.6;
    padding-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- PDF ENGINE --------------------
MAX_CHARS = 3500

def extract_text(file):
    reader = PdfReader(file)
    text = []
    for page in reader.pages:
        try:
            t = page.extract_text()
            if t:
                text.append(t)
        except:
            continue

    final_text = " ".join("\n".join(text).split())
    if not final_text.strip():
        return "No readable text found. Possibly scanned PDF."

    return final_text[:MAX_CHARS]

# -------------------- SCORE PARSER --------------------
def extract_score(text):
    match = re.search(r"ATS SCORE[:\s]*([0-9]{1,3})", text)
    if match:
        return min(int(match.group(1)), 100)
    return None

# -------------------- STATE --------------------
if "mode" not in st.session_state:
    st.session_state.mode = "Full Mentor"

if "page" not in st.session_state:
    st.session_state.page = "Mentor"

if "chat" not in st.session_state:
    st.session_state.chat = []

def set_mode(mode):
    st.session_state.mode = mode
    st.session_state.page = "Mentor"

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.markdown("## 🧠 MENTOR.AI")
    st.caption("Multi-Agent Academic & Career Mentor")

    st.markdown("### 👤 Student Profile")
    name = st.text_input("Name", placeholder="Your name")
    year = st.selectbox("Year of study", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
    domain = st.text_input("Domain / Major", placeholder="AI / CSE / Data Science")
    goals = st.text_area("Goals", placeholder="Placements, GATE, MS, Research...")

    st.markdown("---")
    st.markdown("### 🧩 Modules")
    if st.button("🎓 Mentor System", use_container_width=True):
        st.session_state.page = "Mentor"
    if st.button("📄 Resume ATS", use_container_width=True):
        st.session_state.page = "Resume"

# =========================
# 🎓 MENTOR SYSTEM
# =========================
if st.session_state.page == "Mentor":

    st.markdown("# 🎓 MENTOR.AI")
    st.markdown("### Intelligent Multi-Agent System for Students")

    st.markdown("## 🧩 Choose Your Mentor Agent")

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)

    with col1:
        if st.button("📘 Academic Planner", use_container_width=True): set_mode("Planner")
    with col2:
        if st.button("📖 Tutor Agent", use_container_width=True): set_mode("Tutor")
    with col3:
        if st.button("📝 Assessment Agent", use_container_width=True): set_mode("Assessment")
    with col4:
        if st.button("🌱 Well-being Agent", use_container_width=True): set_mode("Well-being")
    with col5:
        if st.button("🚀 Career Mentor", use_container_width=True): set_mode("Career")
    with col6:
        if st.button("🎉 Party Planner", use_container_width=True): set_mode("Party")
    with col7:
        if st.button("🤖 Full Mentor Mode", use_container_width=True): set_mode("Full Mentor")

    st.markdown(f"<div class='active-agent'>Active Agent: {st.session_state.mode}</div>", unsafe_allow_html=True)
    st.markdown("---")

    # ---------- CHAT HISTORY ----------
    for msg in st.session_state.chat:
        st.chat_message(msg["role"]).markdown(msg["content"])

    user_input = st.chat_input("Describe your academic or career concern...")

    if user_input:
        profile_context = f"""
Student profile:
Name: {name}
Year: {year}
Domain: {domain}
Goals: {goals}
"""

        final_query = profile_context + "\nUser request: " + user_input

        st.session_state.chat.append({"role": "user", "content": user_input})
        st.chat_message("user").markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner(f"🤖 {st.session_state.mode} agent working..."):
                result = run_mentor_ai(final_query, st.session_state.mode)
                st.markdown(result)

        st.session_state.chat.append({"role": "assistant", "content": result})

# =========================
# 📄 RESUME ATS SYSTEM
# =========================
elif st.session_state.page == "Resume":

    st.markdown("# 📄 Resume ATS Analyzer")
    st.caption("Upload your resume and receive an AI recruiter evaluation")

    uploaded_file = st.file_uploader("📤 Upload Resume (PDF only)", type=["pdf"])
    job_desc = st.text_area("🎯 Paste Job Description (optional)", height=180)

    if st.button("🔍 Analyze Resume", use_container_width=True):

        if not uploaded_file:
            st.warning("Please upload a resume PDF.")
        else:
            with st.spinner("📄 Reading resume..."):
                resume_text = extract_text(uploaded_file)

            with st.spinner("🤖 Running ATS & recruiter analysis..."):
                result = run_resume_ai(resume_text, job_desc)

            score = extract_score(result)

            st.markdown("## 📊 Resume Intelligence Report")

            if score is not None:
                st.metric("ATS Score", f"{score}/100")
                st.progress(score / 100)

            st.markdown(result)

# -------------------- FOOTER --------------------
st.markdown("<div class='footer'>MENTOR.AI · Multi-Agent Academic & Career Intelligence System</div>", unsafe_allow_html=True)
