# -*- coding:utf-8 -*-

from django.conf.urls import url
from assets.views import asset, assetgroup, idc


urlpatterns = [
    # url(r'report/asset_with_no_asset_id', asset_report.asset_with_no_asset_id, name="asset_with_no_asset_id"),
    # url(r'report/$', asset_report.asset_report, name='asset_report'),

    # host action url
    url(r'asset/list/$', asset.AssetListView.as_view(), name='asset_list'),
    url(r'asset/add/$', asset.AssetAddView.as_view(), name='asset_add'),
    url(r'asset/detail/(?P<asset_id>[0-9a-zA-Z\-]{36})/$', asset.AssetDetailView.as_view(), name='asset_detail'),
    url(r'asset/edit/(?P<asset_id>[0-9a-zA-Z\-]{36})/$', asset.AssetUpdateView.as_view(), name='asset_edit'),
    url(r'asset/del/(?P<asset_id>[0-9a-zA-Z\-]{36})/$', asset.AssetDelView.as_view(), name='asset_del'),

    # hostgroup action url
    url(r'Assetgroup/list/$', assetgroup.AssetGroupListView.as_view(), name='assetgroup_list'),
    url(r'Assetgroup/add/$', assetgroup.AssetGroupAddView.as_view(), name='assetgroup_add'),
    url(r'Assetgroup/detail/(?P<assetgroup_id>[0-9a-zA-Z\-]{36})/$', assetgroup.AssetGroupDetailView.as_view(), name='assetgroup_detail'),
    url(r'Assetgroup/edit/(?P<assetgroup_id>[0-9a-zA-Z\-]{36})/$', assetgroup.AssetGroupUpdateView.as_view(), name='assetgroup_edit'),
    url(r'Assetgroup/del/(?P<assetgroup_id>[0-9a-zA-Z\-]{36})/$', assetgroup.AssetGroupDelView.as_view(), name='assetgroup_del'),

    # idc action url
    url(r'idc/list/$', idc.IDCListView.as_view(), name='idc_list'),
    url(r'idc/add/$', idc.IDCAddView.as_view(), name='idc_add'),
    url(r'idc/detail/(?P<idc_id>[0-9a-zA-Z\-]{36})/$', idc.IDCDetailView.as_view(), name='idc_detail'),
    url(r'idc/edit/(?P<idc_id>[0-9a-zA-Z\-]{36})/$', idc.IDCUpdateView.as_view(), name='idc_edit'),
    url(r'idc/del/(?P<idc_id>[0-9a-zA-Z\-]{36})/$', idc.IDCDelView.as_view(), name='idc_del'),
]