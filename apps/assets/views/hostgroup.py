# -*- coding:utf-8 -*_

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from utils.mixins import BaseMixin
from assets.models import HostGroup
from assets.forms import HostGroupForm

class HostGroupListView(BaseMixin, ListView):
    model = HostGroup
    template_name = 'asset/hostgroup_list.html'
    context_object_name = 'hostgroup_list'

    def get_queryset(self):
        hostgroup_list = HostGroup.objects.filter().order_by('-create_time')
        return hostgroup_list

    def get_context_data(self, **kwargs):
        return super(HostGroupListView, self).get_context_data(**kwargs)


class HostGroupAddView(BaseMixin, CreateView):
    template_name = 'asset/hostgroup_add.html'
    form_class = HostGroupForm
    success_url = reverse_lazy('hostgroup_list')
    success_messages = '添加主机组成功！'


class HostGroupDetailView(BaseMixin, DetailView):
    model = HostGroup
    template_name = 'asset/hostgroup_detail.html'
    context_object_name = 'hostgroup'
    pk_url_kwarg = 'hostgroup_id'


class HostGroupUpdateView(BaseMixin, UpdateView):
    model = HostGroup
    template_name = 'asset/hostgroup_edit.html'
    form_class = HostGroupForm
    pk_url_kwarg = 'hostgroup_id'
    success_url = reverse_lazy('hostgroup_list')
    success_message = '修改主机信息成功！'


class HostGroupDelView(BaseMixin, DeleteView):
    model = HostGroup
    pk_url_kwarg = 'hostgroup_id'
    success_url = reverse_lazy('hostgroup_list')
