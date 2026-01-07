from langchain_core.prompts import PromptTemplate
from agents.llm import llm

planner_prompt = PromptTemplate.from_template("""
You are an Academic Planner AI.

User request: {query}

Create a structured, realistic study plan.
""")

planner_chain = planner_prompt | llm
