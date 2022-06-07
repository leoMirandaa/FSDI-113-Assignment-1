# Mini Challenge 1

Initialize and build out the early stages of our blog application.

1. Create a new virtual environment. = python3 -m venv venv
2. Activate it. = source venv/bin/activate
3. Install Django. = pip3 install django
4. Create a new django project. = django-admin startproject GreatMusic
    4.1. Make sure you use our containing folder for our project.
    4.2. Name the configuration app "config".
5. Create an app called "pages". = python3 manage.py startapp pages added to settings.py
6. Create an app called "posts". = python3 manage.py startapp posts  added to settings.py
7. Create a home page. = create templates
    7.1. Views. pages>views=  create all the gerenic views, create url patterns
    7.2. Templates. = create templates, html files
8. Create an about page.
    8.1. Views.
    8.2. Templates
9. Create a new model for blog posts called "Post". It should have the following fields:
    9.1. Title.
    9.2. Body.
    9.3. Author.
    9.4. Created on (datetime).
10. Run make migrations and migrate your model.
11. Register your model on the admin panel, and interact with it through the admin panel.

`Note: To create the author field, use the following snippet:`

```
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
```
