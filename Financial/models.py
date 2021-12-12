from django.db import models
from Project.models import Project
from django.contrib.auth.models import User
class financial (models.Model):
    STATUS_TYPE = {
        (1, 'deposit'),
        (2, 'harvest Money'),
    }

    title = models.CharField(max_length=50)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    Date = models.DateField(auto_now=True)
    Description = models.TextField()
    image = models.ImageField(upload_to='images', null=True)
    type = models.IntegerField(choices=sorted(STATUS_TYPE))
    money = models.IntegerField()
    userRecipientofmoney = models.ManyToManyField(User,related_name='userMoneydepositor')
    userMoneydepositor = models.ManyToManyField(User)

    def __str__(self):
        return self.title 