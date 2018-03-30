# -*- coding:utf-8 -*-

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
# from django.contrib.auth.models import Permission
# from django.contrib.auth import get_user_model

from permission.models import AssetActionPermission
from utils.mixins import BaseMixin, ViewPermissionListMixin



class NoActionPermissionView(BaseMixin, TemplateView):
    template_name = 'permission/no_action_permission.html'


class AssetActionPermissionListView(BaseMixin, ListView):
    model = AssetActionPermission
    template_name = 'permission/action_permission_list.html'
    context_object_name = 'permission_list'

    def get_context_data(self, **kwargs):
        return super(AssetActionPermissionListView, self).get_context_data(**kwargs)