from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.2
)

prompt = PromptTemplate(
    input_variables=["resume_text", "job_desc"],
    template="""
You are an ATS system and technical recruiter.

Resume:
{resume_text}

Job Description:
{job_desc}

Perform the following:

1. Give an ATS SCORE out of 100 (must be first line).
2. ATS friendliness check
3. Skill match analysis
4. Missing keywords
5. Role fit evaluation
6. Resume improvement suggestions
7. Rewrite 2 bullets to be stronger

Rules:
- Start with: ATS SCORE: <number>/100
- Use clear section headings
- Bullet points only
- Be realistic and critical
"""
)

resume_chain = prompt | llm
