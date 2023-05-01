from django.db import models
from datetime import date
from django.template.defaultfilters import date


# Create your models here.
class blood(models.Model):
    Fname=models.CharField(max_length=20)
    Lname=models.CharField(max_length=20,null=True)
    Age=models.IntegerField(null=True)
    Bloodgroupchoices=[
        ('A+','A+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('O+','O+')
    ]
    Bloodgroup=models.CharField(choices=Bloodgroupchoices,max_length=25,null=True)
    #Date=models.DateField(blank=True,null=True)


def _str_(self):
        return self.Fname  