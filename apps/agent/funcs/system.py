# -*- coding:utf-8 -*-

import uuid
import socket
import platform
from subprocess import Popen, PIPE


def get_hostname():
    hostname = socket.getfqdn(socket.gethostname())
    return hostname

def get_ipaddress():
    hostname = get_hostname()
    ipaddress = socket.gethostbyname(hostname)
    return ipaddress

def get_macaddress():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
    macaddress = ":".join(mac[i:i + 2] for i in range(0, len(mac), 2))
    return macaddress

def get_os_type():
    if platform.system() == 'Linux':
        return platform.linux_distribution()[0].split()[0]

def get_os_release():
    return platform.release()

def get_os_version():
    vers = platform.linux_distribution()
    os_version = vers[0] + vers[1] + vers[2]
    return os_version

def get_system_data():
    bash = 'dmidecode'
    p = Popen(bash, stdout=PIPE, shell=True)
    data = p.communicate()[0].split('\n')
    system_data, line_in = {}, False
    for line in data:
        if line.startswith('System Information'):
            line_in = True
            continue
        if line.startswith('\t') and line_in:
            k, v = [i.strip() for i in line.split(':')]
            system_data[k] = v
        else:
            line_in = False
    return system_data

def get_manufacturer(system_data):
    return system_data['Manufacturer']

def get_version(system_data):
    return system_data['Version']

def get_sn(system_data):
    return system_data['Serial Number']

def get_system_info():
    system_info = {}

    system_info['hostname'] = get_hostname()
    system_info['ipaddress'] = get_ipaddress()
    system_info['macaddress'] = get_macaddress()
    system_info['os_type'] = get_os_type()
    system_info['os_release'] = get_os_release()
    system_info['os_version'] = get_os_version()
    system_info['manufacturer'] = get_manufacturer(get_system_data())
    system_info['sn'] = get_sn(get_system_data())

    return system_info


# if __name__ == '__main__':
#     system_info = get_system_info()
#     for k, val in system_info.items():
#         print(k, val)