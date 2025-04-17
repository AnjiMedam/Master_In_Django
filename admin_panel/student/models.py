from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=10,default='nothing')

    # def __str__(self):
    #     return self.name  # no need when we use class ProfileAdmin in admin.py
    


class Result(models.Model):
    stu_class = models.CharField(max_length=100)
    marks = models.IntegerField()
     
    # def __str__(self):
    #     return str(self.marks)        # no need when we use class ResultAdmin in admin.py