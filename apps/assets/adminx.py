# -*- coding:utf-8 -*-

import xadmin
from assets.models import IDC, Asset, AssetGroup


class IDCAdmin:
    list_display = ('name','address','phone','manage_user','network','operator','description','create_time','update_time')
    search_fields = ('name','address','phone','manage_user','network','operator')
    list_filter = ('name','address','manage_user__username','network','operator')


class AssetAdmin:
    list_display = ('id', 'asset_name','manage_ipaddress','asset_type','macaddress','sn','asset_group','idc','status')
    search_fields = ('asset_name','manage_ipaddress','asset_type','macaddress','sn','asset_group','idc','status')
    list_filter = ('asset_name','manage_ipaddress','asset_type','macaddress','sn','asset_group','idc','status')
    style_fields = {'asset_group': 'm2m_transfer'}


class AssetGroupAdmin:
    list_display = ('name', 'description','create_time','update_time')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')


xadmin.site.register(IDC, IDCAdmin)
xadmin.site.register(Asset, AssetAdmin)
xadmin.site.register(AssetGroup, AssetGroupAdmin)
