from django.contrib import admin

# Register your models here.
from .models import Topic,Blog
from django.contrib.auth import get_user_model
admin.site.register(Topic)
admin.site.register(Blog)
admin.site.register(get_user_model())