# -*- coding:utf-8 -*-

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, View
from django.db.models import Q
from django.urls import reverse_lazy

from utils.mixins import BaseMixin, ActionPermissionRequiredMixin
from accounts.models import UserGroup
from accounts.forms import UserGroupForm


class UserGroupListView(BaseMixin, ActionPermissionRequiredMixin, ListView):
    model = UserGroup
    template_name = 'account/usergroup_list.html'
    context_object_name = 'usergroup_list'
    permission_required = 'accounts.viewlist_usergroup'
    paginate_by = 10

    def get_queryset(self):
        usergroup_list = UserGroup.objects.order_by('-create_time')
        return usergroup_list

    def get_context_data(self, **kwargs):
        kwargs['paginate_by'] = self.paginate_by
        return super(UserGroupListView, self).get_context_data(**kwargs)


class UserGroupAddView(BaseMixin, ActionPermissionRequiredMixin, CreateView):
    template_name = 'account/usergroup_add.html'
    form_class = UserGroupForm
    permission_required = 'accounts.add_usergroup'
    success_url = reverse_lazy('accounts:usergroup_list')
    success_message = '用户组添加成功！'


class UserGroupDetailView(BaseMixin, ActionPermissionRequiredMixin, DetailView):
    model = UserGroup
    template_name = 'account/usergroup_detail.html'
    permission_required = 'accounts.view_usergroup'
    context_object_name = 'usergroup'
    pk_url_kwarg = 'usergroup_id'


class UserGroupUpdateView(BaseMixin, ActionPermissionRequiredMixin, UpdateView):
    model = UserGroup
    template_name = 'account/usergroup_edit.html'
    form_class = UserGroupForm
    pk_url_kwarg = 'usergroup_id'
    permission_required = 'accounts.change_usergroup'
    success_url = reverse_lazy('accounts:usergroup_list')
    success_message = '修改用户组信息成功！'


class UserGroupDelView(BaseMixin, ActionPermissionRequiredMixin, DeleteView):
    model = UserGroup
    pk_url_kwarg = 'usergroup_id'
    permission_required = 'accounts.delete_usergroup'
    success_url = reverse_lazy('accounts:usergroup_list')


class SearchUserGroupView(UserGroupListView):

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q:
            usergroup_list = UserGroup.objects.filter(Q(name__contains=q)).order_by('-create_time')
        else:
            usergroup_list = UserGroup.objects.order_by('-create_time')
        return usergroup_list
