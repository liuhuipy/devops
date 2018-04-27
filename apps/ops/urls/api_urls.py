# -*- coding:utf-8 -*-

from django.conf.urls import url

from ops.api import shellexec


urlpatterns = [
    url(r'api/ops/shell/', shellexec),
]