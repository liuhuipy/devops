# -*- coding:utf-8 -*-

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from assets.models import Host
from assets.forms import HostForm
from utils.mixins import BaseMixin


class HostListView(BaseMixin, ListView):
    model = Host
    template_name = 'asset/host_list.html'
    context_object_name = 'host_list'

    def get_queryset(self):
        host_list = Host.objects.order_by('-create_time')
        return host_list

    def get_context_data(self, **kwargs):
        return super(HostListView, self).get_context_data(**kwargs)


class HostAddView(BaseMixin, CreateView):
    template_name = 'asset/host_add.html'
    form_class = HostForm
    success_url = reverse_lazy('host_list')
    success_message = '主机添加成功！'


class HostDetailView(BaseMixin, DetailView):
    model = Host
    template_name = 'asset/host_detail.html'
    context_object_name = 'host'
    pk_url_kwarg = 'host_id'


class HostUpdateView(BaseMixin, UpdateView):
    model = Host
    template_name = 'asset/host_edit.html'
    form_class = HostForm
    pk_url_kwarg = 'host_id'
    success_url = reverse_lazy('host_list')
    success_message = '修改主机信息成功！'


class HostDelView(BaseMixin, DeleteView):
    model = Host
    pk_url_kwarg = 'host_id'
    success_url = reverse_lazy('host_list')




