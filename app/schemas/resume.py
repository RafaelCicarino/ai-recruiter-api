from uuid import UUID
from pydantic import BaseModel


class ResumeResponse(BaseModel):
    resume_id: UUID
    filename: str
