from django.db import models

# Create your models here.

class Treyler(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    startYear = models.DateTimeField()
    endYear = models.DateTimeField()

