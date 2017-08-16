#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


import xadmin
from xadmin import views

from accounts.models import RoleList, PermissionList, UserProfile


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings():
    site_title = "自动化运维"
    site_footer = "基于Python3.5、Django1.10开发"
    menu_style = "accordion"


class RoleListAdmin():
    list_display = ('name', 'permission')
    search_fields = ('name', 'permission')
    list_filter = ('name', 'permission__name')


class PermissionListAdmin():
    list_display = ('name', 'url')
    search_fields = ('name', 'url')
    list_filter = ('name', 'url')


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(RoleList, RoleListAdmin)
xadmin.site.register(PermissionList, PermissionListAdmin)

