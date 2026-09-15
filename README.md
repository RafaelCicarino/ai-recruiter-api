# AI Recruiter API

[![Testes da API](https://github.com/RafaelCicarino/ai-recruiter-api/actions/workflows/test.yml/badge.svg)](https://github.com/RafaelCicarino/ai-recruiter-api/actions/workflows/test.yml)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)

API REST para análise de currículos e comparação com vagas. O sistema recebe um currículo em PDF, extrai seu conteúdo, identifica tecnologias e gera indicadores como score ATS, compatibilidade, pontos fortes, pontos de melhoria e sugestões para o candidato.

O projeto foi desenvolvido com foco em arquitetura organizada, validação de dados, persistência, testes automatizados e execução com Docker.

## Documentação interativa

A API disponibiliza documentação automática com Swagger para explorar e testar todos os endpoints.

![Documentação Swagger da AI Recruiter API](docs/swagger-api.png)

## Problema resolvido

Analisar currículos manualmente e comparar cada candidato com os requisitos de uma vaga consome tempo e dificulta a padronização do processo seletivo.

A AI Recruiter API organiza esse fluxo em três etapas:

1. envio e processamento do currículo;
2. cadastro da descrição da vaga;
3. geração de uma análise estruturada de compatibilidade.

## Funcionalidades

- Upload de currículo em PDF
- Extração de texto com PDFPlumber
- Cadastro e validação da descrição da vaga
- Cálculo de score ATS
- Cálculo de compatibilidade entre currículo e vaga
- Identificação de tecnologias
- Indicação de pontos fortes e pontos fracos
- Sugestões de melhoria
- Classificação do nível profissional
- Persistência das informações no PostgreSQL
- Consulta de análises realizadas
- Documentação interativa com Swagger
- Análise local básica quando a API da OpenAI não estiver configurada
- Testes automatizados com Pytest
- Integração contínua com GitHub Actions

## Tecnologias

- Python 3.12
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- OpenAI API
- PDFPlumber
- Pytest
- Docker e Docker Compose
- GitHub Actions

## Arquitetura

```text
app/
├── api/
│   ├── dependencies/     # Dependências compartilhadas pelas rotas
│   └── routes/           # Endpoints de currículos, vagas e análises
├── core/                 # Configurações, segurança e prompts
├── database/
│   ├── models/           # Modelos SQLAlchemy
│   └── session.py        # Conexão e sessões do banco
├── schemas/              # Schemas de entrada e saída
├── services/             # Regras de negócio e integração com IA
├── utils/                # Limpeza e extração de informações
└── main.py               # Inicialização da aplicação

tests/
├── conftest.py           # Configuração isolada dos testes
├── test_health.py        # Teste de disponibilidade da API
└── test_jobs.py          # Testes do cadastro de vagas
```

Essa separação reduz o acoplamento entre rotas, regras de negócio, persistência e serviços externos, facilitando testes e evolução do projeto.

## Como executar com Docker

### 1. Clone o repositório

```bash
git clone https://github.com/RafaelCicarino/ai-recruiter-api.git
cd ai-recruiter-api
```

### 2. Crie o arquivo de ambiente

No Windows:

```powershell
Copy-Item .env.example .env
```

No Linux ou macOS:

```bash
cp .env.example .env
```

Revise as variáveis do `.env` antes de iniciar a aplicação.

### 3. Suba os serviços

```bash
docker compose up --build
```

### 4. Acesse a documentação

- Swagger: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Health check: http://localhost:8000/

## Como executar localmente

### 1. Crie o ambiente virtual com Python 3.12

```bash
python -m venv .venv
```

### 2. Ative o ambiente

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux ou macOS:

```bash
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Configure o banco

Defina a conexão com o PostgreSQL no `.env`:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/ai_recruiter
```

### 5. Inicie a API

```bash
python -m uvicorn app.main:app --reload
```

## Endpoints principais

| Método | Endpoint | Finalidade |
|---|---|---|
| `GET` | `/` | Verificar se a API está online |
| `POST` | `/resume/upload` | Enviar currículo em PDF |
| `POST` | `/job-description` | Cadastrar uma vaga |
| `POST` | `/analysis` | Analisar a compatibilidade |
| `GET` | `/score/{analysis_id}` | Consultar uma análise |

## Exemplos de uso

### Cadastrar uma vaga

```http
POST /job-description
Content-Type: application/json
```

```json
{
  "title": "Desenvolvedor Backend Python",
  "description": "Buscamos profissional com experiência em Python, FastAPI, PostgreSQL, Docker e desenvolvimento de APIs REST."
}
```

Resposta esperada:

```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Desenvolvedor Backend Python"
}
```

### Gerar uma análise

```http
POST /analysis
Content-Type: application/json
```

```json
{
  "resume_id": "550e8400-e29b-41d4-a716-446655440000",
  "job_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
}
```

Exemplo de resposta:

```json
{
  "analysis_id": "7d444840-9dc0-11d1-b245-5ffdce74fad2",
  "ats_score": 85,
  "compatibility_score": 72,
  "level": "Pleno",
  "technologies": ["Python", "FastAPI", "PostgreSQL"],
  "strengths": [],
  "weaknesses": [],
  "suggestions": []
}
```

## Testes automatizados

Os testes utilizam SQLite como banco isolado, sem depender de uma instância local do PostgreSQL.

Execute:

```bash
python -m pytest -v
```

Atualmente são validados:

- disponibilidade da API;
- cadastro de uma vaga válida;
- rejeição de descrições que não atendem às regras de validação.

O workflow do GitHub Actions executa a suíte automaticamente em cada `push` e `pull request` direcionado à branch `main`.

## Segurança

- Credenciais são configuradas por variáveis de ambiente.
- O arquivo `.env` não é versionado.
- O repositório mantém somente um `.env.example` sem valores privados.
- Arquivos enviados, bancos locais, logs e ambientes virtuais são ignorados pelo Git.

## Próximas melhorias

- Ampliar os testes dos endpoints de currículo e análise
- Adicionar migrations com Alembic
- Implementar autenticação completa da API
- Publicar uma demonstração online
- Adicionar captura de tela do Swagger
- Criar versionamento dos endpoints
- Adicionar observabilidade e logs estruturados

## Autor

Desenvolvido por **Rafael Cicarino**.

- [GitHub](https://github.com/RafaelCicarino)
- [LinkedIn](https://www.linkedin.com/in/rafaelcicarino/)
