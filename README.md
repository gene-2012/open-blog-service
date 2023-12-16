# OpenBlog Service

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

## Introduce

This is a simple open-source blog system based by Django.

He has several key features as follows:

- Simple blog display.

- User-defined homepage.

- Powerful backend powered by Django.

### Picture

Home page: ![Home Page](/picture/home_page.jpeg)

Blog detail: ![Blog Detail](/picture/detail.jpeg)

Edit blog: ![Edit Blog](/picture/edit_blog.jpeg)

User-defined homepage: ![User-defined homepage](/picture/user_home.jpeg)

Admin page(by Django): ![Admin](/picture/admin_view.jpeg)
