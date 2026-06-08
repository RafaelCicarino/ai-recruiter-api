def build_report_payload(analysis) -> dict:
    return {
        "analysis_id": analysis.id,
        "ats_score": analysis.ats_score,
        "compatibility_score": analysis.compatibility_score,
        "level": analysis.level,
        "technologies": analysis.technologies or [],
        "strengths": analysis.strengths or [],
        "weaknesses": analysis.weaknesses or [],
        "suggestions": analysis.suggestions or [],
    }
