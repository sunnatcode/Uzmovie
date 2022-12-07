from django.shortcuts import render
from .serializers import (SeriesDirectorSerializers, SeriesActorsSerializers,
SeriesSeasonSerializers, TvSeriesSerializers, SeriesTreylerSerializers,
SerActorsSerializers, SeriesGenreSerializers)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Director, Actors, TvSeries, SeriesActors, SeriesGenre, SeriesSeason, SeriesTreyler
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework import status
# Create your views here.

class DirectorView(ModelViewSet):
    serializer_class = SeriesDirectorSerializers
    queryset = Director.objects.all()
    def create(self, request):
        serializer = SeriesDirectorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Director successfully created"})
        return Response({"message": 'Something wrong'})    

    def list(self, request):
        queryset = Director.objects.all()
        serializer = SeriesDirectorSerializers(queryset, many=True)
        return Response(serializer.data)


class ActorsView(ModelViewSet):
    serializer_class = SerActorsSerializers
    queryset = Actors.objects.all()
    def create(self, request):
        serializer = SerActorsSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'satatus': 201,
                'success': True,
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)    

                   

    def list(self, request):
        queryset = Actors.objects.all()
        serializer = SeriesActorsSerializers(queryset, many=True)
        return Response(serializer.data)


class TvSeriesView(ModelViewSet):
    queryset  = TvSeries.objects.all()
    serializer_class = TvSeriesSerializers

    def create(self, request, *args, **kwargs):
        serializers = TvSeriesSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            data = {
                "status": 201,
                "success": True,
                'data' : serializers.data
            }
            return Response(data, status.HTTP_201_CREATED)
  

    def list(self, request):
        queryset = TvSeries.objects.all()
        serializer = TvSeriesSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({"message": "Data deleted"})
        except:
               return Response({"message": "This Data Not found"})


class TvSeriesSeasonView(GenericAPIView):
    queryset = SeriesSeason.objects.all()
    serializer_class = SeriesSeasonSerializers

    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            data = {
                "status": 201,
                "success": True,
                'data' : serializers.data
            }
            return Response(data, status.HTTP_201_CREATED)

    def get(self, request):
        data = SeriesSeason.objects.all()
        serializ = SeriesSeasonSerializers(data, many=True)
        
        return Response(serializ.data)


class SeriesGenreView(ListCreateAPIView):
    serializer_class = SeriesGenreSerializers
    queryset = SeriesGenre.objects.all()

    def post(self, request, *args, **kwargs):
        serializers = SeriesGenreSerializers(data=  request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'data': serializers.data})

    def get(self, request, *args, **kwargs):
        data = SeriesGenre.objects.all()
        serelaizer = SeriesGenreSerializers(data, many=True)
        return Response(serelaizer.data)        

class SeriesActorsView(ListCreateAPIView):
    serializer_class = SerActorsSerializers
    queryset = SeriesActors.objects.all()

    def post(self, request, *args, **kwargs):
        serializers = SerActorsSerializers(data=  request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'data': serializers.data})

    def get(self, request, *args, **kwargs):
        data = SeriesActors.objects.all()
        serelaizer = SerActorsSerializers(data, many=True)
        return Response(serelaizer.data)        

class SeriesTreylerView(GenericAPIView):
    serializer_class = SeriesTreylerSerializers
    queryset = SeriesTreyler.objects.all()

    def post(self, request, *args, **kwargs):
        serializers = SeriesTreylerSerializers(data=  request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'data': serializers.data})

    def get(self, request, *args, **kwargs):
        data = SeriesTreyler.objects.all()
        serelaizer = SeriesTreylerSerializers(data, many=True)
        return Response(serelaizer.data)        