__author__ = 'liuhui'


from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from django.conf import settings

from assets.models import HostGroup
from assets.forms import HostGroupForm

class HostGroupListView(LoginRequiredMixin, ListView):
    model = HostGroup
    template_name = 'asset/hostgroup_list.html'
    context_object_name = 'hostgroup_list'
    paginate_by = settings.PAGE_NUM

    def get_queryset(self):
        hostgroup_list = HostGroup.objects.all()
        hostgroup_filter = self.request.GET.get('q')
        if hostgroup_filter:
            hostgroup_list = hostgroup_list.filter(Q(name__contains=hostgroup_filter))
        return hostgroup_list

    def get_context_data(self, **kwargs):
        return super(HostGroupListView, self).get_context_data(**kwargs)

@login_required
def HostGroupAdd(request):
    if request.method == 'POST':
        hostgroupform = HostGroupForm(request.POST)
        if hostgroupform.is_valid():
            host = hostgroupform.save()
            if host is not None:
                return HttpResponseRedirect(reverse('hostgroup_list'))
        else:
            return render(request, 'asset/hostgroup_add.html', locals())
    else:
        hostgroupform = HostGroupForm()
    return render(request, 'asset/hostgroup_add.html', locals())