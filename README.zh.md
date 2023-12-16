# OpenBlog Service

## 简介

这是一个基于Django的简单开源博客系统。

它具有以下几个关键特点：

- 简洁的博客展示。

- 用户自定义首页。

- 强大的后端（由Django支持）。

### URL解析列表

- 本地主机
  - `/`：首页
  - `blogs/[blog_id]/`：博客详情
  - `new_blog/`：新建博客
  - `edit_blog/[blog_id]/`：编辑博客
  - `delete_blog/[blog_id]/`：删除博客
  - `/user/`
    - `[user_id]/[page_id]/`：用户主页
    - `edit_page/[user_id]/`：编辑用户主页
  - `/accounts/`
    - `login/`：登录
    - `register/`：注册（有BUG,已关闭）

### 图片

首页： ![首页](/picture/home_page.jpeg)

博客详情： ![博客详情](/picture/detail.jpeg)

编辑博客： ![编辑博客](/picture/edit_blog.jpeg)

用户自定义首页： ![用户自定义个人主页](/picture/user_home.jpeg)

管理页面（由Django生成）： ![管理页面](/picture/admin_view.jpeg)

添加博客页面： ![添加博客](/picture/add_blog.jpeg)

登录： ![登录](/picture/login.jpeg)

## 如何运行此应用

### 预备工作

```bash
python -m venv bl_env
source bl_env/bin/activate  # 对于Linux
pip install django
```

### 数据库和用户设置

#### 数据库

我们使用SQLite作为数据库。运行以下代码进行初始化。

```bash
python manage.py migrate
```

#### 用户

在启动应用之前，请先创建一个超级用户。

```bash
python manage.py createsuperuser
```

### 启动开发服务器

```bash
python manage.py runserver
```

## 联系我们

电子邮件：[gene201248@126.com](mailto:gene201248@126.com)
