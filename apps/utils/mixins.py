# -*- coding:utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin

from assets.models import Host, HostGroup, NetworkDevice, IDC
from accounts.models import User
from power.models import Power


class BaseMixin(LoginRequiredMixin):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin, self).get_context_data(*args, **kwargs)
        context['host_count'] = Host.objects.all().count()
        context['hostgroup_count'] = HostGroup.objects.all().count()
        context['networkdevice_count'] = NetworkDevice.objects.all().count()
        context['idc_count'] = IDC.objects.all().count()

        context['user_count'] = User.objects.all().count()
        context['usergroup_count'] = HostGroup.objects.all().count()

        context['power_count'] = Power.objects.all().count()
        context['asset_count'] = context['host_count'] + context['networkdevice_count']
        return context