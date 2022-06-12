from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, RegistrationSerializer
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import AllowAny
# from .models import User
User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenObtainPairRefreshView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get_object_by_username(self, userName):
        try:
            return User.objects.filter(userName=userName)
        except User.DoesNotExist:
            raise Http404

    # Get User by UserID (eg. "id = 5" )
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    # Get User by UserName (eg. "cashmy")
    def get_by_userName(self, userName):
        user = self.get_object_by_username(userName)
        serializer = UserSerializer(user)
        return Response(serializer.data)