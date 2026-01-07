import streamlit as st
import requests

st.set_page_config(
    page_title="MENTOR.AI",
    page_icon="🧠",
    layout="wide"
)

BACKEND_URL = "http://127.0.0.1:8000/mentor"

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
    padding: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.3);
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

# -------------------- AGENT STATE --------------------
if "mode" not in st.session_state:
    st.session_state.mode = "Full Mentor"

def set_mode(mode):
    st.session_state.mode = mode

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
    st.markdown("### ⚙️ System Capabilities")
    st.markdown("✔ Personalized planning")
    st.markdown("✔ Intelligent tutoring")
    st.markdown("✔ AI assessments")
    st.markdown("✔ Emotional support")
    st.markdown("✔ Career intelligence")

# -------------------- MAIN AREA --------------------
st.markdown("# 🎓 MENTOR.AI")
st.markdown("### An Intelligent Multi-Agent System for Students")
st.write(
    "MENTOR.AI collaborates multiple AI agents to guide students in academics, career planning, assessment, and well-being."
)

# ----------- AGENT CARDS -----------
st.markdown("## 🧩 Choose Your Mentor Agent")

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    if st.button("📘 Academic Planner", use_container_width=True):
        set_mode("Planner")

with col2:
    if st.button("📖 Tutor Agent", use_container_width=True):
        set_mode("Tutor")

with col3:
    if st.button("📝 Assessment Agent", use_container_width=True):
        set_mode("Assessment")

with col4:
    if st.button("🌱 Well-being Agent", use_container_width=True):
        set_mode("Well-being")

with col5:
    if st.button("🚀 Career Mentor", use_container_width=True):
        set_mode("Career")

with col6:
    if st.button("🤖 Full Mentor Mode", use_container_width=True):
        set_mode("Full Mentor")

st.markdown(f"<div class='active-agent'>Active Agent: {st.session_state.mode}</div>", unsafe_allow_html=True)

st.markdown("---")

# -------------------- CHAT SYSTEM --------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

for msg in st.session_state.chat:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

user_input = st.chat_input("Describe your academic or career concern...")

if user_input:
    profile_context = f"""
Student profile:
Name: {name}
Year: {year}
Domain: {domain}
Goals: {goals}
"""

    final_query = profile_context + "\nUser query: " + user_input

    st.session_state.chat.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("🤖 Multi-agents are collaborating..."):
            response = requests.get(
                BACKEND_URL,
                params={
                    "query": final_query,
                    "mode": st.session_state.mode
                }
            )
            result = response.json()["response"]
            st.markdown(result)

    st.session_state.chat.append({"role": "assistant", "content": result})

# -------------------- FOOTER --------------------
st.markdown("<div class='footer'>MENTOR.AI · Multi-Agent Academic & Career Intelligence System</div>", unsafe_allow_html=True)
