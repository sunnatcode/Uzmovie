from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User, update_last_login
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from django.db.transaction import atomic
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework.serializers import CharField,EmailField



class RegisterSerializer(Serializer):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    username = CharField(max_length=255)
    password = CharField(max_length=255)
    email = EmailField(max_length=255)

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise ValidationError("This username is already exists")
        
        if User.objects.filter(email=data['email']).exists():
            raise ValidationError("This email is already exists")
        
        return data

    @atomic
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User(**validated_data)
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username','email','password')



class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'            


class LoginSerializers(TokenObtainPairSerializer):

    def validate(self, attrs):
        user = User.objects.all()
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data['data'] = UserSerializers(self.user).data

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data

