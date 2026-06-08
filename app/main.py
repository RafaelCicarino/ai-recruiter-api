from fastapi import FastAPI
from app.core.config import settings
from app.database.session import Base, engine
from app.database import models
from app.api.routes.resume import router as resume_router
from app.api.routes.jobs import router as jobs_router
from app.api.routes.analysis import router as analysis_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0")

app.include_router(resume_router)
app.include_router(jobs_router)
app.include_router(analysis_router)


@app.get("/")
def health_check():
    return {"status": "online", "project": settings.PROJECT_NAME}
