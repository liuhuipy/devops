# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.generic import ListView, FormView, View
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q

from accounts.models import User
from django.conf import settings
from accounts.forms import LoginForm, UserAddForm


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'account/login.html'
    context_object_name = 'user_list'
    paginate_by = settings.PAGE_NUM

    def get_queryset(self):
        user_list = User.objects.all()
        user_filter = self.request.GET.get('q')
        if user_filter:
            user_list = user_list.filter(Q(email__contains=user_filter)|
                                         Q(username__contains=user_filter)|
                                         Q(role__name__contains=user_filter)|
                                         Q(is_active__in=user_filter))
        return user_list

    def get_context_data(self, **kwargs):
        return super(UserListView, self).get_context_data(**kwargs)


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
        return redirect('login')

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





