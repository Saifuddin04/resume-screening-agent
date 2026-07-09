"""
scorer.py

Computes resume relevance scores against a job description.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_tfidf_similarity(jd_text: str, resume_text: str) -> float:
    """
    Compute cosine similarity between JD and Resume using TF-IDF.

    Returns:
        Similarity score (0–100)
    """

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform([jd_text, resume_text])

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(float(similarity * 100), 2)


def compute_skill_match(jd_skills: list, resume_text: str):
    """
    Compute percentage of required skills found in resume.
    """

    if not jd_skills:
        return 0.0, []

    matched = []

    resume_lower = resume_text.lower()

    for skill in jd_skills:
        if skill in resume_lower:
            matched.append(skill)

    percentage = (len(matched) / len(jd_skills)) * 100

    return round(percentage, 2), matched


def compute_education_score(jd_education: str, resume_text: str):
    """
    Simple education match.
    """

    if not jd_education:
        return 100

    return 100 if jd_education in resume_text.lower() else 0


def compute_final_score(
    tfidf_score,
    skill_score,
    education_score
):
    """
    Weighted final score.
    """

    final = (
        tfidf_score * 0.60 +
        skill_score * 0.30 +
        education_score * 0.10
    )

    return round(float(final), 2)

def score_resume(jd_data: dict, resume_name: str, resume_text: str) -> dict:
    """
    Score a single resume against the job description.
    """

    tfidf = compute_tfidf_similarity(
        jd_data["clean_text"],
        resume_text
    )

    skill_score, matched = compute_skill_match(
        jd_data["skills"],
        resume_text
    )

    education = compute_education_score(
        jd_data["education"],
        resume_text
    )

    final = compute_final_score(
        tfidf,
        skill_score,
        education
    )

    # Calculate missing skills
    missing = list(set(jd_data["skills"]) - set(matched))

    # Decide recommendation status
    if final >= 75:
        status = "Highly Recommended"
    elif final >= 60:
        status = "Recommended"
    elif final >= 40:
        status = "Consider"
    else:
        status = "Not Recommended"

    return {
        "resume_file": resume_name,
        "tfidf_score": tfidf,
        "skill_score": skill_score,
        "education_score": education,
        "matched_skills": matched,
        "missing_skills": missing,
        "matched_skill_count": len(matched),
        "required_skill_count": len(jd_data["skills"]),
        "final_score": final,
        "status": status,
    }