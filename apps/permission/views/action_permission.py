# -*- coding:utf-8 -*-

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.contrib.auth.models import Permission

from utils.mixins import BaseMixin, ActionPermissionRequiredMixin



class NoActionPermissionView(BaseMixin, TemplateView):
    template_name = 'permission/no_action_permission.html'


class AssetActionPermissionListView(BaseMixin, ActionPermissionRequiredMixin, ListView):
    model = Permission
    template_name = 'permission/action_permission_list.html'
    context_object_name = 'permission_list'
    permission_required = 'permission.view_permission'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        return super(AssetActionPermissionListView, self).get_context_data(**kwargs)