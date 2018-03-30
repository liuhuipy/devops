# -*- coding:utf-8 -*-

from rest_framework import serializers

from .models import User, UserGroup


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'image')


class UserGroupSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('name', 'description')
