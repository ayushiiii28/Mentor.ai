import streamlit as st
import requests

st.set_page_config(page_title="MENTOR.AI", page_icon="🧠", layout="centered")

st.title("🧠 MENTOR.AI")
st.subheader("Multi-Agent Academic & Career Mentor")
st.write("An intelligent system for study planning, tutoring, assessment, well-being and career guidance.")

backend_url = "http://127.0.0.1:8000/mentor"

query = st.text_area("Describe your academic or career concern:")

if st.button("Get Mentorship"):
    if query.strip():
        with st.spinner("Multi-agents are collaborating..."):
            res = requests.get(backend_url, params={"query": query})
            output = res.json()["response"]

        st.markdown("## 🌟 Mentor Response")
        st.markdown(output)
