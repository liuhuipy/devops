# -*- coding:utf-8 -*-

import xadmin
from xadmin import views

from .models import UserGroup


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = "Devops自动化运维"
    site_footer = "基于Python3.5、Django1.10开发"
    menu_style = "accordion"


class UserGroupAdmin:
    list_display = ('name','description','create_time','update_time')
    search_fields = ('name','description')
    list_filter = ('name','description')


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(UserGroup, UserGroupAdmin)