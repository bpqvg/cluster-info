import json
import psutil

class Processes:
    def __init__(self):
        pass
    def get_pids(self):
        pids = psutil.pids()
        return json.dumps(pids)
    def get_process_iter(self):
        process_iter = psutil.process_iter(['name', 'username'])
        process_iter_o = []
        for p in process_iter:
            process_iter_o.append({p.pid: p.info})
        return json.dumps(process_iter_o)
    def get_pid_exists(self, pid):
        pid_exists = psutil.pid_exists(pid)
        pid_exists_o = {
            "pid: {}".format(pid): pid_exists
        }
        return json.dumps(pid_exists_o)
    # def get_wait_procs(self, procs, timeout=None, callback=None):
    #     wait_procs = psutil.wait_procs(procs, timeout, callback)
