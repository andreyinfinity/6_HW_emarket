from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(verbose_name='e-mail', unique=True)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    uuid = models.CharField(max_length=32, verbose_name='uuid-hex', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
