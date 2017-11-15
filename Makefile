lint:
	python -m flake8
	python -m mypy --ignore-missing-imports .
	python -m pylint *.py
	python -m pycodestyle --first *.py
	python -m pydocstyle
