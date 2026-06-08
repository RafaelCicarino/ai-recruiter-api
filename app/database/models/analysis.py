import uuid
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from app.database.session import Base


class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    resume_id = Column(UUID(as_uuid=True), ForeignKey("resumes.id"), nullable=False)
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id"), nullable=False)
    ats_score = Column(Integer, nullable=False)
    compatibility_score = Column(Integer, nullable=False)
    level = Column(String(100), nullable=True)
    technologies = Column(JSONB, default=list)
    strengths = Column(JSONB, default=list)
    weaknesses = Column(JSONB, default=list)
    suggestions = Column(JSONB, default=list)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
