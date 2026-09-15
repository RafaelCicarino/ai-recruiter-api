from uuid import UUID


def test_create_job(client):
    payload = {
        "title": "Desenvolvedor Backend Python",
        "description": (
            "Procuramos profissional com experiência em Python, "
            "FastAPI, PostgreSQL e criação de APIs REST."
        ),
    }

    response = client.post("/job-description", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == payload["title"]
    assert UUID(data["job_id"])


def test_create_job_rejects_short_description(client):
    payload = {
        "title": "Desenvolvedor Python",
        "description": "Descrição curta",
    }

    response = client.post("/job-description", json=payload)

    assert response.status_code == 422