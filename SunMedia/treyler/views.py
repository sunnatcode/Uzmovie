from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import TreylerSerializers
from .models import Treyler
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class TreylerView(ListCreateAPIView):
    serializer_class = TreylerSerializers
    queryset = Treyler.objects.all()

    def post(self, request, *args, **kwargs):
        serialziers = TreylerSerializers(data=request.data)
        if serialziers.is_valid(raise_exception=True):
            serialziers.save()
            data  = {
                'status': 201,
                'success': True,
                'data': serialziers.data
            }
            return Response(data, status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        data = Treyler.objects.all()    
        serializer = TreylerSerializers(data, many=True)
        return Response(serializer.data)