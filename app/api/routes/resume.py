from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.database.models.resume import Resume
from app.services.pdf_parser import extract_text_from_pdf
from app.schemas.resume import ResumeResponse

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post("/upload", response_model=ResumeResponse)
async def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    text = await extract_text_from_pdf(file)

    resume = Resume(filename=file.filename or "resume.pdf", content=text)
    db.add(resume)
    db.commit()
    db.refresh(resume)

    return ResumeResponse(resume_id=resume.id, filename=resume.filename)
