import uuid

from sqlalchemy import (
    JSON,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Uuid,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from app.database.session import Base


json_type = JSON().with_variant(JSONB(), "postgresql")


class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    resume_id = Column(
        Uuid(as_uuid=True),
        ForeignKey("resumes.id"),
        nullable=False,
    )
    job_id = Column(
        Uuid(as_uuid=True),
        ForeignKey("jobs.id"),
        nullable=False,
    )
    ats_score = Column(Integer, nullable=False)
    compatibility_score = Column(Integer, nullable=False)
    level = Column(String(100), nullable=True)
    technologies = Column(json_type, default=list)
    strengths = Column(json_type, default=list)
    weaknesses = Column(json_type, default=list)
    suggestions = Column(json_type, default=list)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )