from pathlib import Path

from utils.pdf_parser import extract_text
from utils.text_cleaner import clean_text
from utils.logger import logger


COMMON_SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "flask",
    "django",
    "react",
    "javascript",
    "docker",
    "git",
    "aws",
    "azure",
    "mongodb",
    "mysql",
    "machine learning",
    "deep learning",
    "data analysis",
    "pandas",
    "numpy",
    "rest api",
]


def parse_job_description(file_path: str) -> dict:
    """
    Read and analyze a job description.

    Returns:
        Dictionary containing cleaned text and extracted skills.
    """

    if not Path(file_path).exists():
        logger.error(f"Job Description not found: {file_path}")
        return {}

    raw_text = extract_text(file_path)
    clean = clean_text(raw_text)

    detected_skills = []

    for skill in COMMON_SKILLS:
        if skill in clean:
            detected_skills.append(skill)

    logger.info(f"Detected {len(detected_skills)} skills.")

    return {
        "raw_text": raw_text,
        "clean_text": clean,
        "skills": detected_skills,
        "education": "bachelor" if "bachelor" in clean else "",
    }