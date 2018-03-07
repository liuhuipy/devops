# -*- coding:utf-8 -*-

from django.conf.urls import url
from assets.views import asset_report, host, idc, hostgroup, networkdevice


urlpatterns = [
    url(r'report/asset_with_no_asset_id', asset_report.asset_with_no_asset_id, name="asset_with_no_asset_id"),
    url(r'report/$', asset_report.asset_report, name='asset_report'),

    # Host action url
    url(r'host/list/$', host.HostListView.as_view(), name='host_list'),
    url(r'host/add/$', host.HostAddView.as_view(), name='host_add'),
    url(r'host/detail/(?P<host_id>[0-9a-zA-Z\-]{36})/$', host.HostDetailView.as_view(), name='host_detail'),
    url(r'host/edit/(?P<host_id>[0-9a-zA-Z\-]{36})/$', host.HostUpdateView.as_view(), name='host_edit'),
    url(r'host/del/(?P<host_id>[0-9a-zA-Z\-]{36})/$', host.HostDelView.as_view(), name='host_del'),

    # Hostgroup action url
    url(r'hostgroup/list/$', hostgroup.HostGroupListView.as_view(), name='hostgroup_list'),
    url(r'hostgroup/add/$', hostgroup.HostGroupAddView.as_view(), name='hostgroup_add'),
    url(r'hostgroup/detail/(?P<hostgroup_id>\d+)/$', hostgroup.HostGroupDetailView.as_view(), name='hostgroup_detail'),
    url(r'hostgroup/edit/(?P<hostgroup_id>\d+)/$', hostgroup.HostGroupUpdateView.as_view(), name='hostgroup_edit'),
    url(r'hostgroup/del/(?P<hostgroup_id>\d+)/$', hostgroup.HostGroupDelView.as_view(), name='hostgroup_del'),

    # idc action url
    url(r'idc/list/$', idc.IDCListView.as_view(), name='idc_list'),
    url(r'idc/add/$', idc.IDCAddView.as_view(), name='idc_add'),
    url(r'idc/detail/(?P<idc_id>\d+)/$', idc.IDCDetailView.as_view(), name='idc_detail'),
    url(r'idc/edit/(?P<idc_id>\d+)/$', idc.IDCUpdateView.as_view(), name='idc_edit'),
    url(r'idc/del/(?P<idc_id>\d+)/$', idc.IDCDelView.as_view(), name='idc_del'),

    # networkdevice action url
    url(r'networkdevice/list/$', networkdevice.NetworkDeviceListView.as_view(), name='networkdevice_list'),
    url(r'networkdevice/add/$', networkdevice.NetworkDeviceAddView.as_view(), name='networkdevice_add'),
    url(r'networkdevice/detail/(?P<networkdevice_id>[0-9a-zA-Z\-]{36})/$',
        networkdevice.NetworkDeviceDetailView.as_view(), name='networkdevice_detail'),
    url(r'networkdevice/edit/(?P<networkdevice_id>[0-9a-zA-Z\-]{36})/$',
        networkdevice.NetworkDeviceUpdateView.as_view(),name='networkdevice_edit'),
    url(r'networkdevice/del/(?P<networkdevice_id>[0-9a-zA-Z\-]{36})/$',
        networkdevice.NetworkDeviceDelView.as_view(),name='networkdevice_del'),
]