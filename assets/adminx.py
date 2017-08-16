#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


import xadmin

from assets.models import IDC, Host, HostGroup, NetworkDevice

class IDCAdmin():
    list_display = ('name','address','phone','linkman','email','network','operator','remark','create_time')
    search_fields = ('name','address','phone','linkman','email','network','operator','remark')
    list_filter = ('name','address','linkman__username','operator')


class HostAdmin():
    list_display = ('hostname', 'hostgroup','ipaddress','macaddress','os_type','os_version','Manufactory','sn','cpu_model','cpu_num','cpu_physical','memory','idc','status','remark')
    search_fields = ('hostname', 'hostgroup','ipaddress','macaddress','os_type','Manufactory','sn','idc','status')
    list_filter = ('hostname','hostgroup__name','ipaddress','os_type','os_version','Manufactory','sn','idc__name','status')


class HostGroupAdmin():
    list_display = ('name', 'remark')
    search_fields = ('name', 'remark')
    list_filter = ('name', 'remark')


class NetWorkDeviceAdmin():
    list_display = ('name', 'sn', 'type', 'user', 'Manufactory', 'idc', 'vlan_ip', 'intranet_ip', 'model', 'port_num', 'status', 'device_detail')
    search_fields = ('name', 'sn', 'type', 'user', 'Manufactory', 'idc', 'vlan_ip', 'intranet_ip', 'model', 'port_num', 'status')
    list_filter = ('name', 'sn', 'type', 'user__username', 'Manufactory', 'idc__name', 'vlan_ip', 'intranet_ip', 'model', 'port_num', 'status', 'device_detail')


xadmin.site.register(IDC, IDCAdmin)
xadmin.site.register(Host, HostAdmin)
xadmin.site.register(HostGroup, HostGroupAdmin)
xadmin.site.register(NetworkDevice, NetWorkDeviceAdmin)