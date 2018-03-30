# -*- coding:utf-8 -*-
# user action permission such as add、change、get、delete object permission use Django default Permission.
# user url view permission used UrlViewPermission.

import uuid

from django.db import models

from assets.models import Asset, AssetGroup
from accounts.models import User, UserGroup


class AssetActionPermission(models.Model):
    """Asset action permission"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128, unique=True, verbose_name='权限名')
    users = models.ManyToManyField(User, related_name='user_asset_permission', blank=True, verbose_name='用户')
    user_groups = models.ManyToManyField(UserGroup, related_name='user_asset_permission', blank=True, verbose_name='用户组')
    assets = models.ManyToManyField(Asset, related_name='asset_permission', blank=True, verbose_name='资产')
    asset_groups = models.ManyToManyField(AssetGroup, related_name='asset_permission', blank=True, verbose_name='资产组')

    can_view = models.BooleanField(default=False, verbose_name='是否可查看')
    can_add = models.BooleanField(default=False, verbose_name='是否可添加')
    can_change = models.BooleanField(default=False, verbose_name='是否可更新')
    can_delete = models.BooleanField(default=False, verbose_name='是否可删除')

    is_active = models.BooleanField(default=True, verbose_name='激活')
    description = models.CharField(max_length=256, blank=True, null=True, verbose_name='描述')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '资产操作权限'
        verbose_name_plural = verbose_name


class UrlViewPermission(models.Model):
    """Url view permission"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    users = models.ManyToManyField(User, blank=True, verbose_name='用户')
    user_groups = models.ManyToManyField(UserGroup, blank=True, verbose_name='用户组')
    url = models.URLField(verbose_name='URL')
    is_active = models.BooleanField(default=True, verbose_name='激活')
    description = models.CharField(max_length=256, blank=True, null=True, verbose_name='描述')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    class Meta:
        verbose_name = 'URL访问权限'
        verbose_name_plural = verbose_name

