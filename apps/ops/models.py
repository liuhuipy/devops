# -*- coding:utf-8 -*-

import uuid

from django.db import models

from assets.models import Asset, AssetGroup
from accounts.models import User


class AnsibleExecShellLog(models.Model):
    """Execute bash by ansible"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    user = models.ForeignKey(User, verbose_name='执行人')
    shell = models.CharField(max_length=256, verbose_name='命令')
    assets = models.ManyToManyField(Asset, related_name='bash_asset', blank=True, verbose_name='资产')
    asset_groups = models.ManyToManyField(AssetGroup, related_name='bash_assetgroup', blank=True, verbose_name='资产组')
    system_user = models.CharField(max_length=32, default='root', verbose_name='授权用户')
    result = models.TextField(max_length=4096, blank=True, null=True, verbose_name='返回结果')

    exec_time = models.DateTimeField(auto_now_add=True, verbose_name='执行时间')

    class Meta:
        verbose_name = '执行命令'
        verbose_name_plural = verbose_name
        permissions = (
            ('viewlist_ansibleexecshelllog', ('访问命令日志列表')),
            ('view_ansibleexecshelllog', ('查看命令日志')),
            ('add_ansibleexecshelllog', ('添加命令日志')),
            ('change_ansibleexecshelllog', ('修改命令日志')),
            ('delete_ansibleexecshelllog', ('删除命令日志')),
        )
        default_permissions = ()


class AnsiblePlaybook(models.Model):
    """ansible playbook"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=64, unique=True, verbose_name='名称')
    assets = models.ManyToManyField(Asset, related_name='playbook_asset', blank=True, verbose_name='资产')
    asset_groups = models.ManyToManyField(AssetGroup, related_name='playbook_assetgroup', blank=True, verbose_name='资产组')
    system_user = models.CharField(max_length=32, default='root', verbose_name='授权用户')
    playbook_file = models.FileField(max_length=64, upload_to='playbooks/', verbose_name='yaml文件路径')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '执行ansible剧本'
        verbose_name_plural = verbose_name
        permissions = (
            ('viewlist_ansibleplaybook', ('访问剧本列表')),
            ('view_ansibleplaybook', ('查看剧本')),
            ('add_ansibleplaybook', ('添加剧本')),
            ('change_ansibleplaybook', ('修改剧本')),
            ('delete_ansibleplaybook', ('删除剧本')),
        )
        default_permissions = ()


class AnsibleScript(models.Model):
    """script"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    script_name = models.CharField(max_length=64, unique=True, verbose_name='脚本名称')
    assets = models.ManyToManyField(Asset, related_name='shell_asset', blank=True, verbose_name='资产')
    asset_groups = models.ManyToManyField(AssetGroup, related_name='shell_assetgroup', blank=True, verbose_name='资产组')
    system_user = models.CharField(max_length=32, default='root', verbose_name='授权用户')
    script_file = models.TextField(max_length=1024, blank=True, null=True, verbose_name='脚本文件路径')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '执行脚本'
        verbose_name_plural = verbose_name
        permissions = (
            ('viewlist_ansiblescript', ('访问脚本列表')),
            ('view_ansiblescript', ('查看脚本')),
            ('add_ansiblescript', ('添加脚本')),
            ('change_ansiblescript', ('修改脚本')),
            ('delete_ansiblescript', ('删除脚本')),
        )
        default_permissions = ()


class AnsibleExecLog(models.Model):
    """Task audit"""
    ANISBLE_EXEC_TYPE_CHOICE = (
        ('playbook_exec', 'Playbook_Exec'),
        ('script_exec', 'Script_Exec'),
        ('other', 'Other'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    user = models.ForeignKey(User, verbose_name='执行人')
    exec_time = models.DateTimeField(auto_now_add=True, verbose_name='执行时间')
    assets = models.ManyToManyField(Asset, related_name='task_asset_log', blank=True, verbose_name='资产')
    asset_groups = models.ManyToManyField(AssetGroup, related_name='task_assetgroup_log', blank=True, verbose_name='资产组')
    system_user = models.CharField(max_length=32, default='root', verbose_name='授权用户')
    exec_type = models.CharField(max_length=32, choices=ANISBLE_EXEC_TYPE_CHOICE, verbose_name='执行类型')
    result = models.TextField(max_length=2048, blank=True, null=True, verbose_name='返回结果')

    class Meta:
        verbose_name = 'ansible操作日志'
        verbose_name_plural = verbose_name
        permissions = (
            ('viewlist_ansibleexeclog', ('访问ansible执行日志列表')),
            ('view_ansibleexeclog', ('查看ansible执行日志')),
            ('add_ansibleexeclog', ('添加ansible执行日志')),
            ('change_ansibleexeclog', ('修改ansible执行日志')),
            ('delete_ansibleexeclog', ('删除ansible执行日志')),
        )
        default_permissions = ()


class Crontab(models.Model):
    """The crontab such linux crontab"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=32, unique=True, verbose_name='任务名')
    miniute = models.CharField(max_length=16, default=None, verbose_name='分')
    hour = models.CharField(max_length=16, default=None, verbose_name='时')
    day = models.CharField(max_length=16, default=None, verbose_name='日')
    month = models.CharField(max_length=16, default=None, verbose_name='月')
    week = models.CharField(max_length=16, default=None, verbose_name='周')
    exec_playbook = models.ForeignKey(AnsiblePlaybook, blank=True, null=True, verbose_name='定时playbook任务')
    exec_script = models.ForeignKey(AnsibleScript, blank=True, null=True, verbose_name='定时脚本')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '定时任务'
        verbose_name_plural = verbose_name
        permissions = (
            ('viewlist_crontab', ('访问crontab列表')),
            ('view_crontab', ('查看crontab')),
            ('add_crontab', ('添加crontab')),
            ('change_crontab', ('修改crontab')),
            ('delete_crontab', ('删除crontab')),
        )
        default_permissions = ()
