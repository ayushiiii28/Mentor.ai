from langchain_core.prompts import PromptTemplate
from agents.llm import llm

assessment_prompt = PromptTemplate.from_template("""
You are an Assessment AI.

Generate quiz questions and evaluation strategies.

User request: {query}
""")

assessment_chain = assessment_prompt | llm
