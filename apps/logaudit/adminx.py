# -*- coding:utf-8 -*-

import xadmin
from logaudit.models import Log


class LogAdmin:
    list_display = ('user','time','object','log_type')
    search_fields = ('user','time','object','log_type')
    list_filter = ('user','time','object','log_type')

xadmin.site.register(Log, LogAdmin)