# -*- coding:utf-8 -*-

import json

from django.views.generic import FormView
from django.shortcuts import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse

from ops.models import AnsibleScript, AnsibleExecShellLog
from ops.forms import AnsibleShellExecForm
from utils.mixins import BaseMixin, ActionPermissionRequiredMixin
from ops.tasks import exec_shell


class AnsibleShellExecView(BaseMixin, ActionPermissionRequiredMixin, FormView):
    template_name = 'ops/shell_exec.html'
    model = AnsibleExecShellLog
    permission_required = 'ops.add_ansibleexecshelllog'
    form_class = AnsibleShellExecForm


    # def post(self, request, *args, **kwargs):
    #     print(request.POST.getlist('assets'))
    #     ret = exec_shell(request)
    #     # return HttpResponse(json.dumps(ret), content_type='application/json')
    #     return HttpResponse('<h1>test</h1>')

    def get_context_data(self, *args, **kwargs):
        ret = {}
        if self.request.method == 'POST':
            ret = exec_shell(self.request)
        kwargs['ret'] = json.dumps(ret)
        return super(AnsibleShellExecView, self).get_context_data(*args, **kwargs)


