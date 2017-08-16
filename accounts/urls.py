__author__ = 'liuhui'


from django.conf.urls import url, include
from django.contrib import admin

from accounts.views import user

urlpatterns = [
    url(r'login/$', user.login, name='login'),
    url(r'logout/$', user.logout, name='logout'),
    url(r'user_list/$', user.UserListView.as_view(), name='user_list'),
    url(r'user_add/$', user.user_add, name='user_add'),
]