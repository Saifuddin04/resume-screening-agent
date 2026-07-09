# 🤖 AI Resume Screening Agent

An AI-powered Resume Screening Agent that automatically ranks multiple resumes against a Job Description using Natural Language Processing (NLP), weighted scoring, and Large Language Model (LLM) reasoning.

Built as part of the **Rooman Technologies – Junior AI Research Associate 24-Hour AI Agent Challenge**.

---

# 📌 Project Overview

Recruiters often receive hundreds of resumes for a single job opening. Manually reviewing every resume is time-consuming and inconsistent.

This project automates the initial screening process by:

* Parsing resumes and job descriptions
* Extracting relevant technical skills
* Measuring semantic similarity using TF-IDF
* Computing weighted relevance scores
* Generating AI-powered hiring recommendations
* Exporting ranked results as CSV and JSON

The goal is **not to replace recruiters**, but to help them shortlist candidates faster and more consistently.

---

# ✨ Features

* 📄 Parse TXT, PDF and DOCX resumes
* 📋 Parse Job Descriptions
* 🧹 Automatic text cleaning and normalization
* 🧠 TF-IDF semantic similarity scoring
* ✅ Skill matching against the Job Description
* 🎓 Education scoring
* 📊 Weighted final ranking
* 🤖 AI-generated recruiter summaries using Groq Llama 3.3
* 📁 CSV export
* 📁 JSON export
* 📝 Application logging
* 💻 Command Line Interface (CLI)

---

# 🏗 System Architecture

```
                Job Description
                      │
                      ▼
               JD Parser & Cleaner
                      │
                      ▼
                 Resume Parser
                      │
                      ▼
                Text Normalization
                      │
                      ▼
         TF-IDF Similarity Calculation
                      │
                      ▼
              Skill Matching Engine
                      │
                      ▼
             Weighted Score Calculator
                      │
                      ▼
          Groq LLM Candidate Evaluation
                      │
                      ▼
         CSV + JSON Ranked Candidate List
```

---

# 📂 Project Structure

```
resume-screening-agent/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── job_description/
│   └── jd.txt
│
├── resumes/
│   ├── candidate1.txt
│   ├── candidate2.txt
│   └── candidate3.txt
│
├── output/
│   ├── ranked.csv
│   └── ranked.json
│
├── sample_data/
│
├── utils/
│   ├── exporter.py
│   ├── file_handler.py
│   ├── jd_parser.py
│   ├── llm.py
│   ├── logger.py
│   ├── pdf_parser.py
│   ├── scorer.py
│   └── text_cleaner.py
│
└── logs/
    └── app.log
```

---

# 🛠 Tech Stack

* Python 3.12
* Groq API
* Llama 3.3 70B Versatile
* scikit-learn
* Pandas
* PyMuPDF
* python-docx
* Flask *(installed for future UI support)*
* python-dotenv

---

# ⚙ Installation

Clone the repository:

```bash
git clone <repository-url>
cd resume-screening-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶ Running the Agent

```bash
python app.py
```

The agent will:

1. Read the Job Description
2. Read every resume in the `resumes/` folder
3. Compute TF-IDF similarity
4. Match required skills
5. Calculate education score
6. Compute the final weighted score
7. Generate an AI hiring summary
8. Export ranked results

---

# 📤 Outputs

The generated files are stored in the `output/` folder.

* `ranked.csv`
* `ranked.json`

The CLI also displays:

* Candidate ranking
* Recommendation
* Matched skills
* Missing skills
* AI-generated strengths
* AI-generated weakness
* Hiring recommendation

---

# 🧮 Scoring Methodology

The final score is calculated using a weighted approach:

| Component         | Weight |
| ----------------- | -----: |
| TF-IDF Similarity |    40% |
| Skill Match       |    40% |
| Education Score   |    20% |

This balances semantic relevance, explicit skill coverage, and educational qualifications.

---

# 🤖 AI Integration

The project uses the **Groq API** with the **Llama 3.3 70B Versatile** model.

The LLM is **not used to rank candidates**.

Instead, it explains the ranking by generating:

* Two candidate strengths
* One weakness
* A hiring recommendation

This keeps scoring deterministic while using AI for human-readable reasoning.

---

# ⚖ Trade-offs

Due to the 24-hour challenge timeline:

* TF-IDF was chosen instead of transformer embeddings for speed and simplicity.
* Skill extraction uses keyword matching instead of Named Entity Recognition (NER).
* Education scoring uses rule-based matching.
* The application is CLI-based to prioritize functionality and reproducibility.
* SQLite/database storage was intentionally omitted because it was unnecessary for the challenge requirements.

---

# 🚀 Future Improvements

Given more development time, the following enhancements would be added:

* HTML report generation
* Interactive dashboard
* Score visualizations and charts
* Sentence-transformer embeddings
* Semantic skill extraction
* Experience duration analysis
* Multi-page PDF support improvements
* Batch upload interface
* Flask or React web interface
* Recruiter feedback loop for score tuning

---

# 👨‍💻 Author

**Saifuddin Shariff**

Built for the **Rooman Technologies Junior AI Research Associate – 24-Hour AI Agent Challenge**.
