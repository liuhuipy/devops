__author__ = 'liuhui'

import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Params = {
    "server_ip": "192.168.61.1",
    "port": 8000,
    "request_timeout": 15,
    "url": {
        "asset_report_with_no_id": "asset/report/asset_with_no_asset_id",
        "asset_report": "asset/report/",
    },
    "asset_id": "%s/var/.asset_id" % BaseDir,
    "log_file": "%s/log/run_log" % BaseDir,
    "auth": {
        'user': 'liuhui_py@163.com',
        'token': 'aixocm',
    },
}