install:
	pip install -r requirements-dev.txt

lint:
	isort src
	flake8 src

depend-tree:
	pipdeptree
