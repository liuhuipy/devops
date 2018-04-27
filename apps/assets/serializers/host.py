# -*- coding:utf-8 -*-

from rest_framework import serializers

from ..models import Asset, AssetGroup, IDC


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = ('id', 'asset_name', 'manage_ipaddress', 'macaddress', 'sn', 'manufacturer', 'mem_total', 'disk_size')


class AssetGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssetGroup
        fields = ('name', 'description')


class IDCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IDC
        fields = ('name', 'address', 'phone')
