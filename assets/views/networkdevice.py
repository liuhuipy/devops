__author__ = 'liuhui'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.db.models import Q

from django.conf import settings
from assets.models import NetworkDevice
from assets.forms import NetworkDeviceForm


class NetworkDeviceListView(LoginRequiredMixin, ListView):
    model = NetworkDevice
    template_name = 'asset/networkdevice_list.html'
    context_object_name = 'networkdevice_list'
    paginate_by = settings.PAGE_NUM

    def get_queryset(self):
        networkdevice_list = NetworkDevice.objects.all()
        networkdevice_filter = self.request.GET.get('q')
        if networkdevice_filter:
            networkdevice_list = networkdevice_list.filter(Q(name__contains=networkdevice_filter)|
                                                           Q(type__contains=networkdevice_filter)|
                                                           Q(model__contains=networkdevice_filter)
                                                          )
        return networkdevice_list

    def get_context_data(self, **kwargs):
        return super(NetworkDeviceListView, self).get_context_data(**kwargs)

@login_required
def NetworkDeviceAdd(request):
    if request.method == 'POST':
        networkdeviceform = NetworkDeviceForm(request.POST)
        if networkdeviceform.is_valid():
            networkdevice = networkdeviceform.save()
            if networkdevice is not None:
                return HttpResponseRedirect(reverse('networkdevice_list'))
        else:
            return render(request, 'asset/networkdevice_add.html', locals())
    else:
        networkdeviceform = NetworkDeviceForm()
    return render(request, 'asset/networkdevice_add.html', locals())