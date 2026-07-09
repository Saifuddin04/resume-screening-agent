from pathlib import Path

from utils.llm import generate_candidate_summary
from utils.jd_parser import parse_job_description
from utils.pdf_parser import extract_text
from utils.text_cleaner import clean_text
from utils.scorer import score_resume
from utils.exporter import export_to_csv, export_to_json

JD_PATH = "job_description/jd.txt"
RESUME_FOLDER = "resumes"


def main():

    print("=" * 60)
    print("Resume Screening Agent")
    print("=" * 60)

    jd = parse_job_description(JD_PATH)

    if not jd:
        print("Failed to load Job Description.")
        return

    results = []

    supported_extensions = {".pdf", ".docx", ".txt"}

    for resume in Path(RESUME_FOLDER).iterdir():

        if resume.suffix.lower() not in supported_extensions:
            continue

        text = extract_text(str(resume))

        if not text:
            continue

        cleaned = clean_text(text)

        result = score_resume(
            jd,
            resume.name,
            cleaned
        )

        results.append(result)

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    print("\nGenerating AI explanations...\n")

    for candidate in results:

        explanation = generate_candidate_summary(
            jd,
            candidate
        )

        candidate["ai_summary"] = explanation

    print("\nRanked Candidates\n")

    for index, candidate in enumerate(results, start=1):

        # Save the rank so it also appears in the exported JSON/CSV
        candidate["rank"] = index

        print(f"\n{'=' * 70}")
        print(f"Rank #{index}")
        print(f"{'=' * 70}")

        print(f"Resume File        : {candidate['resume_file']}")
        print(f"Recommendation     : {candidate['status']}")
        print(f"Final Score        : {candidate['final_score']}")
        print(f"TF-IDF Score       : {candidate['tfidf_score']}")
        print(f"Skill Match        : {candidate['skill_score']}%")
        print(f"Education Score    : {candidate['education_score']}")

        print(
            f"Matched Skills ({candidate['matched_skill_count']}/{candidate['required_skill_count']}):"
        )
        print(", ".join(candidate["matched_skills"]))

        print("\nMissing Skills:")
        if candidate["missing_skills"]:
            print(", ".join(candidate["missing_skills"]))
        else:
            print("None")

        print("\nAI Evaluation:")
        print(candidate["ai_summary"])

        print(f"{'=' * 70}")

    export_to_csv(
        results,
        "output/ranked.csv"
    )

    export_to_json(
        results,
        "output/ranked.json"
    )

    print("=" * 60)
    print("Ranking Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()