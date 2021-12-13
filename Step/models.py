from django.db import models
from Project.models import Project
class parent(models.Model):

    parentname=models.CharField(max_length=50)

    def __str__(self):
        return self.parentname



class Step(models.Model):
    SATTUS_Periority = {
        (1, 'high'),
        (2, 'normal'),
        (3, 'low')
    }
    Name=models.CharField(max_length=200)
    priority=models.IntegerField()
    ProjectId=models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    ParentId=models.OneToOneField(parent,on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.Name