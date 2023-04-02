from django.shortcuts import render
from rest_framework import generics

from users.models import User
from users.permissions import OwnProfileEditPermission
from users.serializers import UserSerializer, UserProfileInfoSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreatAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserProfileInfoSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [OwnProfileEditPermission]
