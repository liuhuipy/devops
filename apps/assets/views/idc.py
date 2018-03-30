# -*- coding:utf-8 -*-

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from utils.mixins import BaseMixin
from assets.models import IDC
from assets.forms import IDCForm


class IDCListView(BaseMixin, ListView):
    model = IDC
    template_name = 'asset/idc_list.html'
    context_object_name = 'idc_list'

    def get_queryset(self):
        idc_list = IDC.objects.order_by('-create_time')
        return idc_list

    def get_context_data(self, **kwargs):
        return super(IDCListView, self).get_context_data(**kwargs)


class IDCAddView(BaseMixin, PermissionRequiredMixin, CreateView):
    template_name = 'asset/idc_add.html'
    form_class = IDCForm
    permission_required = 'assets.add_idc'
    success_url = reverse_lazy('idc_list')
    success_messages = '添加IDC机房成功！'


class IDCDetailView(BaseMixin, PermissionRequiredMixin, DetailView):
    model = IDC
    template_name = 'asset/idc_detail.html'
    permission_required = 'assets.get_idc'
    context_object_name = 'idc'
    pk_url_kwarg = 'idc_id'


class IDCUpdateView(BaseMixin, PermissionRequiredMixin, UpdateView):
    model = IDC
    template_name = 'asset/idc_edit.html'
    form_class = IDCForm
    pk_url_kwarg = 'idc_id'
    permission_required = 'assets.change_idc'
    success_url = reverse_lazy('idc_list')
    success_message = '修改机房信息成功！'


class IDCDelView(BaseMixin, PermissionRequiredMixin, DeleteView):
    model = IDC
    pk_url_kwarg = 'idc_id'
    permission_required = 'assets.delete_idc'
    success_url = reverse_lazy('idc_list')