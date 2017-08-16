#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q

from accounts.models import UserProfile
from django.conf import settings
from accounts.forms import LoginForm, UserAddForm

@login_required
def index(request):
    return render(request, 'index.html')

class UserListView(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'account/user_list.html'
    context_object_name = 'user_list'
    paginate_by = settings.PAGE_NUM

    def get_queryset(self):
        user_list = UserProfile.objects.all()
        user_filter = self.request.GET.get('q')
        if user_filter:
            user_list = user_list.filter(Q(email__contains=user_filter)|
                                         Q(username__contains=user_filter)|
                                         Q(role__name__contains=user_filter)|
                                         Q(is_active__in=user_filter))
        return user_list

    def get_context_data(self, **kwargs):
        return super(UserListView, self).get_context_data(**kwargs)


@csrf_protect
def login(request):
    if request.method == 'POST':
        loginform = LoginForm(request, request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('index'))
            print('bb')
        print('cc')
    else:
        loginform = LoginForm()
        print('aa')
        user = None
    return render(request, 'account/login.html', {'form':loginform})


@csrf_protect
@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def user_add(request):
    if request.method == "POST":
        userform = UserAddForm(request.POST)
        if userform.is_valid():
            user = userform.save(commit=False)
            user.set_password(userform.cleaned_data['password'])
            userform.save()
            return HttpResponseRedirect(reverse('user_list'))
    else:
        userform = UserAddForm()
    return render(request, 'account/user_add.html', locals())





