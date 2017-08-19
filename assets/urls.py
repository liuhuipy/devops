__author__ = 'liuhui'

from django.conf.urls import url, include
from django.contrib import admin
from assets.views import asset_report, host, idc, hostgroup, networkdevice

urlpatterns = [
    url(r'report/asset_with_no_asset_id', asset_report.asset_with_no_asset_id, name="asset_with_no_asset_id"),
    url(r'report/$', asset_report.asset_report, name='asset_report'),
    url(r'host_list/$', host.HostListView.as_view(), name='host_list'),
    url(r'host/add/$', host.HostAdd, name='host_add'),
    url(r'host/del/$', host.HostDel, name='host_del'),
    #url(r'host/edit/(?P<ids>\d+)/$', host.host_edit, name='host_edit'),
    url(r'hostgroup_list/$', hostgroup.HostGroupListView.as_view(), name='hostgroup_list'),
    url(r'hostgroup/add/$', hostgroup.HostGroupAdd, name='hostgroup_add'),
    url(r'idc_list/$', idc.IDCListView.as_view(), name='idc_list'),
    url(r'idc_add/$', idc.IDCAdd, name='idc_add'),
    url(r'networkdevice_list/$', networkdevice.NetworkDeviceListView.as_view(), name='networkdevice_list'),
    url(r'networkdevice_add/$', networkdevice.NetworkDeviceAdd, name='networkdevice_add'),
]