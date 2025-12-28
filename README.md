# Code Quality Assessment Tool

[![Build Status](https://github.com/varvarank/code-quality-tool/actions/workflows/audit.yml/badge.svg)](https://github.com/varvarank/code-quality-tool/actions)

## Описание
Инструмент для автоматического анализа качества Python-кода. Предназначен для образовательных целей, чтобы быстро оценивать наличие документации и сложность кода студентов.

## Функционал
- Подсчет количества функций и классов.
- Проверка наличия Docstrings.
- Расчет итоговой оценки (0-100).
- Генерация отчетов.

## Структура проекта
- `src/` - Исходный код анализатора.
- `tests/` - Unit-тесты.
- `.github/workflows/` - CI/CD пайплайны.

## Установка

```bash
git clone [https://github.com/varvarank/code-quality-tool.git](https://github.com/varvarank/code-quality-tool.git)
cd code-quality-tool
pip install -r requirements.txt
```

## Примеры использования

Чтобы проанализировать файл, запустите:
`python src/main.py src/analyzer.py`

**Пример вывода в терминале:**
```text
--- Code Report ---
Functions: 3
Docstrings: 3
Lines: 48
Final Score: 100/100
```

## Автоматизация (CI/CD)

В проекте настроен GitHub Actions workflow, который при каждом пуше:
1. Проверяет синтаксис и стиль кода через `flake8`.
2. Запускает автоматические тесты через `pytest`.
3. **Креативная часть (Artifacts):** Инструмент автоматически генерирует отчет audit.txt и сохраняет его в артефакты сборки. Это позволяет увидеть результат анализа, не скачивая код. Также настроен workflow_dispatch для ручного запуска проверки.