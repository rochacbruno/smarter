test: lint
	pytest -v --cov-config .coveragerc --cov=smarter -l --tb=short --maxfail=1 tests/
	coverage xml
	coverage html

lint:
	flake8 .
	black --check .
	mypy smarter

install:
	pip install -e .[test]

fmt:
	isort .
	black .

report:
	codecov

ci: install test report