from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from .forms import AnsibleScriptForm
from assets.models import Asset, AssetGroup


class AnsibleScript(FormView):
    template_name = 'ops/script.html'
    form_class = AnsibleScriptForm
    success_url = ''

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        assets = form['assets']
        asset_groups = form['asset_groups']
        shell = form['shell']
        script = form['script']
        hosts, hostgroups = [], {}
        if not assets and not asset_groups:
            return render(request, 'ops/script.html')
        for asset in assets:
            hosts.append(asset.manage_ipaddress)
        for assetgroup in asset_groups:
            hostgroups[assetgroup.name] = []
            asset_list = Asset.objects.get(asset_groups__id=assetgroup.id)
            for asset in asset_list:
                hostgroups[assetgroup.name].append(asset.manage_ipaddress)






