from groq import Groq

from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_candidate_summary(jd_data: dict, result: dict) -> str:
    """
    Generate an AI explanation for a ranked candidate.
    """

    missing_skills = ", ".join(result["missing_skills"])

    if not missing_skills:
        missing_skills = "None"

    prompt = f"""
    You are an experienced HR recruiter.

    A resume has already been evaluated using a deterministic NLP scoring system.

    Job Description Required Skills:
    {", ".join(jd_data["skills"])}

    Resume File:
    {result["resume_file"]}

    Matched Skills:
    {", ".join(result["matched_skills"])}

    Missing Skills:
    {missing_skills}

    Matched Skill Count:
    {result["matched_skill_count"]}/{result["required_skill_count"]}

    TF-IDF Similarity:
    {result["tfidf_score"]}

    Skill Match:
    {result["skill_score"]}

    Education Score:
    {result["education_score"]}

    Final Score:
    {result["final_score"]}

    Current Recommendation:
    {result["status"]}

    IMPORTANT:
    - Use ONLY the information provided.
    - Do NOT invent skills or experience.
    - Mention missing skills if appropriate.
    - Keep the explanation concise.

    Write exactly in this format:

    Strengths:
    - ...
    - ...

    Weakness:
    - ...

    Recommendation:
    ...
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content