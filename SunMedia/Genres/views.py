from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import GenreSerializres
from .models import Genres
from rest_framework.response import Response
# Create your views here.

class GenreView(ModelViewSet):
    serializer_class = GenreSerializres
    queryset = Genres.objects.all()
    def create(self, request, *args, **kwargs):
        serializers  = GenreSerializres(data=request.data)
        if not Genres.objects.filter(GenreName=request.data['GenreName']).exists():
            if serializers.is_valid():
                serializers.save()
                return Response({'message': "Genre successfully created"})
            return Response({"message": 'Something wrong'})
        return Response({"message": 'This genre name already exist'})                    


    def list(self, request):
        queryset = Genres.objects.all()
        serializer = GenreSerializres(queryset, many=True)
        return Response(serializer.data)  