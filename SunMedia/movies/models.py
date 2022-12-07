
from django.db import models
from django.db.models import TextChoices
from Genres import models as q
from treyler.models import Treyler
# Create your models here.



class Director(models.Model):
    firs_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    nationaly = models.CharField(max_length=200)
    birth = models.DateField()

class Movies(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    realseYear = models.DateTimeField()
    country = models.CharField(max_length=200)
    MovieLength = models.IntegerField()


class MoviesGenres(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    genres = models.ManyToManyField(q.Genres)

class Actors(models.Model):
    firs_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    nationaly = models.CharField(max_length=200)
    birth = models.DateField()

class MovieActor(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE)

class MovieTreyler(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    treyler = models.ForeignKey(Treyler, on_delete=models.CASCADE)