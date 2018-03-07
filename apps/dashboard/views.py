# -*- coding:utf-8 -*-

from django.views.generic import TemplateView

from accounts.models import User
from assets.models import Host
from utils.mixins import BaseMixin


class IndexView(BaseMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        kwargs['host_normal_count'] = Host.objects.filter(status='normal').count()
        kwargs['host_measure_count'] = Host.objects.filter(status='measure').count()
        kwargs['host_scrap_count'] = Host.objects.filter(status='scrap').count()
        kwargs['host_other_count'] = Host.objects.filter(status='other').count()
        kwargs['user_is_active_count'] = User.objects.filter(is_staff=True).count()
        kwargs['user_is_not_active_count'] = User.objects.filter(is_staff=False).count()
        return super(IndexView, self).get_context_data(**kwargs)
