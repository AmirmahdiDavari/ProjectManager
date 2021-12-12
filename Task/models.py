from django.db import models
from django.contrib.auth.models import User
from Step.models import Step
from django.utils import timezone
# class ExpertUser(models.Model):
#     STEPID_CHOICES={
#         (1,'SEO'),
#         (2,'FRONT_END'),
#         (3,'BACK_END'),
#         (4,'SRVER'),
#     }
#     ferst_neme=models.TextField()
#     last_name=models.TextField()
#     emailaddres=models.EmailField()
#     Role=models.IntegerField(choices=sorted(STEPID_CHOICES),null=False)
#
#     def __str__(self):
#         return self.STEPID_CHOICES


class Task(models.Model):
    STATUS_CHOICES = {
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
    createDate = models.DateTimeField(auto_now_add=True,null=True)
    startDate = models.DateField(blank=True,null=True)
    endDate = models.DateField(blank=True,null=True)
    status = models.IntegerField(choices=sorted(STATUS_CHOICES),default=0,blank=True, null=True)
    Estimated_end=models.DateField(blank=True,null=True)
    StepID = models.ForeignKey(Step,on_delete=models.CASCADE,blank=True, null=True)
    ratePerformance = models.IntegerField(choices=sorted(SATTUS_RATE),null= True ,editable=False)
    Expert = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    periority=models.IntegerField(choices=sorted(SATTUS_Periority),default=3)

    def __str__(self):
        return self.title
