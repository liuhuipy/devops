# -*- coding:utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from ..api import UserViewSet, UserGroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'usergroups', UserGroupViewSet, base_name='usergroups')

urlpatterns = [
    url(r'api/accounts/', include(router.urls))
]