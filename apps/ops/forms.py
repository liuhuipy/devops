# -*- coding:utf-8 -*-

from django import forms

from ops.models import AnsibleScript, AnsibleExecPlaybook



class AnsibleScriptForm(forms.ModelForm):

    class Meta:
        model = AnsibleScript
        fields = ['assets', 'asset_groups', 'shell', 'script']
        widgets = {
            'assets': forms.Select(attrs={'class': 'form-control select2', 'multiple': 'multiple',
                                         'data-placeholder': 'assets'}),
            'asset_groups': forms.Select(attrs={'class': 'form-control select2', 'multiple': 'multiple',
                                                'data-placeholder': 'asset_groups'}),
            'shell': forms.TextInput(attrs={'class': 'form-control','placeholder': 'shell'}),
            'script': forms.Textarea(attrs={'class': 'form-control','placeholder': '不填默认仅执行一条命令'}),
        }
        labels = {
            'assets': '选择主机',
            'asset_groups': '选择主机组',
            'shell': '命令',
            'script': '请填入脚本',
        }


class AnsibleExecPlaybookForm(forms.ModelForm):

    class Meta:
        model = AnsibleExecPlaybook
        fields = ['assets', 'asset_groups', 'playbook_shell', 'playbook_yaml_name']
        widgets = {
            'assets': forms.Select(attrs={'class': 'form-control select2', 'multiple': 'multiple',
                                          'data-placeholder': 'assets'}),
            'asset_groups': forms.Select(attrs={'class': 'form-control select2', 'multiple': 'multiple',
                                                'data-placeholder': 'asset_groups'}),
            'playbook_shell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'playbook_shell'}),
            'playbook_yaml_name': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'yaml_url'}),
        }
        labels = {
            'assets': '选择主机',
            'asset_groups': '选择主机组',
            'playbook_shell': '命令',
            'playbook_yaml_name': '请填入ansible yaml入口路径',
        }
