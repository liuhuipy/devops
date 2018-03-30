# -*- coding:utf-8 -*-

from django import forms
# from django.forms import ModelForm
from django.forms.widgets import *

from assets.models import IDC, Asset, AssetGroup


class AssetForm(forms.ModelForm):
    '''
    sn = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'sn'}),
        label='SN号',
        max_length=64,
        required=False,
        error_messages={
            'validate_unique': 'SN号已经存在',
        }
    )
    idc = forms.ChoiceField(
        widget=Select(attrs={'class': 'from-control select2', 'style': 'width:100%', 'placeholder': 'idc'}),
        label='机房',
        required=False,
    )
    hostgroup = forms.ChoiceField(
        widget=Select(attrs={'class': 'form-control select2', 'data-placeholder': 'Select a State',
                               'style': 'width:100%', 'multiple': 'multiple', 'placeholder': 'hostgroup'}),
        label='主机组',
        required=False,
    )
    host_type = forms.ChoiceField(
        widget=Select(attrs={'class': 'form-control select2', 'style': 'width:100%', 'placeholder': 'host_type'}),
        label='主机类型',
        required=False,
    )
    host_model = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'host_model'}),
        label='主机型号',
        required=False,
    )
    manufactory = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'manufactroy'}),
        label='厂商',
        required=False,
    )
    os_type = forms.MultipleChoiceField(
        widget=Select(attrs={'class': 'form-control select2', 'style': 'width:100%','placeholder': 'os_type'}),
        label='操作系统类型',
        required=False,
    )
    os_version = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'os_version'}),
        label='操作系统版本',
        required=False,
        error_messages={
            'validate_unique': ''
        }
    )
    manage_user = forms.ChoiceField(
        widget=Select(attrs={'class': 'form-control select2', 'placeholder': 'manage_user'}),
        label='管理人',
        required=False,
    )
    cpu_model = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'cpu_model'}),
        label='CPU型号',
        required=False,
    )
    cpu_num = forms.IntegerField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'cpu_num'}),
        label='物理CPU个数',
        required=False,
    )
    cpu_cores = forms.IntegerField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'cpu_cores'}),
        label='逻辑CPU个数',
        required=False,
    )
    memory = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'memory'}),
        label='内存大小',
        required=False,
    )
    disk = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'disk'}),
        label='磁盘大小',
        required=False,
    )
    status = forms.ChoiceField(
        widget=Select(attrs={'class': 'from-control select2', 'style': 'width:100%', 'placeholder': 'status'}),
        label='主机状态',
        required=False,
    )
    description = forms.ChoiceField(
        widget=Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
        label='描述',
        required=False
    )
    '''
    class Meta:
        model = Asset
        fields = [
            'asset_name','manage_ipaddress','other_ipaddress','manage_user','sn',
            # 'hostname', 'manage_ipaddress', 'other_ipaddress', 'macaddress', 'sn', 'idc', 'hostgroup', 'host_type',
            # 'host_model', 'manufactory', 'os_type', 'os_version', 'manage_user', 'cpu_model', 'cpu_num', 'cpu_cores',
            # 'memory', 'disk', 'status', 'description'
        ]
        widgets = {
            'asset_name': TextInput(attrs={'class': 'form-control','placeholder': 'hostname'}),
            'manage_ipaddress': TextInput(attrs={'class': 'form-control', 'data-inputmask': "'alias': 'ip'",
                                         'data-mask': '', 'placeholder': 'manage_ip'}),
            'other_ipaddress': TextInput(attrs={'class': 'form-control', 'data-inputmask': "'alias': 'ip'",
                                         'data-mask': '', 'placeholder': 'other_ip'}),
            'manage_user': Select(attrs={'class': 'form-control select2', 'placeholder': 'manage_user'}),
            'sn': TextInput(attrs={'class': 'form-control', 'placeholder': 'sn'}),
        }
        labels = {
            'asset_name': '资产名',
            'manage_ipaddress': '管理IP',
            'other_ipaddress': '其他IP',
            'manage_user': '管理人',
            'sn': 'SN号',
        }


class AssetGroupForm(forms.ModelForm):
    class Meta:
        model = AssetGroup
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','placeholder': 'hostname'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }
        labels = {
            'name': '资产组名',
            'description': '描述',
        }


class IDCForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = [
            'name', 'address', 'phone', 'manage_user', 'network', 'operator', 'description',
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'manage_user': Select(attrs={'class': 'form-control select2', 'placeholder': 'manage_user'}),
            'network': TextInput(attrs={'class': 'form-control', 'placeholder': 'network'}),
            'operator': Select(attrs={'class': 'form-control select2', 'placeholder': 'operator'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }
        labels = {
            'name': '机房名',
            'address': '机房地址',
            'phone': '联系电话',
            'manage_user': '管理人',
            'network': 'IP地址范围',
            'operator': '运营商',
            'description': '描述',
        }





