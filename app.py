import streamlit as st
import requests

st.set_page_config(
    page_title="MENTOR.AI",
    page_icon="🧠",
    layout="wide"
)

BACKEND_URL = "http://127.0.0.1:8000/mentor"

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.title("🧠 MENTOR.AI")
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
st.title("🎓 MENTOR.AI")
st.subheader("An Intelligent Multi-Agent System for Students")
st.write(
    "MENTOR.AI collaborates multiple AI agents to guide students in academics, career planning, assessment, and well-being."
)

if "chat" not in st.session_state:
    st.session_state.chat = []

# Display chat history
for msg in st.session_state.chat:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Chat input
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
            response = requests.get(BACKEND_URL, params={"query": final_query})
            result = response.json()["response"]
            st.markdown(result)

    st.session_state.chat.append({"role": "assistant", "content": result})

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption("MENTOR.AI · Multi-Agent Academic & Career Intelligence System")
