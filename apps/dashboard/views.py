# -*- coding:utf-8 -*-

from django.views.generic import TemplateView

from accounts.models import User
from assets.models import Asset
from utils.mixins import BaseMixin


class IndexView(BaseMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        kwargs['asset_normal_count'] = Asset.objects.filter(status='normal').count()
        kwargs['asset_measure_count'] = Asset.objects.filter(status='measure').count()
        kwargs['asset_other_count'] = Asset.objects.filter(status='other').count()
        kwargs['user_is_staff_count'] = User.objects.filter(is_active=True).count()
        kwargs['user_is_not_staff_count'] = User.objects.filter(is_staff=False).count()
        return super(IndexView, self).get_context_data(**kwargs)
