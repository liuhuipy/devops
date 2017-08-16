__author__ = 'liuhui'


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.db.models import Q

from django.conf import settings
from assets.models import IDC
from assets.forms import IDCForm


class IDCListView(LoginRequiredMixin, ListView):
    model = IDC
    template_name = 'asset/idc_list.html'
    context_object_name = 'idc_list'
    paginate_by = settings.PAGE_NUM

    def get_queryset(self):
        idc_list = IDC.objects.all()
        idc_filter = self.request.GET.get('q')
        if idc_filter:
            idc_list = idc_list.filter(Q(name__contains=idc_filter)|
                                       Q(address__contains=idc_filter)
                                       )
        return idc_list

    def get_context_data(self, **kwargs):
        return super(IDCListView, self).get_context_data(**kwargs)

@login_required
def IDCAdd(request):
    if request.method == 'POST':
        idcform = IDCForm(request.POST)
        if idcform.is_valid():
            idc = idcform.save()
            if idc is not None:
                return HttpResponseRedirect(reverse('idc_list'))
        else:
            return render(request, 'asset/idc_add.html', locals())
    else:
        idcform = IDCForm()
    return render(request, 'asset/idc_add.html', locals())