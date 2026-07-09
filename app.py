from pathlib import Path

from utils.llm import generate_candidate_summary
from utils.jd_parser import parse_job_description
from utils.resume_parser import parse_resume
from utils.pdf_parser import extract_text
from utils.text_cleaner import clean_text
from utils.scorer import score_resume
from utils.exporter import (
    export_to_csv,
    export_to_json,
    export_to_html,
)

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

        # Parse resume into structured data
        resume_data = parse_resume(cleaned)

        result = score_resume(
            jd,
            resume.name,
            resume_data,
        )

        results.append(result)

    if not results:
        print("No valid resumes found.")
        return

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    print("\nGenerating AI explanations...\n")

    for candidate in results:

        candidate["ai_summary"] = generate_candidate_summary(
            jd,
            candidate
        )

    print("\nRanked Candidates\n")

    for index, candidate in enumerate(results, start=1):

        candidate["rank"] = index

        print("\n" + "=" * 70)
        print(f"Rank #{index}")
        print("=" * 70)

        print(f"Resume File        : {candidate['resume_file']}")
        print(f"Recommendation     : {candidate['status']}")
        print(f"Final Score        : {candidate['final_score']}")
        print(f"TF-IDF Score       : {candidate['tfidf_score']}")
        print(f"Skill Match        : {candidate['skill_score']}%")
        print(f"Education Score    : {candidate['education_score']}")

        print(
            f"Matched Skills ({candidate['matched_skill_count']}/{candidate['required_skill_count']}):"
        )

        if candidate["matched_skills"]:
            print(", ".join(candidate["matched_skills"]))
        else:
            print("None")

        print("\nMissing Skills:")

        if candidate["missing_skills"]:
            print(", ".join(candidate["missing_skills"]))
        else:
            print("None")

        print("\nAI Evaluation:")
        print(candidate["ai_summary"])

        print("=" * 70)

    # ==========================================================
    # Screening Summary
    # ==========================================================

    total_candidates = len(results)

    highly_recommended = sum(
        1
        for c in results
        if c["status"] == "Highly Recommended"
    )

    recommended = sum(
        1
        for c in results
        if c["status"] == "Recommended"
    )

    consider = sum(
        1
        for c in results
        if c["status"] == "Consider"
    )

    not_recommended = sum(
        1
        for c in results
        if c["status"] == "Not Recommended"
    )

    average_score = round(
        sum(c["final_score"] for c in results)
        / total_candidates,
        2,
    )

    highest_score = max(
        c["final_score"]
        for c in results
    )

    lowest_score = min(
        c["final_score"]
        for c in results
    )

    print("\n")
    print("=" * 70)
    print("SCREENING SUMMARY")
    print("=" * 70)

    print(f"Total Candidates      : {total_candidates}")
    print(f"Highly Recommended    : {highly_recommended}")
    print(f"Recommended           : {recommended}")
    print(f"Consider              : {consider}")
    print(f"Not Recommended       : {not_recommended}")
    print(f"Average Score         : {average_score}")
    print(f"Highest Score         : {highest_score}")
    print(f"Lowest Score          : {lowest_score}")

    print("=" * 70)

    # ==========================================================
    # Export Results
    # ==========================================================

    export_to_csv(
        results,
        "output/ranked.csv"
    )

    export_to_json(
        results,
        "output/ranked.json"
    )

    export_to_html(
        results,
        "output/report.html"
    )

    print("\nGenerated Files")

    print("✓ output/ranked.csv")
    print("✓ output/ranked.json")
    print("✓ output/report.html")

    print("\n" + "=" * 60)
    print("Ranking Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()