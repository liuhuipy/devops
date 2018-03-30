# -*- coding:utf-8 -*-

from django.conf.urls import url

from permission.views import url_view_permission, action_permission, user_permission

urlpatterns = [
    url(r'noviewpermission/$', url_view_permission.NoViewPermissionView.as_view(), name='no_view_permission'),
    url(r'noactionpermission/$', action_permission.NoActionPermissionView.as_view(), name='no_action_permission'),
    url(r'userpermission/list/(?P<user_id>\d+)/$', user_permission.UserPermissionListView.as_view(), name='user_permission_list'),

    # action permission url
    url(r'actionpermission/list/$', action_permission.AssetActionPermissionListView.as_view(), name='action_permission_list'),
]