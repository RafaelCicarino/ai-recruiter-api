from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.database.models.job import JobDescription
from app.schemas.job import JobCreate, JobResponse

router = APIRouter(tags=["Jobs"])


@router.post("/job-description", response_model=JobResponse)
def create_job(payload: JobCreate, db: Session = Depends(get_db)):
    job = JobDescription(title=payload.title, description=payload.description)
    db.add(job)
    db.commit()
    db.refresh(job)

    return JobResponse(job_id=job.id, title=job.title)
