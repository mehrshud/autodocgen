.PHONY: install test lint format clean docker-build

install:
	pip install -r requirements.txt
	pip install pytest pytest-cov black flake8 bandit

test:
	pytest tests/ -v --cov=src --cov-report=term-missing

lint:
	flake8 src/ tests/ --max-line-length=120
	bandit -r src/ -ll

format:
	black src/ tests/

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage coverage.xml __pycache__

docker-build:
	docker build -t $(shell basename $(CURDIR)) .

docker-run:
	docker-compose up -d

all: install lint test