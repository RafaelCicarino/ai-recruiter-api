from uuid import UUID
from pydantic import BaseModel


class AnalysisCreate(BaseModel):
    resume_id: UUID
    job_id: UUID


class AnalysisResponse(BaseModel):
    analysis_id: UUID
    ats_score: int
    compatibility_score: int
    level: str | None = None
    technologies: list[str]
    strengths: list[str]
    weaknesses: list[str]
    suggestions: list[str]
