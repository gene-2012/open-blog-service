# OpenBlog Service

A simple open-source blog system powered by Django.

## How to Run This App

### Prework

```bash
python -m venv bl_env
source bl_env/bin/activate  # for Linux
pip install django
```

### Database And User Settings

#### Database

We use SQLite as the database. Run this code to initialize.

```bash
python manage.py migrate
```

#### User

Before starting the app, please create a super user first.

```bash
python manage.py createsuperuser
```

### Start a Development Server

```bash
python manage.py runserver
```
## 