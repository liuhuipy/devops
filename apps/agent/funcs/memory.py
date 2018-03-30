# -*- coding:utf-8 -*-
# get server memory information

from subprocess import Popen, PIPE


def get_data_info():
    bash = "cat /proc/meminfo"
    p = Popen(bash, stdout=PIPE, shell=True)
    data_info = p.communicate()[0].split('\n')
    return data_info

def get_mem_total(data_info):
    for line in data_info:
        if line.startswith('MemTotal'):
            return int(line.split(':')[1].lstrip().rstrip('kB'))
    return None

def get_mem_free(data_info):
    for line in data_info:
        if line.startswith('MemFree'):
            return int(line.split(':')[1].lstrip().rstrip('kB'))
    return 0

def get_mem_buffers(data_info):
    for line in data_info:
        if line.startswith('Buffers'):
            return int(line.split(':')[1].lstrip().rstrip('kB'))
    return 0

def get_mem_cached(data_info):
    for line in data_info:
        if line.startswith('Cached'):
            return int(line.split(':')[1].lstrip().rstrip('kB'))
    return 0

def get_mem_available(data_info):
    for line in data_info:
        if line.startswith('MemAvailable'):
            return int(line.split(':')[1].lstrip().rstrip('kB'))
    return 0

def get_swap_mem_total(data_info):
    for line in data_info:
        if line.startswith('SwapTotal'):
            return int(line.split(':')[1].lstrip().rstrip('kB'))
    return 0

def get_swap_mem_free(data_info):
    for line in data_info:
        if line.startswith('SwapFree'):
            return int(line.split(':')[1].lstrip().rstrip('kB'))
    return 0

def get_memory_info():
    memory_info = {}
    data_info = get_data_info()

    memory_info['mem_total'] = get_mem_total(data_info)
    memory_info['mem_free'] = get_mem_free(data_info)
    memory_info['mem_buffers'] = get_mem_buffers(data_info)
    memory_info['mem_cached'] = get_mem_cached(data_info)
    memory_info['mem_available'] = get_mem_available(data_info)
    memory_info['mem_used'] = memory_info['mem_total'] - memory_info['mem_free'] - memory_info['mem_buffers'] \
                              - memory_info['mem_cached']

    memory_info['swap_mem_total'] = get_swap_mem_total(data_info)
    memory_info['swap_mem_free'] = get_swap_mem_free(data_info)
    memory_info['swap_mem_used'] = memory_info['swap_mem_total'] - memory_info['swap_mem_free']

    return memory_info


# if __name__ == '__main__':
#     memory_info = get_memory_info()
#     for k, val in memory_info.items():
#         print(k, val)