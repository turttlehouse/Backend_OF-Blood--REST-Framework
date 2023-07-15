from django.db import models
from datetime import date
from django.template.defaultfilters import date


# Create your models here.
class blood(models.Model):      #we create a class that inherits form models.Model and we create the fields for correct datatype
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
    occupationchoices= [
    ('Teacher','Teacher'),
    ('Business','Business'),
    ('farmer','farmer'),
    ('Doctor','Doctor'),
    ('others','others')
    ]
    occupation=models.CharField(choices=occupationchoices,max_length=25,null=True)
    #Date=models.DateField(blank=True,null=True)



#we also apply string method to see an accurate description here we don't need to create and id since django does this for us
def _str_(self):
        return self.Fname  