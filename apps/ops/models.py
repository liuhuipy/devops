# -*- coding:utf-8 -*-

import uuid

from django.db import models

from assets.models import Asset, AssetGroup
from accounts.models import User


class AnsibleExecPlaybook(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    user = models.ForeignKey(User, related_name='exec_playbook_user', verbose_name='执行人')
    assets = models.ManyToManyField(Asset, related_name='shell_asset', blank=True, verbose_name='资产')
    asset_groups = models.ManyToManyField(AssetGroup, related_name='shell_asset', blank=True, verbose_name='资产组')
    playbook_shell = models.CharField(max_length=128, verbose_name='playbook命令')
    playbook_yaml_name = models.CharField(max_length=64, verbose_name='yaml入口文件')
    result = models.TextField(max_length=512, blank=True, null=True, verbose_name='返回结果')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '执行ansible剧本'
        verbose_name_plural = verbose_name


class AnsibleScript(models.Model):
    """Execute shell by ansible log"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    user = models.ForeignKey(User, related_name='shell_user', verbose_name='执行人')
    assets = models.ManyToManyField(Asset, related_name='shell_asset', blank=True, verbose_name='资产')
    asset_groups = models.ManyToManyField(AssetGroup, related_name='shell_asset', blank=True, verbose_name='资产组')
    shell = models.CharField(max_length=128, verbose_name='shell命令')
    script = models.TextField(max_length=512, blank=True, null=True, verbose_name='脚本')
    result = models.TextField(max_length=512, blank=True, null=True, verbose_name='返回结果')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '批量脚本命令'
        verbose_name_plural = verbose_name




