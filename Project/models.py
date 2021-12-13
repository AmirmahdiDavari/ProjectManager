
from django.db import models
from django.utils.html import format_html

from django.contrib.auth.models import User

from ProjectManager import settings


class Project(models.Model):

    STATUS_CHOICES = {
        (1, 'Done'),
        (2, 'deActive'),
        (3, 'Active'),
        (4, 'Fail'),
    }

    title = models.CharField(max_length=100)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='images',null=True)
    Experts = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="creator_set")
    ScrumMaster = models.ManyToManyField(settings.AUTH_USER_MODEL)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.IntegerField(choices=sorted(STATUS_CHOICES),default=2)


    def __str__(self):
        return self.title
    def image_tag(self):
        return format_html( "<img width=100 height=75 src='{}'>".format(self.image.url))
