istall:
	poetry install

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-prime:
	poetry run brain-prime

brain-prog:
	poetry run brain-prog

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 brain_games



