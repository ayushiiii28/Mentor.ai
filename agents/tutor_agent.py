from langchain_core.prompts import PromptTemplate
from agents.llm import llm

tutor_prompt = PromptTemplate.from_template("""
You are a Tutor AI.

Explain the topic clearly with examples.

User request: {query}
""")

tutor_chain = tutor_prompt | llm
