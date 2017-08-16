from django.db import models
from django.conf import settings
from django.utils import timezone
from accounts.models import UserProfile


# Create your models here.


ASSET_STATUS = {
    (1, u'在线'),
    (2, u'已下线'),
    (3, u'故障'),
    (4, u'备用'),
}

NETWORK_TYPE = (
    (1, u'路由器'),
    (2, u'交换机'),
    (3, u'负载均衡'),
    (4, u'VPN设备'),
)

IDC_OPERATOR = (
    (1, u'电信'),
    (2, u'联通'),
    (3, u'移动'),
    (4, u'铁通'),
)


class IDC(models.Model):
    '''
    add IDC table
    '''
    name = models.CharField(max_length=64, verbose_name=u'机房名称')
    address = models.CharField(max_length=128, verbose_name=u'机房地址')
    phone = models.CharField(max_length=32, verbose_name=u'联系电话')
    linkman = models.ForeignKey(UserProfile, verbose_name=u'联系人')
    email = models.EmailField(blank=True, null=True, verbose_name=u'邮箱')
    network = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'IP地址范围')
    operator = models.SmallIntegerField(choices=IDC_OPERATOR, verbose_name=u'运营商')
    remark = models.TextField(max_length=200, blank=True, null=True, verbose_name=u'备注')
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now=True)

    class Meta:
        verbose_name = u'IDC机房'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class HostGroup(models.Model):
    '''
    add HostGroup table
    '''
    name = models.CharField(max_length=32, unique=True, verbose_name=u'组名')
    remark = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'备注')

    class Meta:
        verbose_name = u'主机组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Host(models.Model):
    '''
    add Host table
    '''
    hostname = models.CharField(max_length=100, verbose_name=u'主机名', unique=True)
    hostgroup = models.ForeignKey(HostGroup, null=True, blank=True, verbose_name=u'主机组')
    idc = models.ForeignKey(IDC, null=True, blank=True, verbose_name=u'所属机房')
    ipaddress = models.GenericIPAddressField(verbose_name=u'IP地址')
    macaddress = models.CharField(max_length=50, null=True, blank=True, verbose_name=u'Mac地址')
    os_type = models.CharField(max_length=100, verbose_name=u'操作系统')
    os_version = models.CharField(max_length=100, verbose_name=u'系统版本')
    Manufactory = models.CharField(max_length=50, null=True, blank=True, verbose_name=u'设备厂商')
    sn = models.CharField(max_length=64, verbose_name=u'SN号', unique=True)
    cpu_model = models.CharField(max_length=100, verbose_name=u'CPU型号')
    cpu_num = models.SmallIntegerField(default=0, verbose_name=u'物理CPU数量')
    cpu_physical = models.SmallIntegerField(default=0, verbose_name=u'逻辑CPU数量')
    memory = models.CharField(max_length=32, verbose_name=u'内存大小')
    disk = models.CharField(max_length=255, verbose_name=u'硬盘大小')
    status = models.SmallIntegerField(default=1, null=True, blank=True, choices=ASSET_STATUS, verbose_name=u'资产状态')
    remark = models.TextField(max_length=200, blank=True, null=True, verbose_name=u'备注')

    class Meta:
        verbose_name = '主机'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} sn:{}'.format(self.hostname, self.sn)


class NetworkDevice(models.Model):
    '''
    add NetworkDevice
    '''
    name = models.CharField(max_length=64, unique=True)
    sn = models.CharField(max_length=64, blank=True, verbose_name=u'SN号', unique=True)
    type = models.SmallIntegerField(choices=NETWORK_TYPE, default=1, verbose_name=u'网络设备类型')
    user = models.ForeignKey(UserProfile, verbose_name=u'设备管理员')
    Manufactory = models.CharField(max_length=50, null=True, blank=True, verbose_name=u'设备厂商')
    idc = models.ForeignKey(IDC, blank=True, verbose_name=u'所属机房')
    vlan_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name=u'VlanIP')
    intranet_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name=u'内网IP')
    model = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'型号')
    port_num = models.SmallIntegerField(blank=True, null=True, verbose_name=u'端口个数')
    status = models.SmallIntegerField(default=1, blank=True, choices=ASSET_STATUS, verbose_name=u'资产状态')
    device_detail = models.TextField(blank=True, null=True, verbose_name=u'详细配置')

    class Meta:
        verbose_name = '网络设备'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name





