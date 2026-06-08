from uuid import UUID
from pydantic import BaseModel, Field


class JobCreate(BaseModel):
    title: str = Field(..., min_length=3)
    description: str = Field(..., min_length=20)


class JobResponse(BaseModel):
    job_id: UUID
    title: str
