install:
	poetry install

brain-games:
	poetry run brain-games

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build
	
test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=python-project-lvl1 --cov-report xml

lint:
	poetry run flake8 python-project-lvl1

selfcheck:
	poetry check

check: selfcheck test lint

# build: check
# 	poetry build

.PHONY: install test lint selfcheck check build