from agents.planner_agent import planner_chain
from agents.tutor_agent import tutor_chain
from agents.assessment_agent import assessment_chain
from agents.wellbeing_agent import wellbeing_chain
from agents.career_agent import career_chain
from core.memory import SimpleMemory

memory = SimpleMemory()

def run_mentor_ai(query: str):

    memory.add(f"User: {query}")
    context = "\n".join(memory.get_last())

    full_query = f"""
Previous context:
{context}

Current request:
{query}
"""

    responses = {
        "planner": planner_chain.invoke({"query": full_query}).content,
        "tutor": tutor_chain.invoke({"query": full_query}).content,
        "assessment": assessment_chain.invoke({"query": full_query}).content,
        "wellbeing": wellbeing_chain.invoke({"query": full_query}).content,
        "career": career_chain.invoke({"query": full_query}).content,
    }

    final_output = f"""
📘 ACADEMIC PLAN
{responses['planner']}

📖 TUTOR SUPPORT
{responses['tutor']}

📝 ASSESSMENT
{responses['assessment']}

🌱 WELL-BEING SUPPORT
{responses['wellbeing']}

🚀 CAREER GUIDANCE
{responses['career']}
"""

    memory.add(final_output)
    return final_output
