# OpenBlog Service

A simple opensource blog system powered by Django.

## How To Run This App

### Prework

```bash
python -m venv bl_env
bl_env/scripts/activate -> for windows
pip install django
```

### Database Settings

We use Sqlite as the database. Run this code to init.

```bash
python manage.py migrate
```

### Start A DEV Server

```bash
python manage.py runserver
```