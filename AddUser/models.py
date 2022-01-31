from django.contrib.auth.models import User, AbstractUser
from django.db import models


class MyUser(AbstractUser):
    image = models.ImageField(upload_to='project/images', blank=True,null=True, verbose_name="عکس")
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = 'لیست کاربران '
        
