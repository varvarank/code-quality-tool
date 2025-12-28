import ast
import os


class CodeAnalyzer:
    def __init__(self):
        self.metrics = {
            "functions_count": 0,
            "classes_count": 0,
            "docstrings_count": 0,
            "lines_of_code": 0
        }

    def analyze_file(self, file_path):
        """Анализирует один файл Python."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found")

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.metrics["lines_of_code"] = len(content.splitlines())

        tree = ast.parse(content)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                self.metrics["functions_count"] += 1
                if ast.get_docstring(node):
                    self.metrics["docstrings_count"] += 1
            elif isinstance(node, ast.ClassDef):
                self.metrics["classes_count"] += 1

        return self.get_score()

    def get_score(self):
        """Вычисляет оценку качества кода (0-100)."""
        score = 100
        # Штраф за отсутствие докстрингов
        if self.metrics["functions_count"] > 0:
            doc_ratio = self.metrics["docstrings_count"] / self.metrics["functions_count"]
            if doc_ratio < 0.5:
                score -= 20

        # Штраф за слишком большие файлы
        if self.metrics["lines_of_code"] > 200:
            score -= 10

        return max(0, score)

    def generate_report(self):
        return (f"--- Code Report ---\n"
                f"Functions: {self.metrics['functions_count']}\n"
                f"Docstrings: {self.metrics['docstrings_count']}\n"
                f"Lines: {self.metrics['lines_of_code']}\n"
                f"Final Score: {self.get_score()}/100")
