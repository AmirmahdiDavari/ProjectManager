from django.contrib.auth.models import User, AbstractUser
from django.db import models


class MyUser(AbstractUser):
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = 'لیست کاربران '
