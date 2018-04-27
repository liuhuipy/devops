# -*- coding:utf-8 -*-

from django.conf.urls import url

from accounts.views import user, usergroup

urlpatterns = [
    url(r'login/$', user.LoginView.as_view(), name='login'),
    url(r'logout/$', user.LogoutView.as_view(), name='logout'),

    # user action url
    url(r'user/list/$', user.UserListView.as_view(), name='user_list'),
    url(r'user/add/$', user.UserAddView.as_view(), name='user_add'),
    url(r'user/detail/(?P<user_id>\d+)/$', user.UserDetailView.as_view(), name='user_detail'),
    url(r'user/edit/(?P<user_id>\d+)/$', user.UserUpdateView.as_view(), name='user_edit'),
    url(r'user/del/(?P<user_id>\d+)/$', user.UserDelView.as_view(), name='user_del'),
    url(r'user/search/$', user.SearchUserView.as_view(), name='user_search'),

    # usergroup action url
    url(r'usergroup/list/$', usergroup.UserGroupListView.as_view(), name='usergroup_list'),
    url(r'usergroup/add/$', usergroup.UserGroupAddView.as_view(), name='usergroup_add'),
    url(r'usergroup/detail/(?P<usergroup_id>\d+)/$', usergroup.UserGroupDetailView.as_view(), name='usergroup_detail'),
    url(r'usergroup/edit/(?P<usergroup_id>\d+)/$', usergroup.UserGroupUpdateView.as_view(), name='usergroup_edit'),
    url(r'usergroup/del/(?P<usergroup_id>\d+)/$', usergroup.UserGroupDelView.as_view(), name='usergroup_del'),
    url(r'usergroup/search/$', usergroup.SearchUserGroupView.as_view(), name='usergroup_search')
]