# 🤖 AI Resume Screening Agent

An AI-powered Applicant Tracking System (ATS) that automatically screens, scores, and ranks multiple resumes against a Job Description using Natural Language Processing (NLP), skill matching, weighted scoring, and Large Language Model (LLM) reasoning.

Built for the **Rooman Technologies – Junior AI Research Associate AI Agent Challenge**.

---

# 🚀 Project Overview

Recruiters often receive hundreds of resumes for a single job opening. Manually reviewing every resume is slow, repetitive, and inconsistent.

This project automates the initial screening process by:

- Parsing resumes (PDF, DOCX, TXT)
- Parsing job descriptions
- Extracting technical skills
- Computing semantic similarity using TF-IDF
- Matching candidate skills against job requirements
- Calculating weighted ATS scores
- Generating AI-powered recruiter summaries
- Ranking all candidates automatically
- Exporting professional reports

The objective is **not to replace recruiters**, but to help them shortlist candidates faster and more consistently.

---

# ✨ Features

## Resume Processing

- ✅ PDF Resume Parsing
- ✅ DOCX Resume Parsing
- ✅ TXT Resume Parsing
- ✅ Automatic Text Cleaning

---

## Job Description Processing

- ✅ Job Description Parsing
- ✅ Dynamic Skill Extraction
- ✅ Education Detection
- ✅ Keyword Matching

---

## ATS Scoring Engine

- ✅ TF-IDF Semantic Similarity
- ✅ Dynamic Skill Matching
- ✅ Education Score
- ✅ Weighted Final Score
- ✅ Candidate Ranking

---

## AI Features

- ✅ AI-generated Candidate Summary
- ✅ Strengths Identification
- ✅ Weakness Detection
- ✅ Hiring Recommendation

Powered by **Groq Llama 3.3 70B**.

---

## Reports

- ✅ CSV Export
- ✅ JSON Export
- ✅ HTML Report

---

## Engineering Features

- ✅ Modular Project Structure
- ✅ Logging
- ✅ Dynamic Skills Database
- ✅ Unit Tests (Pytest)
- ✅ Git Version Control

---

# 🏗 System Architecture

```
                     Job Description
                            │
                            ▼
                   Job Description Parser
                            │
                            ▼
                  Dynamic Skill Extraction
                            │
                            ▼
                     Resume Parser
                            │
                            ▼
                  Text Normalization
                            │
                            ▼
               TF-IDF Similarity Engine
                            │
                            ▼
                  Skill Matching Engine
                            │
                            ▼
                Weighted ATS Score Engine
                            │
                            ▼
              AI Candidate Evaluation
                            │
                            ▼
               Ranked Candidate Reports
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
├── pytest.ini
│
├── job_description/
│   └── jd.txt
│
├── resumes/
│   ├── *.pdf
│   ├── *.docx
│   └── *.txt
│
├── output/
│   ├── ranked.csv
│   ├── ranked.json
│   └── report.html
│
├── sample_data/
│   └── skills.txt
│
├── tests/
│   ├── test_resume_parser.py
│   └── test_skills_loader.py
│
├── utils/
│   ├── __init__.py
│   ├── exporter.py
│   ├── jd_parser.py
│   ├── llm.py
│   ├── logger.py
│   ├── pdf_parser.py
│   ├── resume_parser.py
│   ├── scorer.py
│   ├── skills_loader.py
│   └── text_cleaner.py
│
└── logs/
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3 |
| AI | Groq Llama 3.3 |
| NLP | TF-IDF |
| ML | Scikit-Learn |
| PDF Parsing | PyMuPDF |
| DOCX Parsing | python-docx |
| Data Handling | Pandas |
| Testing | Pytest |

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/resume-screening-agent.git

cd resume-screening-agent
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create a `.env`

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# ▶ Running

```bash
python app.py
```

The application will

1. Parse the Job Description
2. Parse every resume
3. Clean the text
4. Extract required skills
5. Compute TF-IDF similarity
6. Match candidate skills
7. Calculate weighted ATS scores
8. Generate AI explanations
9. Rank all candidates
10. Export reports

---

# 🧪 Running Tests

Run all unit tests

```bash
pytest
```

Example

```
=========================
10 passed in 0.06s
=========================
```

---

# 📊 Scoring Methodology

The ATS score combines three components:

| Component | Weight |
|-----------|--------|
| TF-IDF Similarity | 50% |
| Skill Match | 35% |
| Education Match | 15% |

The weighted score determines the final candidate ranking.

---

# 📤 Output

The application generates

```
output/
│
├── ranked.csv
├── ranked.json
└── report.html
```

The terminal displays

- Candidate Rank
- Final Score
- TF-IDF Score
- Skill Match
- Matched Skills
- Missing Skills
- AI Evaluation
- Hiring Recommendation

---

# 🧠 AI Integration

This project integrates the **Groq API** using the **Llama 3.3 70B** model.

The LLM is **not responsible for scoring candidates**.

Instead, it provides human-readable explanations including:

- Candidate strengths
- Candidate weaknesses
- Hiring recommendation

This keeps the ATS scoring deterministic while using AI for explainability.

---

# 📈 Future Improvements

- Interactive Recruiter Dashboard
- Resume Upload UI
- Sentence Transformer Embeddings
- Semantic Skill Matching
- Experience Analysis
- Recruiter Feedback Loop
- GitHub Actions CI/CD
- Docker Support
- REST API
- Flask / React Web Interface

---

# 📸 Screenshots

### Terminal Output

> *(Add screenshot here)*

---

### HTML Report

> *(Add screenshot here)*

---

### Ranked Candidates

> *(Add screenshot here)*

---

# 👨‍💻 Author

**Saifuddin Shariff**

AI Resume Screening Agent

Built for the **Rooman Technologies – Junior AI Research Associate AI Agent Challenge**.

---

# ⭐ Acknowledgements

This project was developed to demonstrate practical skills in:

- Artificial Intelligence
- Natural Language Processing
- Python Software Development
- Resume Screening Automation
- Applicant Tracking Systems
- Prompt Engineering
- Software Testing
- Modular Software Architecture