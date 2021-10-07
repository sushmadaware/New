from django.db import models

# Create your models here.
class StudentModel(models.Model):
    rn=models.IntegerField()
    name=models.CharField(max_length=30)
    marks=models.FloatField()