from utils.skills_loader import load_skills


def test_load_skills_returns_list():
    skills = load_skills()

    assert isinstance(skills, list)


def test_skills_are_loaded():
    skills = load_skills()

    assert len(skills) > 0


def test_python_exists():
    skills = load_skills()

    assert "python" in skills


def test_sql_exists():
    skills = load_skills()

    assert "sql" in skills


def test_no_duplicates():
    skills = load_skills()

    assert len(skills) == len(set(skills))