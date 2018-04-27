# -*- coding:utf-8 -*-

import json

from rest_framework.views import APIView
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from ops.tasks import exec_shell

# class ShellExecView(APIView):
def shellexec(request):
    if request.method == 'POST':
        print(request)
        ret = exec_shell(request)
        return HttpResponse(json.dumps({
            'status': 0,
            'ret': ret
        }))