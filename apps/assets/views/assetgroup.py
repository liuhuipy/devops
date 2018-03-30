# -*- coding:utf-8 -*_

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from utils.mixins import BaseMixin
from assets.models import AssetGroup
from assets.forms import AssetGroupForm

class AssetGroupListView(BaseMixin, ListView):
    model = AssetGroup
    template_name = 'asset/assetgroup_list.html'
    context_object_name = 'assetgroup_list'

    def get_queryset(self):
        assetgroup_list = AssetGroup.objects.filter().order_by('-create_time')
        return assetgroup_list

    def get_context_data(self, **kwargs):
        return super(AssetGroupListView, self).get_context_data(**kwargs)


class AssetGroupAddView(BaseMixin, PermissionRequiredMixin, CreateView):
    template_name = 'asset/assetgroup_add.html'
    form_class = AssetGroupForm
    permission_required = 'assets.add_assetgroup'
    success_url = reverse_lazy('assetgroup_list')
    success_messages = '添加资产组成功！'


class AssetGroupDetailView(BaseMixin, PermissionRequiredMixin, DetailView):
    model = AssetGroup
    template_name = 'asset/assetgroup_detail.html'
    context_object_name = 'assetgroup'
    permission_required = 'assets.get_assetgroup'
    pk_url_kwarg = 'assetgroup_id'


class AssetGroupUpdateView(BaseMixin, PermissionRequiredMixin, UpdateView):
    model = AssetGroup
    template_name = 'asset/assetgroup_edit.html'
    form_class = AssetGroupForm
    pk_url_kwarg = 'assetgroup_id'
    permission_required = 'assets.change_assetgroup'
    success_url = reverse_lazy('assetgroup_list')
    success_message = '修改资产组信息成功！'


class AssetGroupDelView(BaseMixin, PermissionRequiredMixin, DeleteView):
    model = AssetGroup
    pk_url_kwarg = 'assetgroup_id'
    permission_required = 'assets.delete_assetgroup'
    success_url = reverse_lazy('assetgroup_list')
