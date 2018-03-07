# -*- coding:utf-8 -*-

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from assets.models import NetworkDevice
from assets.forms import NetworkDeviceForm
from utils.mixins import BaseMixin


class NetworkDeviceListView(BaseMixin, ListView):
    model = NetworkDevice
    template_name = 'asset/networkdevice_list.html'
    context_object_name = 'networkdevice_list'

    def get_queryset(self):
        networkdevice_list = NetworkDevice.objects.order_by('-create_time')
        return networkdevice_list

    def get_context_data(self, **kwargs):
        return super(NetworkDeviceListView, self).get_context_data(**kwargs)


class NetworkDeviceAddView(BaseMixin, CreateView):
    template_name = 'asset/networkdevice_add.html'
    form_class = NetworkDeviceForm
    success_url = reverse_lazy('networkdevice_list')
    success_message = '物理设备添加成功！'


class NetworkDeviceDetailView(BaseMixin, DetailView):
    model = NetworkDevice
    template_name = 'asset/networkdevice_detail.html'
    context_object_name = 'networkdevice'
    pk_url_kwarg = 'networkdevice_id'


class NetworkDeviceUpdateView(BaseMixin, UpdateView):
    model = NetworkDevice
    template_name = 'asset/networkdevice_edit.html'
    form_class = NetworkDeviceForm
    pk_url_kwarg = 'networkdevice_id'
    success_url = reverse_lazy('networkdevice_list')
    success_message = '修改主机信息成功！'


class NetworkDeviceDelView(BaseMixin, DeleteView):
    model = NetworkDevice
    pk_url_kwarg = 'networkdevice_id'
    success_url = reverse_lazy('networkdevice_list')
