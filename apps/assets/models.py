# -*- coding:utf-8 -*-

import uuid

from django.db import models
from accounts.models import User


class IDC(models.Model):
    """add IDC table"""
    IDC_OPERATOR_CHOICES = (
        (1, '电信'),
        (2, '联通'),
        (3, '移动'),
        (4, '铁通'),
        (5, '其他'),
    )
    name = models.CharField(max_length=64, verbose_name='机房名')
    address = models.CharField(max_length=128, verbose_name='所在地址')
    phone = models.CharField(max_length=32, blank=True, null=True, verbose_name='联系电话')
    manage_user = models.ForeignKey(User, blank=True, null=True, verbose_name='管理人')
    network = models.CharField(max_length=32, blank=True, null=True, verbose_name='所在网段')
    operator = models.SmallIntegerField(choices=IDC_OPERATOR_CHOICES, default=1, verbose_name='运营商')
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name='描述')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '机房'
        verbose_name_plural = verbose_name
        permissions = (
            ('get_idc', ('查看机房')),
            ('add_idc', ('添加机房')),
            ('edit_idc', ('编辑机房')),
            ('del_idc', ('删除机房')),
        )
        default_permissions = ()

    def __str__(self):
        return self.name


class HostGroup(models.Model):
    """add HostGroup table"""
    name = models.CharField(max_length=32, unique=True, verbose_name='主机组')
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='描述')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    class Meta:
        # ordering = ['-create_time']
        verbose_name = '主机组'
        verbose_name_plural = verbose_name
        permissions = (
            ('get_hostgroup', ('查看主机组')),
            ('add_hostgroup', ('添加主机组')),
            ('edit_hostgroup', ('编辑主机组')),
            ('del_hostgroup', ('删除主机组')),
        )
        default_permissions = ()

    def __str__(self):
        return self.name


class Host(models.Model):
    """add Host table"""
    HOST_TYPE_CHOICES = (
        ('server', '服务器'),
        ('virtual machine', '虚拟机'),
        ('other', 'Other'),
    )
    OS_CHOICES = (
        ('centos', 'Centos'),
        ('ubuntu', 'Ubuntu'),
        ('macOS', 'MacOS'),
        ('windows', 'Windows'),
        ('other', 'Other'),
    )
    HOST_STATUS_CHOICES = (
        ('normal', '正常'),
        ('measure', '故障'),
        ('other', 'Other')
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    hostname = models.CharField(max_length=32, unique=True, verbose_name='主机名')
    manage_ipaddress = models.GenericIPAddressField(unique=True, verbose_name='管理IP')
    other_ipaddress = models.GenericIPAddressField(blank=True, null=True, unique=True, verbose_name='其他IP')
    macaddress = models.CharField(max_length=32, null=True, blank=True, verbose_name='MAC地址')
    sn = models.CharField(max_length=64, blank=True, null=True, verbose_name='SN号')

    idc = models.ForeignKey(IDC, null=True, blank=True, verbose_name='所在机房')
    manufactory = models.CharField(max_length=64, blank=True, null=True, verbose_name='厂商')
    host_model = models.CharField(max_length=32, blank=True, null=True, verbose_name='主机型号')
    manage_user = models.ForeignKey(User, blank=True, null=True, verbose_name='管理人')
    hostgroup = models.ManyToManyField(HostGroup, default='', verbose_name='主机组')
    host_type = models.CharField(max_length=32, choices=HOST_TYPE_CHOICES, default='server', verbose_name='主机类型')

    os_type = models.CharField(max_length=32, choices=OS_CHOICES, default='centos', verbose_name='操作系统类型')
    os_version = models.CharField(max_length=64, blank=True, null=True, verbose_name='操作系统版本')
    cpu_model = models.CharField(max_length=32, blank=True, null=True, verbose_name='CPU型号')
    cpu_num = models.SmallIntegerField(default=0, blank=True, null=True, verbose_name='物理CPU个数')
    cpu_cores= models.SmallIntegerField(default=0, blank=True, null=True, verbose_name='逻辑CPU个数')
    memory = models.CharField(max_length=32, blank=True, null=True, verbose_name='内存')
    disk = models.CharField(max_length=256, blank=True, null=True, verbose_name='硬盘')

    status = models.CharField(max_length=32, choices=HOST_STATUS_CHOICES, default='normal',
                              verbose_name='主机状态')
    description = models.TextField(max_length=256, null=True, blank=True, verbose_name='描述')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    class Meta:
        unique_together = ['hostname', 'macaddress', 'sn']
        verbose_name = '主机'
        verbose_name_plural = verbose_name
        permissions = (
            ('get_host', ('查看主机')),
            ('add_host', ('添加主机')),
            ('edit_host', ('编辑主机')),
            ('del_host', ('删除主机')),
        )
        default_permissions = ()

    def __str__(self):
        return '{} sn:{}'.format(self.hostname, self.sn)


class NetworkDevice(models.Model):
    """add NetworkDevice"""
    NETWORK_DEVICE_TYPE_CHOICES = (
        ('route', '路由器'),
        ('switch', '交换机'),
        ('firewall', '防火墙'),
        ('other', 'Other'),
    )
    NETWORK_DEVICE_STATUS_CHOICES = (
        ('normal', '正常'),
        ('measure', '故障'),
        ('other', 'Other')
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    device_name = models.CharField(max_length=64, unique=True, verbose_name='设备名称')
    manage_ipaddress = models.GenericIPAddressField(verbose_name='管理IP')
    other_ipaddress = models.GenericIPAddressField(blank=True, null=True,verbose_name='其他IP')
    device_type = models.CharField(max_length=32, choices=NETWORK_DEVICE_TYPE_CHOICES, default='route',
                                   verbose_name='设备类型')
    macaddress = models.CharField(max_length=32, blank=True, null=True, verbose_name='MAC地址')
    sn = models.CharField(max_length=64, blank=True, null=True, verbose_name='SN号')
    port_num = models.SmallIntegerField(blank=True, null=True, verbose_name='接口个数')
    manufactory = models.CharField(max_length=64, blank=True, null=True, verbose_name='厂商')
    manage_user = models.ForeignKey(User, blank=True, null=True, verbose_name='管理人')
    idc = models.ForeignKey(IDC, null=True, blank=True, verbose_name='所在机房')
    device_detail = models.TextField(blank=True, null=True, verbose_name='设备配置详情')
    status = models.CharField(max_length=32, choices=NETWORK_DEVICE_STATUS_CHOICES, default='normal', verbose_name='设备状态')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    class Meta:
        unique_together = ['device_name', 'macaddress', 'sn']
        verbose_name = '网络设备'
        verbose_name_plural = verbose_name
        permissions = (
            ('get_network_device', ('查看网络设备')),
            ('add_network_device', ('添加网络设备')),
            ('edit_network_device', ('编辑网络设备')),
            ('del_network_device', ('删除网络设备')),
        )
        default_permissions = ()

    def __str__(self):
        return self.device_name





