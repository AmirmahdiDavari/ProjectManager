from django.db import models
from django.contrib.auth.models import User

from ProjectManager.settings import AUTH_USER_MODEL
from  extentions.Utils import jalali_converter
from ProjectManager import settings
from Step.models import Step


class Task(models.Model):
    STATUS_TASK = {
        (0, 'deActive'),
        (1, 'Active'),
        (2, 'Faile'),
        (3, 'Done'),
    }

    SATTUS_RATE={
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')
    }
    SATTUS_Periority={
        (1,'high'),
        (2,'normal'),
        (3,'low')
    }
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    createDate = models.DateTimeField(auto_now_add=True,editable=False)
    # startDate = models.DateField(blank=True,null=True)
    endDate = models.DateField(blank=True,null=True)
    status = models.IntegerField(choices=sorted(STATUS_TASK),default=0,blank=True, null=True,editable=False)
    Estimated_end=models.DateField(blank=True,null=True,editable=False)
    StepID = models.ForeignKey(Step,on_delete=models.CASCADE,blank=True, null=True)
    ratePerformance = models.IntegerField(choices=sorted(SATTUS_RATE),null= True ,editable=False)
    Expert = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE ,null=True)
    periority=models.IntegerField(choices=sorted(SATTUS_Periority),default=3)

    def __str__(self):
        return self.title



