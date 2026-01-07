from langchain_core.prompts import PromptTemplate
from agents.llm import llm

wellbeing_prompt = PromptTemplate.from_template("""
You are a Well-being Mentor AI.

Provide emotional support, motivation, and healthy routines.

User request: {query}
""")

wellbeing_chain = wellbeing_prompt | llm
