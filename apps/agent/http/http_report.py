# -*- coding:utf-8 -*-

import os
import sys
import time
import threading
import requests
import json
import logging
import schedule
import configparser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from funcs import system, memory, cpu, disk

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(message)s')
logging.FileHandler(os.path.join(BASE_DIR)+'/log/agent.log')


config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR)+'/conf/agent.conf')

ip = config.get('agent', 'ip').encode('utf-8')
port = config.get('agent', 'port').encode('utf-8')
report_api = config.get('agent', 'report_api').encode('utf-8')
interval = int(config.get('agent', 'interval').encode('utf-8'))

print(ip, port, report_api, interval)

def get_agent_data():
    agent_data_info = system.get_system_info()
    agent_data_info['memory'] = memory.get_memory_info()
    agent_data_info['cpu'] = cpu.get_cpu_info()
    agent_data_info['disk'] = disk.get_disk_info()
    return agent_data_info

def get_server_url():
    server_url = 'http://' + ip + ':' + port + '/' + report_api
    return server_url


def report_agent_data():
    server_url = get_server_url()
    data = json.dumps(get_agent_data())
    print(data)
    headers = {'content-type': 'application/json'}
    response = requests.post(server_url, data=data, headers=headers)
    print(response.text, response.status_code)
    logger.info(response.text, response.status_code)


def run(job_func):
    job_sched = threading.Thread(target=job_func)
    job_sched.start()


if __name__ == '__main__':

    schedule.every(interval).seconds.do(run, report_agent_data)
    while True:
        schedule.run_pending()
        time.sleep(1)