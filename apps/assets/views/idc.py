# -*- coding:utf-8 -*-

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from utils.mixins import BaseMixin, ActionPermissionRequiredMixin
from assets.models import IDC
from assets.forms import IDCForm


class IDCListView(BaseMixin, ActionPermissionRequiredMixin, ListView):
    model = IDC
    template_name = 'asset/idc_list.html'
    context_object_name = 'idc_list'
    permission_required = 'assets.viewlist_idc'
    paginate_by = 10

    def get_queryset(self):
        idc_list = IDC.objects.order_by('-create_time')
        return idc_list

    def get_context_data(self, **kwargs):
        kwargs['paginate_by'] = self.paginate_by
        return super(IDCListView, self).get_context_data(**kwargs)


class IDCAddView(BaseMixin, ActionPermissionRequiredMixin, CreateView):
    template_name = 'asset/idc_add.html'
    form_class = IDCForm
    permission_required = 'assets.add_idc'
    success_url = reverse_lazy('idc_list')
    success_messages = '添加IDC机房成功！'


class IDCDetailView(BaseMixin, ActionPermissionRequiredMixin, DetailView):
    model = IDC
    template_name = 'asset/idc_detail.html'
    permission_required = 'assets.view_idc'
    context_object_name = 'idc'
    pk_url_kwarg = 'idc_id'


class IDCUpdateView(BaseMixin, ActionPermissionRequiredMixin, UpdateView):
    model = IDC
    template_name = 'asset/idc_edit.html'
    form_class = IDCForm
    pk_url_kwarg = 'idc_id'
    permission_required = 'assets.change_idc'
    success_url = reverse_lazy('idc_list')
    success_message = '修改机房信息成功！'


class IDCDelView(BaseMixin, ActionPermissionRequiredMixin, DeleteView):
    model = IDC
    pk_url_kwarg = 'idc_id'
    permission_required = 'assets.delete_idc'
    success_url = reverse_lazy('idc_list')