# -*- coding:utf-8 -*-

import json

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from assets.models import Asset
from assets.forms import AssetForm
from utils.mixins import BaseMixin


class AssetListView(BaseMixin, ListView):
    model = Asset
    template_name = 'asset/asset_list.html'
    context_object_name = 'asset_list'

    def get_queryset(self):
        asset_list = Asset.objects.order_by('-create_time')
        return asset_list

    def get_context_data(self, **kwargs):
        return super(AssetListView, self).get_context_data(**kwargs)


class AssetAddView(BaseMixin, PermissionRequiredMixin, CreateView):
    template_name = 'asset/asset_add.html'
    form_class = AssetForm
    permission_required = 'assets.add_asset'
    success_url = reverse_lazy('asset_list')
    success_message = '资产添加成功！'


class AssetDetailView(BaseMixin, DetailView):
    model = Asset
    template_name = 'asset/asset_detail.html'
    permission_required = 'assets.view_asset'
    context_object_name = 'asset'
    pk_url_kwarg = 'asset_id'


class AssetUpdateView(BaseMixin, PermissionRequiredMixin, UpdateView):
    model = Asset
    template_name = 'asset/asset_edit.html'
    form_class = AssetForm
    pk_url_kwarg = 'asset_id'
    permission_required = 'assets.change_asset'
    success_url = reverse_lazy('asset_list')
    success_message = '修改资产信息成功！'


class AssetDelView(BaseMixin, PermissionRequiredMixin, DeleteView):
    model = Asset
    pk_url_kwarg = 'asset_id'
    permission_required = 'assets.delete_asset'
    success_url = reverse_lazy('asset_list')


class AssetReport(APIView):
    permission_classes = []
    def dispatch(self, request, *args, **kwargs):
        return super(AssetReport, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data
        asset_data = {}
        asset_data['asset_name'] = data['hostname']
        asset_data['manage_ipaddress'] = data['ipaddress']
        asset_data['macaddress'] = data['macaddress']
        asset_data['sn'] = data['sn']
        asset_data['manufacturer'] = data['manufacturer']
        asset_data['os_type'] = data['os_type']
        asset_data['os_version'] = data['os_version']
        print(asset_data)
        if 'disk' in data:
            asset_data['disk_used'] = int(data['disk']['disk_used'])
            asset_data['disk_size'] = int(data['disk']['disk_size'])
            asset_data['disk_free'] = int(data['disk']['disk_free'])
        if 'memory' in data:
            asset_data['mem_total'] = int(data['memory']['mem_total'])
            asset_data['mem_free'] = int(data['memory']['mem_free'])
            asset_data['mem_buffers'] = int(data['memory']['mem_buffers'])
            asset_data['mem_cached'] = int(data['memory']['mem_cached'])
            asset_data['mem_available'] = int(data['memory']['mem_available'])
            asset_data['swap_mem_total'] = int(data['memory']['swap_mem_total'])
            asset_data['swap_mem_used'] = int(data['memory']['swap_mem_used'])
            asset_data['swap_mem_free'] = int(data['memory']['swap_mem_free'])
        try:
            asset = Asset.objects.create(
                asset_name=asset_data['asset_name'],
                manage_ipaddress=asset_data['manage_ipaddress'],
                macaddress=asset_data['macaddress'],
                sn=asset_data['sn'],
                manufacturer=asset_data['manufacturer'],
                os_type=asset_data['os_type'],
                os_version=asset_data['os_version'],
                disk_used=asset_data['disk_used'],
                disk_size=asset_data['disk_size'],
                disk_free=asset_data['disk_free'],
                mem_total=asset_data['mem_total'],
                mem_free=asset_data['mem_free'],
                # mem_used=asset_data['mem_used'] or 0,
                mem_buffers=asset_data['mem_buffers'],
                mem_cached=asset_data['mem_cached'],
                mem_available=asset_data['mem_available'],
                swap_mem_total=asset_data['swap_mem_total'],
                swap_mem_used=asset_data['swap_mem_used'],
                swap_mem_free=asset_data['swap_mem_free'],
            )
            return Response('xxxxxxxxxxxxxxxxxx')
        except:
            return Response('yyyyyyyyyyyyyyyyyy')

