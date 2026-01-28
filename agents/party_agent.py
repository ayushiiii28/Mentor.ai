from langchain_core.prompts import PromptTemplate
from agents.llm import llm

party_prompt = PromptTemplate.from_template("""
You are a party planner AI.

Build a personalized party plan.

User request: {query}
""")

party_chain = party_prompt | llm
