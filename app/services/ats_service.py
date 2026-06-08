from app.utils.keyword_extractor import extract_technologies


def calculate_basic_ats_score(resume_text: str, job_description: str) -> dict:
    resume_techs = extract_technologies(resume_text)
    job_techs = extract_technologies(job_description)

    matched = set(resume_techs).intersection(set(job_techs))
    compatibility = int((len(matched) / len(job_techs)) * 100) if job_techs else 0

    score = 40
    if len(resume_text) > 1200:
        score += 15
    if resume_techs:
        score += min(len(resume_techs) * 3, 20)
    if "experiência" in resume_text.lower() or "experience" in resume_text.lower():
        score += 10
    if "projeto" in resume_text.lower() or "project" in resume_text.lower():
        score += 10
    if "certificação" in resume_text.lower() or "certification" in resume_text.lower():
        score += 5

    return {
        "ats_score": min(score, 100),
        "compatibility_score": min(compatibility, 100),
        "technologies": resume_techs,
    }
