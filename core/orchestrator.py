from agents.planner_agent import planner_chain
from agents.tutor_agent import tutor_chain
from agents.assessment_agent import assessment_chain
from agents.wellbeing_agent import wellbeing_chain
from agents.career_agent import career_chain
from agents.resume_agent import resume_chain
from agents.party_agent import party_chain

MAX_CHARS = 1800


# =========================
# 🎓 MULTI-AGENT MENTOR
# =========================
def run_mentor_ai(query: str, mode: str = "Full Mentor"):

    query = query[:MAX_CHARS]

    if mode == "Full Mentor":
        rules = "- Bullet points\n- Very concise\n- Max 80 words"
    else:
        rules = "- Bullet points\n- Detailed\n- Practical\n- Examples\n- Max 220 words"

    base_prompt = f"""
User request:
{query}

Rules:
{rules}
"""

    outputs = {}

    if mode == "Full Mentor":
        outputs["planner"] = planner_chain.invoke({"query": base_prompt}).content
        outputs["tutor"] = tutor_chain.invoke({"query": base_prompt}).content
        outputs["assessment"] = assessment_chain.invoke({"query": base_prompt}).content
        outputs["wellbeing"] = wellbeing_chain.invoke({"query": base_prompt}).content
        outputs["career"] = career_chain.invoke({"query": base_prompt}).content
        outputs["party"] = party_chain.invoke({"query": base_prompt}).content


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

    elif mode == "Party":
        outputs["party"] = party_chain.invoke({"query": base_prompt}).content

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
    if "party" in outputs:
        final_output += f"🎉 PARTY PLANNER\n{outputs['party']}\n\n"

    return final_output.strip()


# =========================
# 📄 RESUME ATS SYSTEM
# =========================
def run_resume_ai(resume_text: str, job_desc: str = ""):
    resume_text = resume_text[:3500]
    job_desc = job_desc[:1500]

    return resume_chain.invoke({
        "resume_text": resume_text,
        "job_desc": job_desc or "General software / AI role"
    }).content
