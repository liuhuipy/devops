# -*- coding:utf-8 -*-

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

from ..models import Asset, AssetGroup, IDC
from ..serializers.host import AssetSerializer, AssetGroupSerializer, IDCSerializer
from ..pagination import AssetsPagination


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = AssetsPagination


class AssetGroupViewSet(viewsets.ModelViewSet):
    queryset = AssetGroup.objects.all()
    serializer_class = AssetGroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = AssetsPagination


class IDCViewSet(viewsets.ModelViewSet):
    queryset = IDC.objects.all()
    serializer_class = IDCSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = AssetsPagination


