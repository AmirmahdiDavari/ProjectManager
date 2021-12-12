from django.contrib.auth.models import User
from django.db import models
class User(User):
    pass
    STATUSE={
        (1,'expert'),
        (2,'scram'),
        (3,'fonshial'),
    }
    Skill=models.IntegerField(choices=sorted(STATUSE),default=1)