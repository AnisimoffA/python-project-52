install:
	poetry install

lint:
	poetry run flake8 task_manager

test:
	poetry run python manage.py test

test-coverage:
	coverage xml

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

push:
	python3 -m pip install dist/hexlet_code-1.0.0-py3-none-any.whl --force-reinstall

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
    poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

shell:
	poetry run python manage.py shell_plus