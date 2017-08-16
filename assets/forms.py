#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

from django.forms import ModelForm
from django.forms.widgets import *

from assets.models import Host, HostGroup, NetworkDevice, IDC



class HostForm(ModelForm):
    class Meta:
        model = Host
        exclude = ('id',)
        widgets = {
            'hostname': TextInput(attrs={'class': 'form-control','style': 'width:300px;', 'placeholder': u'hostname'}),
            'hostgroup': Select(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'hostgroup'}),
            'idc': Select(attrs={'class': 'from-control','style': 'width:300px;','placeholder': u'idc'}),
            'ipaddress': TextInput(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'ipaddress'}),
            'macaddress': TextInput(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'macaddress'}),
            'os_type': TextInput(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'os_type'}),
            'os_version': TextInput(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'os_version'}),
            'Manufactory': TextInput(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'Manufactroy'}),
            'sn': TextInput(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'sn'}),
            'cpu_model': TextInput(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'cpu_model'}),
            'cpu_num': TextInput(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'cpu_num'}),
            'cpu_physical': TextInput(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'cpu_physical'}),
            'memory': TextInput(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'memory'}),
            'disk': TextInput(attrs={'class': 'form-control','style': 'width:300px;','placeholder': u'disk'}),
            'status': Select(attrs={'class': 'from-control','style': 'width:300px;','placeholder': u'status'}),
            'remark': Textarea(attrs={'class': 'form-control','style': 'width:400px;','placeholder': u'remark'}),
        }
        labels = {
            'hostname': u'主机名',
            'hostgroup': u'所属主机组',
            'idc': u'所属机房',
            'ipaddress': u'IP地址',
            'macaddress': u'MAC地址',
            'os_type': u'操作系统类型',
            'os_version': u'操作系统版本',
            'Manufactory': u'厂商',
            'sn': u'SN号',
            'cpu_model': u'CPU型号',
            'cpu_num': u'物理CPU数量',
            'cpu_physical': u'逻辑CPU数量',
            'memory': u'内存大小',
            'disk': u'硬盘大小',
            'status': u'资产状态',
            'remark': u'备注',
        }

class HostGroupForm(ModelForm):
    class Meta:
        model = HostGroup
        exclude = ('id',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','style': 'width:300px;', 'placeholder': u'name'}),
            'remark': Textarea(attrs={'class': 'form-control', 'style': 'width:400px;', 'placeholder': u'remark'}),
        }
        labels = {
            'name': u'主机组名',
            'remark': u'备注',
        }


class IDCForm(ModelForm):
    class Meta:
        model = IDC
        exclude = ('id',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','style': 'width:300px;', 'placeholder': u'name'}),
            'address': TextInput(attrs={'class': 'form-control', 'style': 'width:400px;', 'placeholder': u'address'}),
            'phone': TextInput(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'phone'}),
            'linkman': Select(attrs={'class': 'form-control', 'style': 'width:400px;', 'placeholder': u'linkman'}),
            'email': EmailInput(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'email'}),
            'network': TextInput(attrs={'class': 'form-control', 'style': 'width:400px;', 'placeholder': u'network'}),
            'operator': Select(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'operator'}),
            'remark': Textarea(attrs={'class': 'form-control', 'style': 'width:400px;', 'placeholder': u'remark'}),

        }
        labels = {
            'name': u'机房名',
            'address': u'机房地址',
            'phone': u'联系电话',
            'linkman': u'联系人',
            'email': u'邮箱',
            'network': u'IP地址范围',
            'operator': u'运营商',
            'remark': u'备注'
        }


class NetworkDeviceForm(ModelForm):
    class Meta:
        model = NetworkDevice
        exclude = ('id',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','style': 'width:300px;', 'placeholder': u'name'}),
            'sn': TextInput(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'sn'}),
            'type': Select(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'type'}),
            'user': Select(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'user'}),
            'Manufactory': TextInput(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'Manufactory'}),
            'idc': Select(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'idc'}),
            'vlan_ip': TextInput(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'vlan_ip'}),
            'intranet_ip': TextInput(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'intranet_ip'}),
            'model': TextInput(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'model'}),
            'port_num': TextInput(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'port_num'}),
            'status': Select(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'status'}),
            'device_detail': Textarea(attrs={'class': 'form-control', 'style': 'width:300px;', 'placeholder': u'device_detail'}),
        }
        labels = {
            'name': u'设备名称',
            'sn': u'SN号',
            'type': u'设备类型',
            'user': u'设备管理员',
            'Manufactory': u'厂商',
            'idc': u'所属机房',
            'vlan_ip': u'vlan IP地址',
            'intranet_ip': u'内网IP地址',
            'model': u'型号',
            'port_num': u'端口数',
            'status': u'状态',
            'device_detail': u'配置详情',
        }


