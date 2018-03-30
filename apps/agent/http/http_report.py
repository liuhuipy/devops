# -*- coding:utf-8 -*-

import os
import sys
import requests
from requests import cookies
import json
import logging

# import configparser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from funcs import system, memory, cpu, disk

# config = configparser.ConfigParser()
# config.read('../conf/agent.conf')
#
# ip = config.get('server', 'ip')
# port = config.get('server', 'port')
# report_url = config.get('server', 'report_url')


def get_agent_data():
    agent_data_info = system.get_system_info()
    agent_data_info['memory'] = memory.get_memory_info()
    agent_data_info['cpu'] = cpu.get_cpu_info()
    agent_data_info['disk'] = disk.get_disk_info()
    return agent_data_info

def get_server_url():
    # server_url = 'http://' + ip + ':' + port + '/' + report_url
    server_url = 'http://1'
    return server_url



def report_agent_data(server_url, agent_data_info):
    # session = requests.Session()
    # resp = session.get('http://172.16.162.1:8000/api/assets/report/info/')
    # csrf_token = resp.cookies['csrftoken']
    # print(csrf_token)
    # agent_data_info['csrfmiddlewaretoken'] = csrf_token
    # headers = {
    #     "csrf_token": cookies,
    #     "Content-Type": "application/x-www-form-urlencoded",
    #     "User-Agent": "curl/7.47.0",
    #     "charset": "UTF-8",
    #     "Connection": "Keep-Alive"
    # }
    data = json.dumps(agent_data_info)
    print(data)
    # cookies = dict(cookies_are = 'working')
    # cookies = '{{ csrf_token }}'
    headers = {'content-type': 'application/json'}
    response = requests.post(server_url, data=data, headers=headers)
    if response.text:
        print(response.text)
    else:
        print(response.status_code)


if __name__ == '__main__':
    # get_server_url(ip, port, report_url)
    report_agent_data('http://172.16.162.1:8000/api/assets/report/', get_agent_data())
