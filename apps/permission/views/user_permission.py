# -*- coding:utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import get_user_model

from utils.mixins import BaseMixin
from permission.models import AssetActionPermission, UrlViewPermission

User = get_user_model()


class UserPermissionListView(BaseMixin, DetailView):
    model = User
    template_name = 'permission/user_permission_list.html'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        id = self.kwargs.get(self.pk_url_kwarg)
        user_permission_list = {}
        user = User.objects.get(id=id)
        user_permission_list = user.user_asset_permission.all()
        print(user_permission_list)
        # for permission in user.get_all_permissions():
        #     key += 1
        #     user_permission_list[key] = {}
        #     user_permission_list[key]['app'] = permission.split('.')[0]
        #     user_permission_list[key]['action'] = permission.split('.')[1].split('_')[0]
        #     user_permission_list[key]['object'] = permission.split('.')[1].split('_')[1]
        kwargs['user_permission_list'] = user_permission_list
        return super(UserPermissionListView, self).get_context_data(**kwargs)