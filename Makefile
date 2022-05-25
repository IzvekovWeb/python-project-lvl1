install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 brain_games

build:
	poetry build
	
test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=python-project-lvl1 --cov-report xml


selfcheck:
	poetry check

check: selfcheck test lint

# build: check
# 	poetry build

.PHONY: install test lint selfcheck check build