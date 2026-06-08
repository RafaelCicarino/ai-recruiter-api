from app.utils.keyword_extractor import extract_technologies


def match_resume_to_job(resume_text: str, job_description: str) -> int:
    resume_techs = set(extract_technologies(resume_text))
    job_techs = set(extract_technologies(job_description))
    if not job_techs:
        return 0
    return int((len(resume_techs.intersection(job_techs)) / len(job_techs)) * 100)
