__author__ = 'liuhui'

import sys
import os
import uuid
import re
import platform
import socket
import datetime
import json
import time
import threading
from subprocess import Popen, PIPE
BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(BASE_DIR)
#python3
#from devops_client.conf import settings
from conf import settings

server_ip = settings.Params['server_ip']
port = settings.Params['port']
timeout = settings.Params['request_timeout']


try:
    import psutil
except ImportError as msg:
    print(msg)
    print("---------------------------------------------")
    print("begining install psutil module, please waiting")
    p = Popen('pip install psutil==5.2.2', stdout=PIPE, shell=True)
    stdout, stderr = p.communicate()
    print(stdout)
    import psutil

try:
    import schedule
except ImportError as msg:
    print(msg)
    print("------------------------------------------------")
    print("begining install schedule module, please waiting")
    p = Popen('pip install schedule==0.4.3', stdout=PIPE, shell=True)
    stdout, stderr = p.communicate()
    print(stdout)
    import schedule

try:
    import requests
except ImportError as msg:
    print(msg)
    print("------------------------------------------------")
    print("begining install schedule module, please waiting")
    p = Popen('pip install requests==2.17.3', stdout=PIPE, shell=True)
    stdout, stderr = p.communicate()
    print(stdout)
    import requests


def get_dmi():
    p = Popen('dmidecode', stdout=PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout

def parser_dmi(dmi):
    pd = dict()
    line_in = False
    for line in dmi.split('\n'):
        if line.startswith('System Information'):
            line_in = True
            continue
        if line.startswith('\t') and line_in:
            k, v = [i.strip() for i in line.split(':')]
            pd[k] = v
        else:
            line_in = False
    return pd

def get_hostname():
    hostname = socket.getfqdn(socket.gethostname())
    return hostname

def get_ipaddress():
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('{}'.format(server_ip), 0))
    ipaddress = s.getsockname()[0]
    '''
    hostname = get_hostname()
    ipaddress = socket.gethostbyname(hostname)
    return ipaddress

def get_macaddress():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
    macaddress = "{}:{}:{}:{}:{}:{}".format(mac[0:2], mac[2:4], mac[4:6], mac[6:8], mac[8:10], mac[10:])
    return macaddress

def get_os_type():
    os_type = platform.system()
    return os_type

def get_os_version():
    os_version = platform.linux_distribution()[0] + platform.linux_distribution()[1] + platform.linux_distribution()[2]
    return os_version

def get_cpu_model():
    cmd = "cat /proc/cpuinfo"
    p = Popen(cmd, stdout=PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout

def parser_cpu(stdout):
    groups = [i for i in stdout.split('\n\n')]
    group = groups[-2]
    cpu_list = [i for i in group.split('\n')]
    cpu_info = {}
    for x in cpu_list:
        k, v = [i.strip() for i in x.split(':')]
        cpu_info[k] = v
    return cpu_info

def get_cpu_num():
    cpu_num = {'logical': psutil.cpu_count(logical=False), 'physical': psutil.cpu_count()}
    return cpu_num

def get_memory():
    cmd = "grep MemTotal /proc/meminfo"
    p = Popen(cmd, stdout=PIPE, shell=True)
    data = p.communicate()[0]
    mem_total = data.split()[1]
    memtotal = str(round(int(mem_total)/1024.0/1024.0, 0)) + 'GB'
    return memtotal

def humanize_bytes(bytesize, precision=0):
    abbrevs = (
        (10**15, 'PB'),
        (10**12, 'TB'),
        (10**9, 'GB'),
        (10**6, 'MB'),
        (10**3, 'kB'),
        (1, 'bytes')
    )
    if bytesize == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytesize >= factor:
            break
    return '%.*f%s' % (precision, round(float(bytesize) / factor), suffix)
def get_disk_info():
    with open('/proc/partitions','r') as dp:
        res = ''
        for disk in dp.readlines():
            if re.search(r'[s,h,v]d[a-z]\n',disk):
                blknum = disk.strip().split(' ')[-2]
                dev = disk.strip().split(' ')[-1]
                size = int(blknum)*1024
                consist = dev+'['+humanize_bytes(size).strip()+']'
                res += consist + '+'
    return res[:-1]


def get_asset_info():
    asset_info = dict()
    asset_info['hostname'] = get_hostname()
    asset_info['ipaddress'] = get_ipaddress()
    asset_info['macaddress'] = get_macaddress()
    asset_info['os_type'] = get_os_type()
    asset_info['os_version'] = get_os_version()
    asset_info['Manufactory'] = parser_dmi(get_dmi())['Manufacturer']
    asset_info['sn'] = parser_dmi(get_dmi())['Serial Number']
    asset_info['cpu_num'] = get_cpu_num()['logical']
    asset_info['cpu_physical'] = get_cpu_num()['physical']
    asset_info['cpu_model'] = parser_cpu(get_cpu_model())['model name']
    asset_info['memory'] = get_memory()
    asset_info['disk'] = get_disk_info()
    return asset_info

def post_data(url, data):
    try:
        r = requests.post(url, data)
        if r.text:
            return r.text
        else:
            print("Server return http status code: {}" % r.status_code)
    #python3
    #except  BaseExceptionas msg:
    except StandardError as msg:
        print(msg)
    return True


def get_asset_id():
    asset_id_file = settings.Params['asset_id']
    has_asset_id = False
    if os.path.isfile(asset_id_file):
        asset_id = open(asset_id_file).read().strip()
        if asset_id.isdigit():
            return asset_id
        else:
            has_asset_id = False
    else:
        has_asset_id = False

def update_asset_id(new_asset_id):
    asset_id_file = settings.Params['asset_id']
    f = open(asset_id_file, 'wb')
    f.write(new_asset_id)
    f.close()

def report_asset_info():
    asset_info = get_asset_info()
    asset_id = get_asset_id()
    if asset_id:
        asset_info['asset_id'] = asset_id
        post_url = settings.Params["url"]["asset_report"]
    else:
        asset_info['asset_id'] = None
        post_url = settings.Params["url"]["asset_report_with_no_id"]
    asset_info = {'asset_info': json.dumps(asset_info)}
    osenv = os.environ['LANG']
    os.environ['LANG'] = "us_EN.UTF8"
    print('Get the hardwave infos from host:')
    print(asset_info)
    print('---------------------------------------------------------')
    response = post_data("http://{}:{}/{}".format(server_ip, port, post_url), asset_info)
    os.environ['LANG'] = osenv
    if type(response) != bool:
        response = eval(response.encode())
        if "asset_id" in response:
            update_asset_id(str(response["asset_id"]))
    log_recode(response)
    return True

def log_recode(log,):
    f = open(settings.Params["log_file"], "ab")
    if log is str:
        pass
    if type(log) is dict:

        if "info" in log:
            for msg in log["info"]:
                log_format = "{}\tINFO\t{}\n".format((datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")),msg)
                # print msg
                f.write(log_format)
        if "error" in log:
            for msg in log["error"]:
                log_format = "{}\tERROR\t{}\n".format((datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")),msg)
                f.write(log_format)
        if "warning" in log:
            for msg in log["warning"]:
                log_format = "{}\tWARNING\t{}\n".format((datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")),msg)
                f.write(log_format)

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)

if __name__ == "__main__":

    report_asset_info()
    time.sleep(1)
    schedule.every(timeout).seconds.do(run_threaded, report_asset_info)
    while True:
        schedule.run_pending()
        time.sleep(1)

    '''
    asset_info = report_asset_info()
    for k,v in asset_info.items():
        print("{}:{}".format(k,v))
    '''

