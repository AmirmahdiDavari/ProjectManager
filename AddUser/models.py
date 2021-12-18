from django.contrib.auth.models import User, AbstractUser
from django.db import models


class MyUser(AbstractUser):
    # STATUSE = {
    #     (1, 'Expert'),
    #     (2, 'ScrumMaster'),
    #     (3, 'Financial'),
    #     (4, 'Admin'),
    # }
    #
    # Role = models.IntegerField(choices=sorted(STATUSE), default=1, verbose_name="مهارت")

    Expert = models.BooleanField(default=0, null=True, blank=True)
    ScrumMaster = models.BooleanField(default=0, null=True, blank=True)
    Financial = models.BooleanField(default=0, null=True, blank=True)
    Admin = models.BooleanField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = 'لیست کاربران '
