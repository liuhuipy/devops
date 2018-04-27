# -*- coding:utf-8 -*-

from django.conf.urls import url

from audit.views import ShellListView, ShellDelView


urlpatterns = [
    url(r'shell/log/list/', ShellListView.as_view(), name='shell_list'),
    url(r'shell/log/del/(?P<shell_id>[0-9a-zA-Z\-]{36})/$', ShellDelView.as_view(), name='shell_del'),
]