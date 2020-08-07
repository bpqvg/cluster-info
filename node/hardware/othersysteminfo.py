import json
import psutil
import datetime

class OtherSystemInfo:
    def __init__(self):
        pass
    def get_boot_time(self):
        boot_time = psutil.boot_time()
        boot_time_o = {
            "default": boot_time,
            "humanreadable": datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")
        }
        return json.dumps(boot_time_o)
    def get_users(self):
        users = psutil.users()
        users_o = []
        for user in users:
            user_o = {
                "name": user.name,
                "terminal": user.terminal,
                "host": user.host,
                "started": user.started,
                "pid": user.pid
            }
            users_o.append(user_o)
        return json.dumps(users_o)
