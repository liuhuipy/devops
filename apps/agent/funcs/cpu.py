# -*- coding:utf-8 -*-

from subprocess import Popen, PIPE


def get_data_info():
    bash = "cat /proc/cpuinfo"
    p = Popen(bash, stdout=PIPE, shell=True)
    data_info = p.communicate()[0].split('\n')
    return data_info

def get_logical_cpu_num(data_info): # 逻辑cpu个数
    logical_num = 0
    for line in data_info:
        if line.startswith('processor'):
            logical_num += 1
    return logical_num

def get_physical_cpu_num(data_info): # 物理cpu个数
    physical_max_id = 0
    for line in data_info:
        if line.startswith('physical id') and int(line.split(':')[1].lstrip().rstrip()) > physical_max_id:
            physical_max_id = int(line.split(':')[1].lstrip().rstrip())
    return physical_max_id + 1

def get_vendor_id(data_info): # 厂商名
    vendor_id = ''
    for line in data_info:
        if line.startswith('vendor_id'):
            vendor_id = line.split(':')[1].lstrip().rstrip()
    return vendor_id

def get_model_name(data_info): # cpu的型号
    model_name = ''
    for line in data_info:
        if line.startswith('model name'):
            model_name = line.split(':')[1].lstrip().rstrip()
    return model_name

def get_cpu_cores(data_info): # 每个物理cpu的核数
    cpu_cores = 0
    for line in data_info:
        if line.startswith('cpu cores'):
            cpu_cores = int(line.split(':')[1].lstrip().rstrip())
    return cpu_cores

def get_cpu_info():
    cpu_info = {}
    data_info = get_data_info()
    cpu_info['logical_num'] = get_logical_cpu_num(data_info)
    cpu_info['physical_num'] = get_physical_cpu_num(data_info)
    cpu_info['vendor_id'] = get_vendor_id(data_info)
    cpu_info['model_name'] = get_model_name(data_info)
    cpu_info['cpu_cores'] = get_cpu_cores(data_info)

    return cpu_info


# if __name__ == '__main__':
#     cpu_info = get_cpu_info()
#     for k, val in cpu_info.items():
#         print(k, val)