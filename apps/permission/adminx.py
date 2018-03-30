# -*- coding:utf-8 -*-

import xadmin
from permission.models import AssetActionPermission, UrlViewPermission


class AssetActionPermissioinAdmin:
    list_display = ('name', 'users', 'user_groups', 'assets', 'asset_groups', 'can_view', 'can_add', 'can_change',
                    'can_delete', 'is_active')
    search_fields = ('name', 'users', 'user_groups', 'assets', 'asset_groups', 'can_view', 'can_add', 'can_change',
                    'can_delete', 'is_active')
    list_filter = ('name', 'users', 'user_groups', 'assets', 'asset_groups', 'can_view', 'can_add', 'can_change',
                    'can_delete', 'is_active')
    style_fields = {'users': 'm2m_transfer', 'user_groups': 'm2m_transfer',
                    'assets': 'm2m_transfer', 'asset_groups': 'm2m_transfer'}


class UrlViewPermissionAdmin:
    list_display = ('users', 'user_groups', 'url', 'is_active', 'description')
    search_fields = ('users', 'user_groups', 'url', 'is_active', 'description')
    list_filter = ('users', 'user_groups', 'url', 'is_active', 'description')
    style_fields = {'users': 'm2m_transfer', 'user_groups': 'm2m_transfer'}


xadmin.site.register(AssetActionPermission, AssetActionPermissioinAdmin)
xadmin.site.register(UrlViewPermission, UrlViewPermissionAdmin)