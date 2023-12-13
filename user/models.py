from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    page = models.TextField()
    avatar = models.FileField(upload_to='avatars/',default='default.png')
    def __str__(self) -> str:
        return self.username
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if self.page == None:
            self.page = 'this is a homepage'