from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.database.session import get_db
from app.database.models.resume import Resume
from app.database.models.job import JobDescription
from app.database.models.analysis import Analysis
from app.schemas.analysis import AnalysisCreate, AnalysisResponse
from app.services.ai_service import AIService
from app.services.report_service import build_report_payload

router = APIRouter(tags=["Analysis"])


@router.post("/analysis", response_model=AnalysisResponse)
def analyze_resume(payload: AnalysisCreate, db: Session = Depends(get_db)):
    resume = db.get(Resume, payload.resume_id)
    if not resume:
        raise HTTPException(status_code=404, detail="Currículo não encontrado.")

    job = db.get(JobDescription, payload.job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Vaga não encontrada.")

    ai_service = AIService()
    result = ai_service.analyze_resume(resume.content, job.description)

    analysis = Analysis(
        resume_id=resume.id,
        job_id=job.id,
        ats_score=result["ats_score"],
        compatibility_score=result["compatibility_score"],
        level=result.get("level"),
        technologies=result.get("technologies", []),
        strengths=result.get("strengths", []),
        weaknesses=result.get("weaknesses", []),
        suggestions=result.get("suggestions", []),
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return build_report_payload(analysis)


@router.get("/score/{analysis_id}", response_model=AnalysisResponse)
def get_score(analysis_id: UUID, db: Session = Depends(get_db)):
    analysis = db.get(Analysis, analysis_id)
    if not analysis:
        raise HTTPException(status_code=404, detail="Análise não encontrada.")

    return build_report_payload(analysis)
