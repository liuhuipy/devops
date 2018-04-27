# -*- coding:utf-8 -*-

import json

from celery import shared_task

from assets.models import Asset, AssetGroup
from accounts.models import User
from ops.models import AnsibleScript, AnsibleExecShellLog
from ops.ansible.runner import AdHocRunner, CommandResultCallback


def get_hosts(assets_list, asset_groups_list):
    temps, assets, asset_groups, hosts = set(), [], [], []
    # print(assets_list, asset_groups_list)
    for asset in assets_list:
        # print(asset)
        asset = Asset.objects.get(id=asset)
        assets.append(asset)
        temps.add(asset)
    for group in asset_groups_list:
        asset_groups.append(AssetGroup.objects.get(id=group))
        asset = Asset.objects.get(asset_group__id=group)
        temps.add(asset)

    for asset in temps:
        asset_info = {
            "hostname": asset.asset_name,
            "ip": asset.manage_ipaddress,
            "port": asset.port,
            "username": "root",
        }
        hosts.append(asset_info)
    return hosts, assets, asset_groups


@shared_task
def exec_shell(request):
    assets_list = request.POST.getlist('assets')
    asset_groups_list = request.POST.getlist('asset_groups')
    shell = request.POST.get('shell')
    print(assets_list, asset_groups_list, shell)
    user = User.objects.get(username=request.user)
    hosts, assets, asset_groups = get_hosts(assets_list, asset_groups_list)

    task_tuple = (('shell', shell),)
    hoc = AdHocRunner(hosts=hosts)
    hoc.results_callback = CommandResultCallback()
    ret = hoc.run(task_tuple)
    bash_exec = AnsibleExecShellLog.objects.create(
        user=user,
        shell=shell,
        assets=assets,
        asset_groups=asset_groups,
        system_user='root',
        result=json.dumps(ret),
    )
    return ret


@shared_task
def exec_script(request):
    assets_list = request.POST.getlist('assets')
    asset_groups_list = request.POST.getlist('asset_groups')
    script = request.POST.get('script')
    hosts, assets, asset_groups = get_hosts(assets_list, asset_groups_list)
    runner = AdHocRunner(hosts, forks=5)
    ret = runner.run(task_tuple=[('script', script)])
    print(ret)


