# -*- coding:utf-8 -*-

from django.views.generic import TemplateView

from utils.mixins import BaseMixin


class NoViewPermissionView(BaseMixin, TemplateView):
    template_name = 'permission/no_view_permission.html'

