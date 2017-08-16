#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


from django.forms import ModelForm
from django import forms
from django.contrib import auth
from accounts.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(label=u'邮箱', min_length=4, max_length=32, error_messages={'required': '用户名不能为空'})
    password = forms.CharField(label=u'密 码', min_length=6, max_length=16, error_messages={'required': u'密码不能为空'})

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None

        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = auth.authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(u'用户邮箱密码不匹配')
            elif not self.user_cache.is_active:
                raise forms.ValidationError(u'此账号已被禁用')
        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class UserAddForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username','email', 'password', 'role', 'is_active')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','style': 'width:300px;'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','style': 'width:300px;'}),
            'email': forms.EmailInput(attrs={'class': ' form-control','style': 'width:300px;'}),
            'role': forms.Select(attrs={'class': 'form-control','style': 'width:300px;'}),
            'is_active': forms.Select(choices=((True, u'启用'),(False, u'禁用')), attrs={'class': 'form-control','style': 'width:300px;'}),
        }
        labels = {
            'username': u'用户名',
            'email': u'邮箱',
            'password': u'密码',
            'role': u'角色',
            'is_active': u'状态',
        }
        error_messages = {
            'username': {
                'required': u'请输入用户名',
                'max_length': u'用户名过长',
            },
            'email': {
                'required': u'请输入邮箱',
                'max_length': u'邮箱地址过长',
            },
            'password': {
                'required': u'请输入密码',
                'max_length': u'密码过长',
                'invalid': u'请输入有效邮箱'
            }
        }

    def __init__(self,*args,**kwargs):
        super(UserAddForm,self).__init__(*args,**kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError(u'用户名必须大于4位')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError(u'密码必须大于6位')
        return password
