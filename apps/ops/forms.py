# -*- coding:utf-8 -*-

from django import forms
from django.forms.widgets import *

from ops.models import AnsibleExecShellLog


class AnsibleShellExecForm(forms.ModelForm):

    class Meta:
        model = AnsibleExecShellLog
        fields = ['assets', 'asset_groups', 'shell']
        widgets = {
            'assets': Select(attrs={'class': 'form-control select2', 'id': 'assets', 'multiple': 'multiple',
                                          'data-placeholder': 'assets'}),
            'asset_groups': Select(attrs={'class': 'form-control select2', 'id': 'asset_groups', 'multiple': 'multiple',
                                                'data-placeholder': 'asset groups'}),
            'shell': TextInput(attrs={'class': 'form-control', 'id': 'shell','placeholder':'shell'}),
            # 'result': Textarea(attrs={'class': 'form-control', 'id': 'res', 'rows':'10', 'style':'background-color: black; color: #00a157;'})
        }
        labels = {
            'assets': '选择资产',
            'asset_groups': '选择资产组',
            'shell': '命令',
            # 'result': '返回结果',
        }



