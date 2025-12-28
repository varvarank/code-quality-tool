import sys
import os
# Добавляем корневую папку в путь, чтобы видеть пакет src
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.analyzer import CodeAnalyzer

def main():
    # Для примера анализируем этот же файл, если аргумент не передан
    target_file = sys.argv[1] if len(sys.argv) > 1 else "src/analyzer.py"
    
    analyzer = CodeAnalyzer()
    try:
        score = analyzer.analyze_file(target_file)
        report = analyzer.generate_report()
        print(report)
        
        # Сохраняем отчет в файл (для CI/CD артефактов)
        os.makedirs("reports", exist_ok=True)
        with open("reports/audit.txt", "w") as f:
            f.write(report)
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()