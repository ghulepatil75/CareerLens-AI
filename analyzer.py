import re
from collections import Counter

SKILL_GROUPS = {
    "Programming": ["python","java","c","c++","javascript","kotlin"],
    "Web": ["html","css","react","node.js","flask","django"],
    "Data & AI": ["sql","pandas","numpy","machine learning","deep learning","artificial intelligence"],
    "Cloud & DevOps": ["git","github","docker","aws","linux"],
    "Electronics": ["arduino","esp32","iot","embedded systems","embedded c","pcb design","vlsi","verilog","matlab"],
    "Professional": ["leadership","teamwork","communication","problem solving","project management"]
}

SECTION_ALIASES = {
    "summary": ["summary","objective","profile"],
    "education": ["education","qualifications"],
    "experience": ["experience","work experience","internship"],
    "projects": ["projects","academic projects"],
    "skills": ["skills","technical skills"],
    "certifications": ["certifications","certificates"],
    "achievements": ["achievements","awards"]
}

def clean(text):
    return re.sub(r"\s+", " ", text.lower()).strip()

def has_term(text, term):
    return bool(re.search(r"(?<!\w)" + re.escape(term.lower()) + r"(?!\w)", text))

def detect_skills(text):
    text = clean(text)
    groups, all_skills = {}, []
    for group, skills in SKILL_GROUPS.items():
        found = sorted({skill.title() for skill in skills if has_term(text, skill)})
        if found:
            groups[group] = found
            all_skills.extend(found)
    return groups, sorted(set(all_skills))

def detect_sections(text):
    text = clean(text)
    return {section: any(has_term(text, alias) for alias in aliases)
            for section, aliases in SECTION_ALIASES.items()}

def keywords(text, limit=50):
    stop = {"about","also","from","have","with","your","this","that","skills","skill","experience","project","projects","resume","job","work","role","company","candidate","team"}
    words = re.findall(r"[a-zA-Z][a-zA-Z+#.-]{2,}", text.lower())
    return [w for w, _ in Counter(w for w in words if w not in stop).most_common(limit)]

def job_match(resume, description):
    if not description.strip():
        return 0, [], []
    resume = clean(resume)
    words = keywords(description)
    if not words:
        return 0, [], []
    matched = [w for w in words if has_term(resume, w)]
    missing = [w for w in words if w not in matched]
    return min(round(len(matched) / len(words) * 100), 100), matched[:20], missing[:15]

def analyze_resume(text, qualification="", degree="", purpose="", company="", role="", job_description=""):
    sections = detect_sections(text)
    skill_groups, skills = detect_skills(text)
    low = clean(text)
    score = 0
    breakdown = {}
    contact = 0
    if re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text): contact += 4
    if "linkedin.com" in low: contact += 3
    if "github.com" in low: contact += 3
    breakdown["Contact & Links"] = contact
    breakdown["Structure"] = min(sum(sections.get(x, False) for x in ["summary","education","experience","projects","skills"]) * 3, 15)
    breakdown["Skills"] = min(round(len(skills) * 1.5), 15)
    breakdown["Projects"] = 10 if sections["projects"] else 0
    breakdown["Experience"] = 10 if sections["experience"] else 0
    breakdown["Education"] = 10 if sections["education"] else 0
    breakdown["Achievements"] = 5 if sections["achievements"] else 0
    action_words = ["developed","built","designed","implemented","optimized","led","created","automated","improved","managed"]
    breakdown["Impact Language"] = min(sum(low.count(w) for w in action_words) * 2, 10)
    wc = len(text.split())
    breakdown["Readability"] = 5 if 350 <= wc <= 1000 else (3 if wc >= 180 else 0)
    breakdown["Career Targeting"] = 5 if role or company else 0
    score = min(round(sum(breakdown.values())), 100)
    match, matched, missing = job_match(text, job_description)
    strengths = []
    if len(skills) >= 8: strengths.append("Broad skill coverage detected.")
    if sections["projects"]: strengths.append("Projects section detected.")
    if sections["education"]: strengths.append("Education section detected.")
    if sections["experience"]: strengths.append("Experience or internship section detected.")
    if "linkedin.com" in low: strengths.append("LinkedIn profile detected.")
    if "github.com" in low: strengths.append("GitHub profile detected.")
    if not strengths: strengths.append("Resume text was successfully extracted.")
    weaknesses = [f"{name.title()} section may be missing." for name, present in sections.items() if not present]
    if len(skills) < 6: weaknesses.append("Limited recognizable skills detected.")
    if missing: weaknesses.append("Some target-job keywords are missing.")
    recommendations = ["Tailor your strongest projects and summary to each target role."]
    if not sections["summary"]: recommendations.append("Add a concise professional summary focused on your target role.")
    if not sections["projects"]: recommendations.append("Add 2–4 relevant projects with technologies and outcomes.")
    if not sections["experience"]: recommendations.append("Add internships or experience using action verbs and measurable results.")
    if len(skills) < 6: recommendations.append("Add relevant skills that you can genuinely demonstrate.")
    if missing: recommendations.append("Review missing job-description keywords and add only truthful skills.")
    if company: recommendations.append(f"Create a targeted resume version for {company}.")
    if role: recommendations.append(f"Place your strongest evidence for {role} near the top.")
    level = "Excellent" if score >= 85 else ("Strong" if score >= 70 else ("Developing" if score >= 50 else "Needs Improvement"))
    return {
        "score": score, "level": level, "breakdown": breakdown,
        "skills": skills, "skill_groups": skill_groups, "sections": sections,
        "job_match": match, "matched_keywords": matched, "missing_keywords": missing,
        "strengths": strengths[:6], "weaknesses": weaknesses[:7],
        "recommendations": recommendations[:7], "word_count": wc,
        "context": {"qualification": qualification, "degree": degree, "purpose": purpose, "company": company, "role": role}
    }
