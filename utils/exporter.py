"""
exporter.py

Exports ranked resume results to:
1. CSV
2. JSON
3. Professional HTML Report
"""

import json
from datetime import datetime

import pandas as pd

from utils.logger import logger


def export_to_csv(results: list, output_path: str):
    """
    Export ranked results to CSV.
    """

    try:
        df = pd.DataFrame(results)
        df.to_csv(output_path, index=False)

        logger.info(f"CSV exported to {output_path}")

    except Exception as e:
        logger.error(f"CSV export failed: {e}")


def export_to_json(results: list, output_path: str):
    """
    Export ranked results to JSON.
    """

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(results, file, indent=4)

        logger.info(f"JSON exported to {output_path}")

    except Exception as e:
        logger.error(f"JSON export failed: {e}")


def export_to_html(results: list, output_path: str):
    """
    Generate HTML recruiter report using an external template.
    """

    try:

        total = len(results)

        recommended = sum(
            1 for r in results
            if r["status"] == "Recommended"
        )

        consider = sum(
            1 for r in results
            if r["status"] == "Consider"
        )

        rejected = sum(
            1 for r in results
            if r["status"] == "Not Recommended"
        )

        average = round(
            sum(r["final_score"] for r in results) / total,
            2
        )

        with open(
            "templates/report_template.html",
            "r",
            encoding="utf-8"
        ) as file:

            html = file.read()

        summary = f"""
<div class="card">
<h2>{total}</h2>
<p>Total Candidates</p>
</div>

<div class="card">
<h2>{recommended}</h2>
<p>Recommended</p>
</div>

<div class="card">
<h2>{consider}</h2>
<p>Consider</p>
</div>

<div class="card">
<h2>{rejected}</h2>
<p>Rejected</p>
</div>

<div class="card">
<h2>{average}</h2>
<p>Average Score</p>
</div>
"""

        candidate_html = ""

        for candidate in results:

            if candidate["status"] == "Recommended":
                badge = "good"

            elif candidate["status"] == "Consider":
                badge = "medium"

            else:
                badge = "bad"

            missing = ", ".join(candidate["missing_skills"])

            if not missing:
                missing = "None"

            candidate_html += f"""
<div class="candidate">

<h2>
Rank #{candidate["rank"]} - {candidate["resume_file"]}
</h2>

<p class="{badge}">
{candidate["status"]}
</p>

<ul>

<li><b>Final Score:</b> {candidate["final_score"]}</li>

<li><b>TF-IDF Score:</b> {candidate["tfidf_score"]}</li>

<li><b>Skill Match:</b> {candidate["skill_score"]}%</li>

<li><b>Education Score:</b> {candidate["education_score"]}</li>

</ul>

<h3>Matched Skills</h3>

<p>
{", ".join(candidate["matched_skills"])}
</p>

<h3>Missing Skills</h3>

<p>
{missing}
</p>

<h3>AI Evaluation</h3>

<pre>{candidate["ai_summary"]}</pre>

</div>
"""

        html = html.replace(
            "{{GENERATED_DATE}}",
            datetime.now().strftime("%d %B %Y %I:%M %p")
        )

        html = html.replace(
            "{{SUMMARY}}",
            summary
        )

        html = html.replace(
            "{{CANDIDATES}}",
            candidate_html
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)

        logger.info(f"HTML report exported to {output_path}")

    except Exception as e:

        logger.error(f"HTML export failed: {e}")