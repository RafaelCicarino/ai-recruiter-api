# AI Recruiter API

API profissional para análise de currículos com FastAPI, OpenAI, PDFPlumber e PostgreSQL.

## Funcionalidades

- Upload de currículo em PDF
- Extração de texto com PDFPlumber
- Cadastro de descrição de vaga
- Score ATS
- Tecnologias encontradas
- Pontos fortes
- Pontos fracos
- Sugestões de melhoria
- Compatibilidade com a vaga

## Tecnologias

- Python
- FastAPI
- OpenAI
- PDFPlumber
- PostgreSQL
- SQLAlchemy
- Docker

## Como rodar com Docker

Copie o arquivo de ambiente:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e coloque sua chave da OpenAI:

```env
OPENAI_API_KEY=sua_chave_aqui
```

Suba o projeto:

```bash
docker compose up --build
```

Acesse:

```text
http://localhost:8000/docs
```

## Como rodar localmente sem Docker

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure o `.env` com um PostgreSQL local:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ai_recruiter
```

Rode:

```bash
uvicorn app.main:app --reload
```

## Endpoints

### Upload de currículo

```http
POST /resume/upload
```

Envie um arquivo PDF no campo `file`.

Resposta:

```json
{
  "resume_id": "uuid",
  "filename": "curriculo.pdf"
}
```

### Cadastro da vaga

```http
POST /job-description
```

Body:

```json
{
  "title": "Desenvolvedor Backend Python",
  "description": "Experiência com Python, FastAPI, Docker e PostgreSQL..."
}
```

Resposta:

```json
{
  "job_id": "uuid",
  "title": "Desenvolvedor Backend Python"
}
```

### Gerar análise

```http
POST /analysis
```

Body:

```json
{
  "resume_id": "uuid",
  "job_id": "uuid"
}
```

Resposta:

```json
{
  "analysis_id": "uuid",
  "ats_score": 85,
  "compatibility_score": 72,
  "level": "Pleno",
  "technologies": ["Python", "FastAPI", "PostgreSQL"],
  "strengths": [],
  "weaknesses": [],
  "suggestions": []
}
```

### Consultar score

```http
GET /score/{analysis_id}
```

## Observação importante

Se `OPENAI_API_KEY` não estiver configurada, a API ainda funciona usando uma análise local básica.
