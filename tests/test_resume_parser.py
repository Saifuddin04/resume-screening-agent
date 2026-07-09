from utils.resume_parser import parse_resume


def test_resume_parser_returns_dict():
    resume = parse_resume(
        "Python SQL Machine Learning Bachelor"
    )

    assert isinstance(resume, dict)


def test_extract_python():
    resume = parse_resume(
        "Experienced Python Developer"
    )

    assert "python" in resume["skills"]


def test_extract_sql():
    resume = parse_resume(
        "Worked extensively with SQL databases."
    )

    assert "sql" in resume["skills"]


def test_extract_multiple_skills():
    resume = parse_resume(
        "Python SQL Docker AWS"
    )

    assert len(resume["skills"]) >= 4


def test_extract_education():
    resume = parse_resume(
        "Bachelor of Engineering in Computer Science"
    )

    assert resume["education"] == "bachelor"