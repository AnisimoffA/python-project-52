lint: 
	poetry run flake8 task_manager labels statuses tasks users

install:
	poetry install


selfcheck:
	poetry check

check: selfcheck lint 

build: check
	poetry build

push:
	python3 -m pip install dist/python_project_83-0.1.0-py3-none-any.whl --force-reinstall

dev:
	poetry run python manage.py runserver
	
PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

shell:
	poetry run python manage.py shell_plus