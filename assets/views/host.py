__author__ = 'liuhui'


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.db.models import Q

from django.conf import settings
from assets.models import Host
from assets.forms import HostForm


class HostListView(LoginRequiredMixin, ListView):
    model = Host
    template_name = 'asset/host_list.html'
    context_object_name = 'host_list'
    paginate_by = settings.PAGE_NUM

    def get_queryset(self):
        host_list = Host.objects.all()
        host_filter = self.request.GET.get('q')
        if host_filter:
            host_list = host_list.filter(Q(hostname__contains=host_filter)|
                                         Q(ipaddress__contains=host_filter)|
                                         Q(macaddress__contains=host_filter)|
                                         Q(idc__name__contains=host_filter)|
                                         Q(hostgroup__name__contains=host_filter)|
                                         Q(sn__contains=host_filter))
        return host_list

    def get_context_data(self, **kwargs):
        return super(HostListView, self).get_context_data(**kwargs)

@login_required
def HostAdd(request):
    if request.method == 'POST':
        hostform = HostForm(request.POST)
        if hostform.is_valid():
            host = hostform.save()
            if host is not None:
                return HttpResponseRedirect(reverse('host_list'))
        else:
            return render(request, 'asset/host_add.html', locals())
    else:
        hostform = HostForm()
    return render(request, 'asset/host_add.html', locals())



@login_required
def HostDel(request):
    asset_id = request.GET.get('id', '')
    if asset_id:
        Host.objects.filter(id=asset_id).delete()

    if request.method == 'POST':
        asset_batch = request.GET.get('arg', '')
        asset_id_all = str(request.POST.get('asset_id_all', ''))

        if asset_batch:
            for asset_id in asset_id_all.split(','):
                Host.objects.filter(id=asset_id).delete()
    return HttpResponse(u'删除成功')


