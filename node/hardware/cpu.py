import cpuinfo
import json
import psutil

class Cpu:
    def __init__(self):
        pass
    def get_cpu_info(self):
        return cpuinfo.get_cpu_info_json()
    def get_cpu_percent(self):
        return psutil.cpu_percent(interval=1, percpu=True)
    def get_cpu_freq(self):
        freq = psutil.cpu_freq()
        freq_o = {
            "current": freq.current,
            "min": freq.min,
            "max": freq.max
        }
        return json.dumps(freq_o)
    def get_cpu_stats(self):
        stats = psutil.cpu_stats()
        stats_o = {
            "ctx_switches": stats.ctx_switches,
            "interrupts": stats.interrupts,
            "soft_interrupts": stats.soft_interrupts,
            "syscalls": stats.syscalls
        }
        return json.dumps(stats_o)
    def get_cpu_count(self):
        count = psutil.cpu_count()
        count2 = len(psutil.Process().cpu_affinity())
        if count2 > count:
            count = count2
        return count
    def get_cpu_times_percent(self):
        times_percent = psutil.cpu_times_percent()
        times_percent_o = {
            "user": times_percent.user,
            "nice": times_percent.nice,
            "system": times_percent.system,
            "idle": times_percent.idle,
            "iowait": times_percent.iowait,
            "irq": times_percent.irq,
            "softirq": times_percent.softirq,
            "steal": times_percent.steal,
            "guest": times_percent.guest,
            "guest_nice": times_percent.guest_nice
        }
        return json.dumps(times_percent_o)
    def get_cpu_times(self):
        times = psutil.cpu_times()
        times_o = {
            "user": times.user,
            "nice": times.nice,
            "system": times.system,
            "idle": times.idle,
            "iowait": times.iowait,
            "irq": times.irq,
            "softirq": times.softirq,
            "steal": times.steal,
            "guest": times.guest,
            "guest_nice": times.guest_nice
        }
        return json.dumps(times_o)