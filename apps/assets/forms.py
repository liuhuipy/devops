# -*- coding:utf-8 -*-

from django import forms
# from django.forms import ModelForm
from django.forms.widgets import *

from assets.models import Host, HostGroup, NetworkDevice, IDC


class HostForm(forms.ModelForm):
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
        model = Host
        fields = [
            'hostname','manage_ipaddress','other_ipaddress','manage_user'
            # 'hostname', 'manage_ipaddress', 'other_ipaddress', 'macaddress', 'sn', 'idc', 'hostgroup', 'host_type',
            # 'host_model', 'manufactory', 'os_type', 'os_version', 'manage_user', 'cpu_model', 'cpu_num', 'cpu_cores',
            # 'memory', 'disk', 'status', 'description'
        ]
        widgets = {
            'hostname': TextInput(attrs={'class': 'form-control','placeholder': 'hostname'}),
            'manage_ipaddress': TextInput(attrs={'class': 'form-control', 'data-inputmask': "'alias': 'ip'",
                                         'data-mask': '', 'placeholder': 'manage_ip'}),
            'other_ipaddress': TextInput(attrs={'class': 'form-control', 'data-inputmask': "'alias': 'ip'",
                                         'data-mask': '', 'placeholder': 'other_ip'}),
            'manage_user': Select(attrs={'class': 'form-control select2', 'placeholder': 'manage_user'}),
        }
        labels = {
            'hostname': '主机名',
            'manage_ipaddress': '管理IP',
            'other_ipaddress': '其他IP',
            'manage_user': '管理人',
        }


class HostGroupForm(forms.ModelForm):
    class Meta:
        model = HostGroup
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','placeholder': 'hostname'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }
        labels = {
            'name': '主机组名',
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


class NetworkDeviceForm(forms.ModelForm):
    class Meta:
        model = NetworkDevice
        fields = [
            'device_name', 'manage_ipaddress', 'device_type', 'other_ipaddress', 'macaddress', 'sn',
            'port_num', 'idc', 'manufactory', 'manage_user', 'device_detail', 'status',
        ]
        widgets = {
            'device_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'device_name'}),
            'manage_ipaddress': TextInput(attrs={'class': 'form-control', 'data-inputmask': "'alias': 'ip'",
                                         'data-mask': '', 'placeholder': 'manage_ipaddress'}),
            'device_type': Select(attrs={'class': 'form-control select2', 'placeholder': 'device_type'}),
            'other_ipaddress': TextInput(attrs={'class': 'form-control', 'data-inputmask': "'alias': 'ip'",
                                         'data-mask': '', 'placeholder': 'other_ipaddress'}),
            'macaddress': TextInput(attrs={'class': 'form-control', 'placeholder': 'macaddress'}),
            'sn': TextInput(attrs={'class': 'form-control', 'placeholder': 'sn'}),
            'port_num': TextInput(attrs={'class': 'form-control', 'placeholder': 'port_num'}),
            'idc': Select(attrs={'class': 'form-control select2', 'placeholder': 'idc'}),
            'manfactory': TextInput(attrs={'class': 'form-control', 'placeholder': 'manfactory'}),
            'manage_user': Select(attrs={'class': 'form-control select2', 'placeholder': 'manage_user'}),
            'device_detail': Textarea(attrs={'class': 'form-control', 'placeholder': 'device_detail'}),
            'status': Select(attrs={'class': 'form-control select2', 'placeholder': 'status'}),
        }
        labels = {
            'device_name': '设备名称',
            'manage_ipaddress': '管理IP',
            'device_type': '设备类型',
            'other_ipaddress': '其他IP',
            'macaddress': 'MAC地址',
            'sn': 'SN号',
            'port_num': '端口个数',
            'idc': '机房',
            'manufactory': '厂商',
            'manage_user': '管理人',
            'device_detail': '配置详情',
            'status': '状态',
        }





