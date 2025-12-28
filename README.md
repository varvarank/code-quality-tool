# Code Quality Assessment Tool

![Build Status](https://github.com/ВАШ_НИК/code-quality-tool/actions/workflows/audit.yml/badge.svg)

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
git clone [https://github.com/ВАШ_НИК/code-quality-tool.git](https://github.com/ВАШ_НИК/code-quality-tool.git)
cd code-quality-tool
pip install -r requirements.txt