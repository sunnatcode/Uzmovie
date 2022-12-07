from django.db import models

# Create your models here.
class Genres(models.Model):
    GenreName = models.CharField(max_length=200)