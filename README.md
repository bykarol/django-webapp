# Overview

Web application to manage the list of patients in a clinic. This application is created using Django framework for Python.

> Using a framework can reduce the time it takes to create web content. In the case of Django, you also have the benefit of using the Python programming language to process requests. When a request is made to this web app, the Django framework calls the appropriate Python code. The Python code then parse the request and prepare a response by reading a database. To produce the response, a template HTML file is populated with data created by the Python function. The response is then automatically sent back by the Django framework. 


## Guidance
### Django:
1) Virtual environment to manage dependencies (optional):
  - Set virtual environment: `python -m venv venv`
  - Activate the virtual environment: `.\venv\Scripts\activate`
2) Use pip to install Django: `python -m pip install Django`
3) Django useful commands:
  - Create the initial project files: `django-admin startproject my_project_name`
  - Enter to the project folder: `cd my_project_name`
  - Run the server (check if it is working): `python manage.py runserver`
  - Open the browser, go to http://localhost:8000
4) Creating a new app: `python manage.py startapp my_app_name`
5) After changing the model, do migrations:
  - Add new migrations `python manage.py makemigrations`
  - Do the migrations `python manage.py migrate`

## [Software Demo Video](http://youtube.link.goes.here)

# Web Pages

{Describe each of the web pages you created and how the web app transitions between each of them.  Also describe what is dynamically created on each page.}

# Development Environment
* Visual Studio Code
* Pylance (VS Code Extension)
* Django for Python
* SQLite
* CSS framework - [Bootstrap](https://getbootstrap.com/)
* Git / GitHub

# Useful Websites

* [Django Documentation and Tutorial (official site)](https://docs.djangoproject.com/en/3.0/contents/)
* [Django Tutorial - TutorialsPoint](https://www.tutorialspoint.com/django/index.htm)
* [Django Tutorial - RealPython](https://realpython.com/get-started-with-django-1/)
* [Master in Python - Django Tutorial from video #52 to #66. Spanish Tutorial](https://youtu.be/DdDpaO66gdI?si=N7SABKIobnwl84sq)

# Future Work

* Data Validation on ServerSide
* Item 2
* Item 3
