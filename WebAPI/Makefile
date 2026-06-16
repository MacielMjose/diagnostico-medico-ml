.PHONY: run test lint install

run:
	uvicorn app.main:app --reload --port 8000

test:
	pytest tests/ -v

test-coverage:
	pytest tests/ --cov=app -v

lint:
	ruff check app/ tests/

install:
	pip install -r requirements.txt
