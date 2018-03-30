# -*- coding:utf-8 -*-

from rest_framework import serializers

from ..models import Asset, AssetGroup, IDC


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = ('id', 'asset_name', 'manage_ipaddress', 'macaddress')


class AssetGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssetGroup
        fields = ('name', 'description')


class IDCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IDC
        fields = ('name', 'address', 'phone')
