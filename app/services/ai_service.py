import json
from openai import OpenAI
from app.core.config import settings
from app.core.prompts import RESUME_ANALYSIS_PROMPT
from app.services.ats_service import calculate_basic_ats_score


class AIService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY) if settings.OPENAI_API_KEY else None

    def analyze_resume(self, resume_text: str, job_description: str) -> dict:
        fallback = calculate_basic_ats_score(resume_text, job_description)

        if not self.client:
            return {
                **fallback,
                "level": "Não identificado",
                "strengths": ["Análise local executada sem OpenAI."],
                "weaknesses": ["Configure OPENAI_API_KEY para uma análise mais completa."],
                "suggestions": ["Adicione uma chave da OpenAI no arquivo .env."],
            }

        prompt = RESUME_ANALYSIS_PROMPT.format(
            resume_text=resume_text[:12000],
            job_description=job_description[:6000],
        )

        response = self.client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "Você responde somente JSON válido."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )

        content = response.choices[0].message.content or "{}"
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            data = fallback

        return {
            "ats_score": int(data.get("ats_score", fallback["ats_score"])),
            "compatibility_score": int(data.get("compatibility_score", fallback["compatibility_score"])),
            "level": data.get("level", "Não identificado"),
            "technologies": data.get("technologies", fallback["technologies"]),
            "strengths": data.get("strengths", []),
            "weaknesses": data.get("weaknesses", []),
            "suggestions": data.get("suggestions", []),
        }
