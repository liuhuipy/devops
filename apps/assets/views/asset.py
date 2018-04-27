# -*- coding:utf-8 -*-

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from assets.models import Asset
from assets.forms import AssetForm
from utils.mixins import BaseMixin, ActionPermissionRequiredMixin
from assets.tasks import create_or_update_asset_info


class AssetListView(BaseMixin, ActionPermissionRequiredMixin, ListView):
    model = Asset
    template_name = 'asset/asset_list.html'
    context_object_name = 'asset_list'
    permission_required = 'assets.viewlist_asset'
    paginate_by = 10

    def get_queryset(self):
        asset_list = Asset.objects.order_by('-create_time')
        return asset_list

    def get_context_data(self, **kwargs):
        kwargs['paginate_by'] = self.paginate_by
        return super(AssetListView, self).get_context_data(**kwargs)


class AssetAddView(BaseMixin, ActionPermissionRequiredMixin, CreateView):
    template_name = 'asset/asset_add.html'
    form_class = AssetForm
    permission_required = ('assets.add_asset')
    success_url = reverse_lazy('assets:asset_list')
    success_message = '资产添加成功！'


class AssetDetailView(BaseMixin, ActionPermissionRequiredMixin,DetailView):
    model = Asset
    template_name = 'asset/asset_detail.html'
    permission_required = 'assets.view_asset'
    context_object_name = 'asset'
    pk_url_kwarg = 'asset_id'


class AssetUpdateView(BaseMixin, ActionPermissionRequiredMixin, UpdateView):
    model = Asset
    template_name = 'asset/asset_edit.html'
    form_class = AssetForm
    pk_url_kwarg = 'asset_id'
    permission_required = 'assets.change_asset'
    success_url = reverse_lazy('assets:asset_list')
    success_message = '修改资产信息成功！'


class AssetDelView(BaseMixin, ActionPermissionRequiredMixin, DeleteView):
    model = Asset
    pk_url_kwarg = 'asset_id'
    permission_required = 'assets.delete_asset'
    success_url = reverse_lazy('assets:asset_list')


class SearchAssetView(AssetListView):

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q:
            asset_list = Asset.objects.filter(Q(asset_name__contains=q)
                                              | Q(manage_ipaddress__contains=q)
                                              | Q(macaddress__contains=q)
                                              | Q(os_type__contains=q)).order_by('-create_time')
        else:
            asset_list = Asset.objects.order_by('-create_time')
        return asset_list


class AssetReport(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        if create_or_update_asset_info(data):
            return Response('success!!')
        else:
            return Response('failed!!')

