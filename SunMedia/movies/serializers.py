from rest_framework import serializers
from .models import *
from Genres.models import Genres
from rest_framework.validators import ValidationError

class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Director


class ActorsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Actors




class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Movies



class MovieGenreSerializers(serializers.ModelSerializer):
    def validate(self, data):
        if not MoviesGenres.objects.filter(movie=data['movie']) and MoviesGenres.objects.filter(Genre=data['Genre']):
            if Movies.objects.all().filter(id=data['movie']).exists():
                return ValidationError( 'Something wrong')
            return ValidationError( 'This movie not exists')
        return ValidationError('This object already exists')
    class Meta:
        fields = '__all__'
        model = MoviesGenres


class MovieActorsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MovieActor


class MovieTreyler(serializers.ModelSerializer):
    class Meta:
        models = MovieTreyler
        fields = '__all__'