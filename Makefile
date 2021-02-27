install:
	pip install -r requirements.txt

lint:
	isort src
	flake8 src
