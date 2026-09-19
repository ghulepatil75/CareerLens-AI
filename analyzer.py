import re

COMMON_SKILLS = [
    "python","java","c","c++","sql","html","css","javascript","react","flask",
    "django","git","github","excel","communication","leadership","embedded",
    "iot","arduino","esp32","matlab","autocad","pcb","vlsi","testing",
    "problem solving","teamwork","linux","cloud","data analysis"
]
SECTIONS = ["summary","objective","education","experience","work experience",
            "projects","skills","certifications","internship","achievements"]

def analyze_resume(text, role="", company="", job_description=""):
    clean = re.sub(r"\s+", " ", text).strip()
    lower = clean.lower()
    words = re.findall(r"\b[\w+#.-]+\b", lower)
    word_count = len(words)
    found_skills = [s for s in COMMON_SKILLS if s in lower]
    missing = []
    target = (job_description + " " + role).lower()
    for skill in COMMON_SKILLS:
        if skill in target and skill not in lower:
            missing.append(skill)
    section_hits = [s for s in SECTIONS if s in lower]
    contact_checks = {
        "email": bool(re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", clean)),
        "phone": bool(re.search(r"(?:\+?\d[\d ()-]{8,}\d)", clean)),
        "linkedin": "linkedin.com" in lower,
        "github": "github.com" in lower
    }
    score = 35
    score += min(20, len(section_hits) * 3)
    score += min(15, len(found_skills) * 1.5)
    score += 10 if contact_checks["email"] else 0
    score += 5 if contact_checks["phone"] else 0
    score += 5 if word_count >= 250 else 0
    score = int(min(100, round(score)))

    improvements = []
    if word_count < 250: improvements.append("Add relevant detail about projects, experience, and achievements.")
    if not contact_checks["email"]: improvements.append("Add a professional email address.")
    if not contact_checks["phone"]: improvements.append("Add a valid phone number.")
    if "summary" not in lower and "objective" not in lower: improvements.append("Add a focused professional summary or objective.")
    if "projects" not in lower: improvements.append("Include 2–4 relevant projects with tools and outcomes.")
    if "experience" not in lower and "internship" not in lower: improvements.append("Add internship, practical training, volunteering, or project experience.")
    if not contact_checks["linkedin"]: improvements.append("Add a LinkedIn profile link if available.")
    if not contact_checks["github"] and any(x in lower for x in ["python","iot","embedded","programming"]):
        improvements.append("Add GitHub projects or a portfolio link if relevant.")

    strengths = []
    if found_skills: strengths.append("Relevant skills were detected.")
    if "education" in lower: strengths.append("Education information appears to be included.")
    if "projects" in lower: strengths.append("A projects section appears to be present.")
    if contact_checks["email"] and contact_checks["phone"]: strengths.append("Basic contact details were detected.")
    if not strengths: strengths.append("Your resume has been processed and can be improved with the recommendations below.")

    return {
        "score": score,
        "label": "ATS-style estimate, not a hiring prediction",
        "word_count": word_count,
        "sections_found": section_hits,
        "skills_found": found_skills,
        "missing_keywords": missing[:20],
        "contact_checks": contact_checks,
        "strengths": strengths,
        "improvements": improvements,
        "role": role or "Not specified",
        "company": company or "Not specified",
        "disclaimer": "This result is an educational ATS-style estimate. It does not guarantee ATS approval, interviews, or employment."
    }
