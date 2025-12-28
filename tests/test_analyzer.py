import pytest
from src.analyzer import CodeAnalyzer


# Создаем временный файл для теста
@pytest.fixture
def sample_file(tmp_path):
    d = tmp_path / "subdir"
    d.mkdir()
    p = d / "test_code.py"
    p.write_text("def hello():\n    '''Doc'''\n    pass\n\ndef no_doc():\n    pass")
    return str(p)


def test_analyze_file(sample_file):
    analyzer = CodeAnalyzer()
    analyzer.analyze_file(sample_file)
    assert analyzer.metrics["functions_count"] == 2
    assert analyzer.metrics["lines_of_code"] >= 4
    assert analyzer.metrics["docstrings_count"] == 1


def test_score_logic(sample_file):
    analyzer = CodeAnalyzer()
    analyzer.analyze_file(sample_file)
    score = analyzer.get_score()
    assert score <= 100
    assert score >= 0
