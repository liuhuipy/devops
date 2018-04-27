# -*- coding:utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import get_user_model

from utils.mixins import BaseMixin

User = get_user_model()


class UserPermissionListView(BaseMixin, ListView):
    model = User
    template_name = 'permission/user_permission_list.html'
    pk_url_kwarg = 'user_id'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        id = self.kwargs.get(self.pk_url_kwarg)
        user = User.objects.get(id=id)
        user_permission_list = {}
        for permission in user.get_all_permissions():
            temp = permission.split('.')[1].split('_')
            if temp[1] not in user_permission_list:
                user_permission_list[temp[1]] = []
            user_permission_list[temp[1]].append(temp[0])
        kwargs['user_permission_list'] = user_permission_list
        return super(UserPermissionListView, self).get_context_data(**kwargs)