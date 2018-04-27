# -*- coding:utf-8 -*-

import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserGroup(models.Model):
    name = models.CharField(max_length=64, verbose_name='用户组名')
    description = models.CharField(max_length=256, blank=True, null=True, verbose_name='描述')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '用户组'
        verbose_name_plural = verbose_name
        permissions = (
            ('viewlist_usergroup', ('访问用户组列表')),
            ('view_usergroup', ('查看用户组')),
            ('add_usergroup', ('添加用户组')),
            ('change_usergroup', ('编辑用户组')),
            ('delete_usergroup', ('删除用户组')),
        )
        default_permissions = ()

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(max_length=255,unique=True, blank=True, null=True, verbose_name='邮箱')
    username = models.CharField(max_length=32,unique=True, verbose_name='用户名')
    password = models.CharField(max_length=128,verbose_name='密码')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='电话')
    image = models.ImageField(max_length=128, upload_to='user_images/%Y/%m/%d', blank=True, null=True,
                              default='default.png', verbose_name='头像')
    user_group = models.ManyToManyField(UserGroup, related_name='user_group', verbose_name='用户组')
    is_superuser = models.BooleanField(default=False, verbose_name='是否为超级管理员')
    is_staff = models.BooleanField(default=False, verbose_name='是否为管理员')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    is_online = models.BooleanField(default=False, verbose_name='是否在线')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        permissions = (
            ('viewlist_user', ('访问用户列表')),
            ('view_user', ('查看用户')),
            ('add_user', ('添加用户')),
            ('change_user', ('编辑用户')),
            ('delete_user', ('删除用户')),
        )
        default_permissions = ()

    def __str__(self):  # __unicode__ on Python 2
        return self.username


class UserLoginLog(models.Model):
    """User login log"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    user = models.ForeignKey(User, verbose_name='用户')
    ipaddress = models.GenericIPAddressField(verbose_name='IP地址')
    login_time = models.DateTimeField(auto_now_add=True, verbose_name='登陆时间')
    logout_time = models.DateTimeField(blank=True, null=True, verbose_name='登出时间')

    class Meta:
        verbose_name = '用户登陆日志'
        verbose_name_plural = verbose_name
        permissions = (
            ('viewlist_userloginlog', ('访问用户登录日志列表')),
            ('view_userloginlog', ('查看用户登录日志')),
            ('add_userloginlog', ('添加用户登录日志')),
            ('change_userloginlog', ('编辑用户登录日志')),
            ('delete_userloginlog', ('删除用户登录日志')),
        )
        default_permissions = ()