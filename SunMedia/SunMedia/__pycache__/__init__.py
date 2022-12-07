from django.db import models
from django.db.models import TextChoices
# Create your models here.



class Genres(models.Model):
    GenreName = models.CharField(max_length=100)
