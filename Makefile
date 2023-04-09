PYTHON=./.venv/bin/python

PHONY = help install install-dev test format lint type-check secure migrations migrate

help:
	@echo "---------------HELP-----------------"
	@echo "To install the project type -> make install"
	@echo "To install the project for development type -> make install-dev"
	@echo "To test the project type -> make test"
	@echo "To test with coverage -> make test-cov"
	@echo "To format code type -> make format"
	@echo "To check linter type -> make lint"
	@echo "To run type checker -> make type-check"
	@echo "To run all security related commands -> make secure"
	@echo "To create database migrations -> make migrations"
	@echo "To run database migrations -> make migrate"
	@echo "------------------------------------"

install:
	${PYTHON} -m flit install --env --deps=develop

install-dev:
	${PYTHON} -m flit install --env --deps=develop --symlink

test:
	TEST_RUN="TRUE" ${PYTHON} -m pytest -svvv  tests

test-cov:
	TEST_RUN="TRUE" ${PYTHON} -m pytest -svvv --cov-report html --cov=src tests

format:
	${PYTHON} -m isort src tests --force-single-line-imports
	${PYTHON} -m autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude=__init__.py
	${PYTHON} -m black src tests --config pyproject.toml
	${PYTHON} -m isort src tests

lint:
	${PYTHON} -m flake8 --max-complexity 5 --max-cognitive-complexity=3 src
	${PYTHON} -m black src tests --check --diff --config pyproject.toml
	${PYTHON} -m isort src tests --check --diff

type-check:
	${PYTHON} -m pytype --config=pytype.cfg src

secure:
	${PYTHON} -m bandit -r src --config pyproject.toml

migrations:
	alembic -c src/calculator/adapters/db/alembic.ini revision --autogenerate

migrate:
	alembic -c src/calculator/adapters/db/alembic.ini upgrade head

run:
	${PYTHON} -m uvicorn src.calculator.adapters.entrypoints.api.app:app --host 0.0.0.0 --port 8000 --reload