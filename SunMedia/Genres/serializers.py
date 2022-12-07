from rest_framework import serializers
from .models import *



class GenreSerializres(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genres
