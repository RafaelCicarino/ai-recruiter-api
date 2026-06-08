TECH_STACK = [
    "Python", "Java", "JavaScript", "TypeScript", "React", "Next.js",
    "Node.js", "FastAPI", "Django", "Flask", "Docker", "Kubernetes",
    "AWS", "Azure", "GCP", "PostgreSQL", "MySQL", "Redis", "MongoDB",
    "SQL", "Git", "Linux", "Pandas", "NumPy", "Machine Learning"
]


def extract_technologies(text: str) -> list[str]:
    found = []
    normalized = text.lower()
    for tech in TECH_STACK:
        if tech.lower() in normalized:
            found.append(tech)
    return sorted(set(found))
