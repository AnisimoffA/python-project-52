### Hexlet tests and linter status:
[![Actions Status](https://github.com/AnisimoffA/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/AnisimoffA/python-project-52/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9388f6ca6f9296e88a1d/test_coverage)](https://codeclimate.com/github/AnisimoffA/python-project-52/test_coverage)

Task Manager link: [Here](python-project-52-production-312b.up.railway.app)

### Description

This framework is a convenient task manager built on python 3.8 and django 4.2. To use the system, you must be registered.

![img.png](images/img.png)
![img_1.png](images/img_1.png)
___
Here You can create a task list

![img.png](images/img3.png)

and also You can also view all the tasks, change their status and add the necessary labels.

![img.png](images/img4.png)

___
### How to use it?

Firstly, clone the repo:
```python
git clone https://github.com/AnisimoffA/python-project-52
```

Secondary, generate an .env file located in the project's primary directory. You will be required to define specific variables within it:
```python
DATABASE_URL={provider}://{user}:{password}@{host}:{port}/{db}
SECRET_KEY={your secret key}
LANGUAGE=en-us # Or "ru" if you want
```

Thirdly, run the server:
```python
python3 manage.py runserver
```
___
### Requirements

- Python ^3.2
- Django ^4.2
- Flake8 ^4.0.1
- Bootstrap 4
- Gunicorn ^21.0.0