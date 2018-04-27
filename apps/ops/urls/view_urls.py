# -*- coding:utf-8 -*-

from django.conf.urls import url

from ops.views.ansible_script import AnsibleShellExecView


urlpatterns = [
    url(r'shell/', AnsibleShellExecView.as_view(), name='shell_exec'),
]