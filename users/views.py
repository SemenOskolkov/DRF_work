from django.shortcuts import render
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreatAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
