import sys
import os

# Добавляем путь в начало, чтобы избежать E402
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.analyzer import CodeAnalyzer  # noqa: E402


def main():
    # Для примера анализируем этот же файл
    target_file = sys.argv[1] if len(sys.argv) > 1 else "src/analyzer.py"

    analyzer = CodeAnalyzer()
    try:
        analyzer.analyze_file(target_file)
        report = analyzer.generate_report()
        print(report)

        # Сохраняем отчет в файл
        os.makedirs("reports", exist_ok=True)
        with open("reports/audit.txt", "w") as f:
            f.write(report)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
