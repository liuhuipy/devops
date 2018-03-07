# -*- coding:utf-8 -*-

from django.forms import ModelForm
from django import forms
from django.contrib import auth
from accounts.models import User

error_messages = {
    'username': {
        'required': u'用户名不能为空',
        'min_length': u'用户名长度过短（4-16个字符）',
        'max_length': u'用户名长度过长（4-16个字符）',
        'invalid': u'用户名必须由英文(开头)，数字，下划线构成',
    },
    'email': {
        'required': u'E-mail不能为空',
        'min_length': u'Email长度过短',
        'max_length': u'Email长度过长',
        'invalid': u'电子邮件格式不正确',
    },
    'password': {
        'required': u'密码不能为空',
        'min_length': u'密码长度过短（6-16个字符）',
        'max_length': u'密码长度过长（6-16个字符）',
    }
}


class LoginForm(forms.Form):
    username = forms.CharField(label=u'用户名', min_length=4, max_length=32, error_messages=error_messages.get('username'))
    password = forms.CharField(label=u'密码', min_length=6, max_length=16, error_messages=error_messages.get('password'))

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = auth.authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(u'用户名或密码错误')
            elif not self.user_cache.is_active:
                raise forms.ValidationError(u'用户已被锁定，请联系管理员解锁')
        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email', 'password', 'is_active')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','style': 'width:300px;'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','style': 'width:300px;'}),
            'email': forms.EmailInput(attrs={'class': ' form-control','style': 'width:300px;'}),
            'is_active': forms.Select(choices=((True, u'启用'),(False, u'禁用')), attrs={'class': 'form-control','style': 'width:300px;'}),
        }
        labels = {
            'username': u'用户名',
            'email': u'邮箱',
            'password': u'密码',
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
