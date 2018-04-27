# -*- coding:utf-8 -*-

from celery import shared_task

from assets.models import Asset


@shared_task
def create_or_update_asset_info(data):
    asset_data = {}
    asset_data['asset_name'] = data['hostname']
    asset_data['manage_ipaddress'] = data['ipaddress']
    asset_data['macaddress'] = data['macaddress']
    asset_data['sn'] = data['sn']
    asset_data['manufacturer'] = data['manufacturer']
    asset_data['os_type'] = data['os_type']
    asset_data['os_version'] = data['os_version']
    print(asset_data)
    if 'disk' in data:
        asset_data['disk_used'] = int(data['disk']['disk_used'])
        asset_data['disk_size'] = int(data['disk']['disk_size'])
        asset_data['disk_free'] = int(data['disk']['disk_free'])
    if 'memory' in data:
        asset_data['mem_total'] = int(data['memory']['mem_total'])
        asset_data['mem_free'] = int(data['memory']['mem_free'])
        asset_data['mem_buffers'] = int(data['memory']['mem_buffers'])
        asset_data['mem_cached'] = int(data['memory']['mem_cached'])
        asset_data['mem_available'] = int(data['memory']['mem_available'])
        asset_data['swap_mem_total'] = int(data['memory']['swap_mem_total'])
        asset_data['swap_mem_used'] = int(data['memory']['swap_mem_used'])
        asset_data['swap_mem_free'] = int(data['memory']['swap_mem_free'])
    try:
        asset = Asset.objects.update_or_create(
            asset_name=asset_data['asset_name'],
            manage_ipaddress=asset_data['manage_ipaddress'],
            macaddress=asset_data['macaddress'],
            sn=asset_data['sn'],
            manufacturer=asset_data['manufacturer'],
            os_type=asset_data['os_type'],
            os_version=asset_data['os_version'],
            disk_used=asset_data['disk_used'],
            disk_size=asset_data['disk_size'],
            disk_free=asset_data['disk_free'],
            mem_total=asset_data['mem_total'],
            mem_free=asset_data['mem_free'],
            mem_buffers=asset_data['mem_buffers'],
            mem_cached=asset_data['mem_cached'],
            mem_available=asset_data['mem_available'],
            swap_mem_total=asset_data['swap_mem_total'],
            swap_mem_used=asset_data['swap_mem_used'],
            swap_mem_free=asset_data['swap_mem_free'],
        )
        return True
    except:
        return False