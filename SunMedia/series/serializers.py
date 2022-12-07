from rest_framework import serializers
from .models import (Director, Actors, TvSeries, SeriesActors, SeriesGenre, SeriesSeason, SeriesTreyler)
from Genres.models import Genres

class SeriesDirectorSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Director


class SerActorsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Actors


class TvSeriesSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TvSeries
    
    def validate_title(self, validated_data):
        if TvSeries.objects.filter(title=validated_data).exists():
            raise serializers.ValidationError('This Series already exists')
        return validated_data


class SeriesGenreSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SeriesGenre


class SeriesActorsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SeriesActors
    def validate(self, validated_data):
        print(validated_data)


class SeriesSeasonSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SeriesSeason

class SeriesTreylerSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SeriesTreyler