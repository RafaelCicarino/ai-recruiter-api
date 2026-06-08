RESUME_ANALYSIS_PROMPT = """
Você é um recrutador técnico sênior especializado em ATS.
Analise o currículo e a vaga abaixo.

Retorne SOMENTE um JSON válido com esta estrutura:
{
  "ats_score": 0,
  "compatibility_score": 0,
  "level": "Júnior | Pleno | Sênior | Especialista",
  "technologies": [],
  "strengths": [],
  "weaknesses": [],
  "suggestions": []
}

Critérios:
- ats_score: qualidade geral do currículo para sistemas ATS.
- compatibility_score: aderência do currículo à vaga.
- technologies: tecnologias identificadas no currículo.
- weaknesses: pontos fracos objetivos.
- suggestions: melhorias práticas.

CURRÍCULO:
{resume_text}

VAGA:
{job_description}
"""
