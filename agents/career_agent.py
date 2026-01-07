from langchain_core.prompts import PromptTemplate
from agents.llm import llm

career_prompt = PromptTemplate.from_template("""
You are a Career Advisor AI.

Build a personalized career roadmap and skills plan.

User request: {query}
""")

career_chain = career_prompt | llm
