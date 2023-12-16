# OpenBlog Service

## Introduce

This is a simple open-source blog system based by Django.

He has several key features as follows:

- Simple blog display.

- User-defined homepage.

- Powerful backend powered by Django.

### URL Tree

- localhost
  - `/`:index
  - `blogs/[blog_id]/`: Blog detail
  - `new_blog/`: new blog
  - `edit_blog/[blog_id]/`: edit blog
  - `delete_blog/[blog_id]/`: delete blog
  - `/user/`
    - `[user_id]/[page_id]/`: user home
    - `edit_page/[user_id]/`: edit user home
  - `/accounts/`
    - `login/`: login
    - `register/`: register(closed)

### Picture

Home page: ![Home Page](/picture/home_page.jpeg)

Blog detail: ![Blog Detail](/picture/detail.jpeg)

Edit blog: ![Edit Blog](/picture/edit_blog.jpeg)

User-defined homepage: ![User-defined Homepage](/picture/user_home.jpeg)

Admin page(by Django): ![Admin](/picture/admin_view.jpeg)

Add blog page: ![Add Blog](/picture/add_blog.jpeg)

Login: ![Login](/picture/login.jpeg)

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

## Contact Us

Email: [gene201248@126.com](mailto:gene201248@126.com)
