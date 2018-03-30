# -*- coding:utf-8 -*-

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from utils.mixins import BaseMixin
from accounts.models import UserGroup
from accounts.forms import UserGroupForm


class UserGroupListView(BaseMixin, ListView):
    model = UserGroup
    template_name = 'account/usergroup_list.html'
    context_object_name = 'usergroup_list'

    def get_queryset(self):
        usergroup_list = UserGroup.objects.order_by('-create_time')
        return usergroup_list

    def get_context_data(self, **kwargs):
        return super(UserGroupListView, self).get_context_data(**kwargs)


class UserGroupAddView(BaseMixin, PermissionRequiredMixin, CreateView):
    template_name = 'account/usergroup_add.html'
    form_class = UserGroupForm
    permission_required = 'assets.add_usergroup'
    success_url = reverse_lazy('usergroup_list')
    success_message = '用户组添加成功！'


class UserGroupDetailView(BaseMixin, PermissionRequiredMixin, DetailView):
    model = UserGroup
    template_name = 'account/usergroup_detail.html'
    permission_required = 'assets.get_usergroup'
    context_object_name = 'usergroup'
    pk_url_kwarg = 'usergroup_id'


class UserGroupUpdateView(BaseMixin, PermissionRequiredMixin, UpdateView):
    model = UserGroup
    template_name = 'account/usergroup_edit.html'
    form_class = UserGroupForm
    pk_url_kwarg = 'usergroup_id'
    permission_required = 'assets.change_usergroup'
    success_url = reverse_lazy('usergroup_list')
    success_message = '修改用户组信息成功！'


class UserGroupDelView(BaseMixin, PermissionRequiredMixin, DeleteView):
    model = UserGroup
    pk_url_kwarg = 'usergroup_id'
    permission_required = 'assets.delete_usergroup'
    success_url = reverse_lazy('usergroup_list')
