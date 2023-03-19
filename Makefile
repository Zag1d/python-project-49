install:
	poetry install #эта команда полезны при первом клонировании репозитория

brain-games:
	poetry run brain-games #Набирать команду нужно - make brain-games

build:
	poetry build #Сборка

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

