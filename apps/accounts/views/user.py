# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.db.models import Q

from accounts.models import User
from accounts.forms import LoginForm, UserForm
from utils.mixins import BaseMixin, ActionPermissionRequiredMixin


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        return super(LoginView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        login_form = AuthenticationForm(data=self.request.POST, request=self.request)
        if login_form.is_valid():
            user = login_form.get_user()
            if user is not None:
                auth_login(self.request, user)
                return redirect('index')
        else:
            auth_logout(form)
            return render('account/login.html', {'errors': login_form.errors})

    def get_success_url(self):
        return redirect('index')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        auth_logout(request)
        return redirect('accounts:login')


class UserListView(BaseMixin, ActionPermissionRequiredMixin, ListView):
    model = User
    template_name = 'account/user_list.html'
    context_object_name = 'user_list'
    permission_required = 'accounts.viewlist_user'
    paginate_by = 10

    def get_queryset(self):
        user_list = User.objects.order_by('-create_time')
        return user_list

    def get_context_data(self, **kwargs):
        kwargs['paginate_by'] = self.paginate_by
        return super(UserListView, self).get_context_data(**kwargs)


class UserAddView(BaseMixin, ActionPermissionRequiredMixin, CreateView):
    template_name = 'account/user_add.html'
    form_class = UserForm
    permission_required = 'accounts.add_user'
    success_url = reverse_lazy('accounts:user_list')
    success_message = '用户添加成功！'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super(UserAddView, self).form_valid(form)


class UserDetailView(BaseMixin, ActionPermissionRequiredMixin, DetailView):
    model = User
    template_name = 'account/user_detail.html'
    permission_required = 'accounts.view_user'
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'


class UserUpdateView(BaseMixin, ActionPermissionRequiredMixin, UpdateView):
    model = User
    template_name = 'account/user_edit.html'
    form_class = UserForm
    pk_url_kwarg = 'user_id'
    permission_required = 'accounts.change_user'
    success_url = reverse_lazy('accounts:user_list')
    success_message = '修改用户信息成功！'


class UserDelView(BaseMixin, ActionPermissionRequiredMixin, DeleteView):
    model = User
    pk_url_kwarg = 'user_id'
    permission_required = 'accounts.delete_user'
    success_url = reverse_lazy('accounts:user_list')


class SearchUserView(UserListView):

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q:
            usergroup_list = User.objects.filter(Q(username__contains=q)).order_by('-create_time')
        else:
            usergroup_list = User.objects.order_by('-create_time')
        return usergroup_list


