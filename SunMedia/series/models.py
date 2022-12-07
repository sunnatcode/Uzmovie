from django.db import models
from Genres.models import Genres
from treyler.models import Treyler
# Create your models here.


class Director(models.Model):
    firs_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    nationaly = models.CharField(max_length=200)
    birth = models.DateField()

class Actors(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    nationaly = models.CharField(max_length=200)
    birth = models.DateField()

class TvSeries(models.Model):
    title = models.CharField(max_length=100)
    decription = models.TextField()
    startYear = models.DateTimeField()
    endYear = models.DateTimeField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    image = models.FileField(upload_to='media/', null=True)

class SeriesActors(models.Model):
    series = models.ManyToManyField(TvSeries)
    actors = models.ManyToManyField(Actors)

class SeriesGenre(models.Model):
    series = models.ForeignKey(TvSeries, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genres)

class SeriesTreyler(models.Model):
    series = models.ForeignKey(TvSeries, on_delete=models.CASCADE)
    treyler = models.ForeignKey(Treyler, on_delete=models.CASCADE)

class SeriesSeason(models.Model):
    series = models.ForeignKey(TvSeries, on_delete=models.CASCADE)
    season = models.IntegerField()
    part = models.IntegerField()