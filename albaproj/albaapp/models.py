from django.db import models

# Create your models here.

class Albamon(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=500)
    detail_info = models.TextField()
    pay = models.PositiveIntegerField(default=8720)
    work = models.TextField()
    applicant = models.PositiveIntegerField(default=0)

def __str__(self):
    return self.name