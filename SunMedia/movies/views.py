from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework import status
from .paginators import MoviePaginations
from Genres.models import Genres
# Create your views here.



class DirectorView(ModelViewSet):
    serializer_class = DirectorSerializers
    queryset = Director.objects.all()
    def create(self, request):
        serializer = DirectorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Director successfully created"})
        return Response({"message": 'Something wrong'})    

    def list(self, request):
        queryset = Director.objects.all()
        serializer = DirectorSerializers(queryset, many=True)
        return Response(serializer.data)


class ActorsView(ModelViewSet):
    serializer_class = ActorsSerializers
    queryset = Actors.objects.all()
    def create(self, request):
        serializer = ActorsSerializers(data=request.data)
        if not Actors.objects.filter(first_name=request.data['first_name']).exists() and not Actors.objects.filter(last_name=request.data['last_name']).exists():
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': "Actors successfully created"})
                return Response({"message": 'Something wrong'})    
        return Response({"message": 'This actor already exist b'})    
                   

    def list(self, request):
        queryset = Actors.objects.all()
        serializer = ActorsSerializers(queryset, many=True)
        return Response(serializer.data)


      



class MovieView(ModelViewSet):
    serializer_class = MovieSerializers
    queryset = Movies.objects.all()
    pagination_class = MoviePaginations
    
    
    def create(self, request, *args, **kwargs):
        serializers = MovieSerializers(data=request.data)
        
        if not Movies.objects.filter(title=request.data['title']).exists():
            if serializers.is_valid():
                serializers.save()
                return Response({'message': "Movie successfully created"})
            return Response({"message": 'Something wrong'})
        return Response({"message": 'This movie name already exist'})    


    def list(self, request):
        queryset = Movies.objects.all()
        serializer = MovieSerializers(queryset, many=True)
        return Response(serializer.data) 


    def last_four(self, request):
        user_count = Movies.objects.all().order_by('-id')[-4:-1]
        print(user_count)
        serializers = MovieSerializers(user_count, many=True)
        return Response({'message': serializers.data})
        

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({'message': "Item deleted"})
        except :
            return Response(status=status.HTTP_204_NO_CONTENT)

         

class MovieGenreView(ModelViewSet):
    serializer_class = MovieGenreSerializers
    queryset = MoviesGenres.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializers = MovieGenreSerializers(data=request.data)
        if not MoviesGenres.objects.all().filter(movie=request.data['movie']) and MoviesGenres.objects.all().filter(Genre=request.data['Genre']):
            if Movies.objects.all().filter(id=request.data['movie']).exists(): 
                if serializers.is_valid():
                        serializers.save()
                        return Response({'message': "Movie genre successfully created"})
                return Response({"message": 'Something wrong'})
            return Response({"message": 'This movie not exists'})
        return Response({"message": 'This object already exists'})


    def list(self, request):
        queryset = MoviesGenres.objects.all()
        serializer = MovieGenreSerializers(queryset, many=True)
        return Response(serializer.data) 


class MovieActorView(ModelViewSet):
    
    serializer_class = MovieActorsSerializers
    queryset = MovieActor.objects.all()
    def create(self, request, *args, **kwargs):
        serializers = MovieActorsSerializers(data=request.data)
        if serializers.is_valid():
                serializers.save()
                return Response({'message': "Movie actor successfully created"})
        return Response({"message": 'Something wrong'})
    

    def list(self, request):
        queryset = MovieActor.objects.all()
        serializer = MovieActorsSerializers(queryset, many=True)
        return Response(serializer.data)     

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            instace  = self.get_object()
            instace.delete()
            return Response({'message':'Data deleted'})
        except:
            return Response({'message': 'I think this data not exists'})