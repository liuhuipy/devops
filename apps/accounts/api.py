# -*- coding:utf-8 -*-

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer, UserGroupSerialzer
from .models import User, UserGroup


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerialzer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
