# -*- coding:utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from assets.views.asset import AssetReport
from ..api.asset import AssetViewSet, AssetGroupViewSet, IDCViewSet


router = routers.DefaultRouter()
router.register(r'assets', AssetViewSet, base_name='assets')
router.register(r'assetgroups', AssetGroupViewSet, base_name='assetgroups')
router.register(r'idcs', IDCViewSet, base_name='idcs')


urlpatterns = [
    url(r'api/assets/', include(router.urls)),
    url(r'api/assets/report/', AssetReport.as_view()),
]