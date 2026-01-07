from agents.planner_agent import planner_chain
from agents.tutor_agent import tutor_chain
from agents.assessment_agent import assessment_chain
from agents.wellbeing_agent import wellbeing_chain
from agents.career_agent import career_chain

MAX_CHARS = 1800

def run_mentor_ai(query: str, mode: str = "Full Mentor"):

    query = query[:MAX_CHARS]

    base_prompt = f"""
User request:
{query}

Rules:
- Bullet points only
- Clear and concise
- Max 100 words
"""

    outputs = {}

    # -------- FULL MENTOR MODE --------
    if mode == "Full Mentor":
        outputs["planner"] = planner_chain.invoke({"query": base_prompt}).content
        outputs["tutor"] = tutor_chain.invoke({"query": base_prompt}).content
        outputs["assessment"] = assessment_chain.invoke({"query": base_prompt}).content
        outputs["wellbeing"] = wellbeing_chain.invoke({"query": base_prompt}).content
        outputs["career"] = career_chain.invoke({"query": base_prompt}).content

    # -------- SINGLE AGENT MODES --------
    elif mode == "Planner":
        outputs["planner"] = planner_chain.invoke({"query": base_prompt}).content

    elif mode == "Tutor":
        outputs["tutor"] = tutor_chain.invoke({"query": base_prompt}).content

    elif mode == "Assessment":
        outputs["assessment"] = assessment_chain.invoke({"query": base_prompt}).content

    elif mode == "Well-being":
        outputs["wellbeing"] = wellbeing_chain.invoke({"query": base_prompt}).content

    elif mode == "Career":
        outputs["career"] = career_chain.invoke({"query": base_prompt}).content

    # -------- FORMAT OUTPUT --------
    final_output = ""

    if "planner" in outputs:
        final_output += f"📘 ACADEMIC PLAN\n{outputs['planner']}\n\n"

    if "tutor" in outputs:
        final_output += f"📖 TUTOR SUPPORT\n{outputs['tutor']}\n\n"

    if "assessment" in outputs:
        final_output += f"📝 ASSESSMENT\n{outputs['assessment']}\n\n"

    if "wellbeing" in outputs:
        final_output += f"🌱 WELL-BEING SUPPORT\n{outputs['wellbeing']}\n\n"

    if "career" in outputs:
        final_output += f"🚀 CAREER GUIDANCE\n{outputs['career']}\n\n"

    return final_output.strip()
