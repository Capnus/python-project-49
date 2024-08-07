install:
	poetry install

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-prime:
	poetry run brain-prime

brain-progression:
	poetry run brain-progression

brain-gcd:
	poetry run brain-gcd

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 brain_games



