# -*- coding:utf-8 -*_

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from utils.mixins import BaseMixin, ActionPermissionRequiredMixin
from assets.models import AssetGroup
from assets.forms import AssetGroupForm


class AssetGroupListView(BaseMixin, ActionPermissionRequiredMixin, ListView):
    model = AssetGroup
    template_name = 'asset/assetgroup_list.html'
    context_object_name = 'assetgroup_list'
    permission_required = 'assets.viewlist_assetgroup'
    paginate_by = 10

    def get_queryset(self):
        assetgroup_list = AssetGroup.objects.filter().order_by('-create_time')
        return assetgroup_list

    def get_context_data(self, **kwargs):
        kwargs['paginate_by'] = self.paginate_by
        return super(AssetGroupListView, self).get_context_data(**kwargs)


class AssetGroupAddView(BaseMixin, ActionPermissionRequiredMixin, CreateView):
    template_name = 'asset/assetgroup_add.html'
    form_class = AssetGroupForm
    permission_required = 'assets.add_assetgroup'
    success_url = reverse_lazy('assets:assetgroup_list')
    success_messages = '添加资产组成功！'


class AssetGroupDetailView(BaseMixin, ActionPermissionRequiredMixin, DetailView):
    model = AssetGroup
    template_name = 'asset/assetgroup_detail.html'
    context_object_name = 'assetgroup'
    permission_required = 'assets.view_assetgroup'
    pk_url_kwarg = 'assetgroup_id'


class AssetGroupUpdateView(BaseMixin, ActionPermissionRequiredMixin, UpdateView):
    model = AssetGroup
    template_name = 'asset/assetgroup_edit.html'
    form_class = AssetGroupForm
    pk_url_kwarg = 'assetgroup_id'
    permission_required = 'assets.change_assetgroup'
    success_url = reverse_lazy('assets:assetgroup_list')
    success_message = '修改资产组信息成功！'


class AssetGroupDelView(BaseMixin, ActionPermissionRequiredMixin, DeleteView):
    model = AssetGroup
    pk_url_kwarg = 'assetgroup_id'
    permission_required = 'assets.delete_assetgroup'
    success_url = reverse_lazy('assets:assetgroup_list')
