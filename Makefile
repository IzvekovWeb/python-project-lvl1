# Установка зависимостей проекта
install:
	poetry install

# Запуск программ (игр)
brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

# Сборка проекта в whl файл
build:
	poetry build

# Публикация в PyPI (иммитация)
publish:
	poetry publish --dry-run

# Установка wheel файла
package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

# Проверка на lint
lint:
	poetry run flake8 brain_games

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=python-project-lvl1 --cov-report xml

.PHONY: install test lint selfcheck check build