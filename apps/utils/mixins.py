# -*- coding:utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.shortcuts import redirect,HttpResponseRedirect
from django.urls import reverse

from assets.models import IDC, Asset, AssetGroup
from accounts.models import User


class BaseMixin(LoginRequiredMixin):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin, self).get_context_data(*args, **kwargs)
        context['asset_count'] = Asset.objects.all().count()
        context['assetgroup_count'] = AssetGroup.objects.all().count()
        context['idc_count'] = IDC.objects.all().count()

        context['user_count'] = User.objects.all().count()
        context['usergroup_count'] = AssetGroup.objects.all().count()

        context['permission_count'] = Permission.objects.all().count()
        return context


class ActionPermissionRequiredMixin(PermissionRequiredMixin):
    """
    CBV mixin which verifies that the current user has all specified
    permissions.
    """
    def dispatch(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get(self.pk_url_kwarg)
            if not self.has_permission() and not request.user.is_staff and not request.user.is_superuser \
                    and str(request.user.id) != pk:
                return HttpResponseRedirect(reverse('permission:no_action_permission'))
        except:
            if not self.has_permission() and not request.user.is_staff and not request.user.is_superuser:
                return HttpResponseRedirect(reverse('permission:no_action_permission'))
        return super(PermissionRequiredMixin, self).dispatch(request, *args, **kwargs)
