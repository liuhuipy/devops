# -*- coding:utf-8 -*-

from subprocess import Popen, PIPE


def get_data_info():
    bash = 'df'
    p = Popen(bash, stdout=PIPE, shell=True)
    data_info = p.communicate()[0].split('\n')[1:-1]
    return data_info

def get_disk_size(data_info):
    disk_size = 0
    for line in data_info:
        disk_size += int(line.split()[1])
    return disk_size

def get_disk_used(data_info):
    disk_used = 0
    for line in data_info:
        disk_used += int(line.split()[2])
    return disk_used

def get_disk_free(data_info):
    disk_free = 0
    for line in data_info:
        disk_free += int(line.split()[3])
    return disk_free

def get_disk_info():
    disk_info = {}
    data_info = get_data_info()

    disk_info['disk_size'] = get_disk_size(data_info)
    disk_info['disk_used'] = get_disk_used(data_info)
    disk_info['disk_free'] = get_disk_free(data_info)

    return disk_info


# if __name__ == '__main__':
#     disk_info = get_disk_info()
#     for k, val in disk_info.items():
#         print(k, val)