🧠 MENTOR.AI
Multi-Agent Academic & Career Intelligence System

MENTOR.AI is an Agentic AI system designed to support students with academics, career planning, well-being, assessments, and resume evaluation.
It leverages multiple specialized AI agents, coordinated through a central orchestrator, to deliver structured, goal-oriented guidance instead of generic chatbot responses.

This project demonstrates the practical use of Agentic AI architecture powered by Large Language Models (LLMs).

<img width="1919" height="959" alt="Screenshot 2026-01-07 133019" src="https://github.com/user-attachments/assets/a628441b-3515-43e8-ada3-ed12741e934e" />


🚀 Key Features

🤖 Multi-Agent Architecture

Academic Planner Agent

Tutor Agent

Assessment Agent

Well-being Agent

Career Guidance Agent

Resume ATS Agent

🧠 Central Orchestrator

Dynamically selects agents based on user mode

Controls prompt rules and output length

Aggregates structured responses

📄 AI Resume ATS Analyzer

PDF resume upload

ATS friendliness check

Skill matching & keyword gap analysis

Recruiter-style feedback

ATS score visualization

🎓 Student Mentor System

Personalized academic guidance

Placement & higher studies mentoring

Mental wellness and productivity support

🌐 Interactive UI

Built with Streamlit

Card-based agent selection

Chat-based mentoring experience

🧩 System Architecture
User (Streamlit UI)
        ↓
Profile + Query
        ↓
Orchestrator (Controller Layer)
        ↓
Agent Selection (Mode)
        ↓
LangChain LLM Chains (Agents)
        ↓
Groq Cloud API (Inference Engine)
        ↓
LLaMA-3.1-8B Model
        ↓
Structured Agent Responses
        ↓
UI Rendering

🛠️ Technology Stack

Python 3.11+

Streamlit – UI & interaction layer

LangChain – Agent framework & LLM orchestration

Groq Cloud API – High-speed LLM inference

LLaMA-3.1-8B-Instant – Foundation model

PyPDF – Resume PDF extraction

Regex & NLP utilities – ATS score parsing

