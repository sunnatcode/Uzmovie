from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView, DestroyAPIView
from .serializers import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status':201,
                'success':True,
                'data':serializer.data
            }
            return Response(data,status.HTTP_201_CREATED)
            


class RegisterGetView(ListAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

class UserDelete(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes  = [AllowAny, ]
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message':'User deleted'})
    
class LoginApiView(TokenObtainPairView):
    serializer_class = LoginSerializers
