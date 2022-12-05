
from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30, blank=False, default='')
    roll = models.IntegerField()
    address = models.CharField(max_length=200, blank=False, default='')
    
    def __str__(self):
        return self.name
    
