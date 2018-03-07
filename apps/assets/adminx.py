# -*- coding:utf-8 -*-

import xadmin
from assets.models import IDC, Host, HostGroup, NetworkDevice


class IDCAdmin:
    list_display = ('name','address','phone','manage_user','network','operator','description','create_time','update_time')
    search_fields = ('name','address','phone','manage_user','network','operator')
    list_filter = ('name','address','manage_user__username','network','operator')


class HostAdmin:
    list_display = ('hostname','manage_ipaddress','macaddress','sn','hostgroup','idc','host_type','status')
    search_fields = ('hostname','manage_ipaddress','macaddress','sn','hostgroup','idc','host_type','status')
    list_filter = ('hostname','manage_ipaddress','macaddress','sn','hostgroup','idc','host_type','status')
    style_fields = {'content': 'ueditor', 'hostgroup': 'm2m_transfer'}


class HostGroupAdmin:
    list_display = ('name', 'description','create_time','update_time')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')


class NetWorkDeviceAdmin:
    list_display = ('device_name', 'manage_ipaddress','device_type','other_ipaddress', 'macaddress', 'sn',
                    'port_num', 'idc', 'manufactory', 'manage_user', 'device_detail', 'status')
    search_fields = ('device_name', 'manage_ipaddress','device_type','other_ipaddress', 'macaddress', 'sn',
                    'port_num', 'idc', 'manufactory', 'manage_user', 'device_detail', 'status')
    list_filter = ('device_name', 'manage_ipaddress','device_type','other_ipaddress', 'macaddress', 'sn',
                    'port_num', 'idc', 'manufactory', 'manage_user', 'device_detail', 'status')


xadmin.site.register(IDC, IDCAdmin)
xadmin.site.register(Host, HostAdmin)
xadmin.site.register(HostGroup, HostGroupAdmin)
xadmin.site.register(NetworkDevice, NetWorkDeviceAdmin)