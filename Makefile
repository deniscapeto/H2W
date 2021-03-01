install:
	poetry install

lint:
	poetry run isort src
	poetry run flake8 src
