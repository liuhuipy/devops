# -*- coding:utf-8 -*-

import xadmin

from ops.models import AnsibleExecShellLog, AnsibleScript, AnsiblePlaybook, AnsibleExecLog, Crontab


class AnsibleExecShellLogAdmin:
    list_display = ('user','shell','assets','asset_groups','system_user','exec_time','result')
    search_fields = ('user','shell','assets','asset_groups','system_user','exec_time','result')
    list_filter = ('user','shell','assets','asset_groups','system_user','exec_time','result')
    style_fields = {'content': 'ueditor', 'assets': 'm2m_transfer','asset_groups': 'm2m_transfer'}

xadmin.site.register(AnsibleExecShellLog, AnsibleExecShellLogAdmin)

