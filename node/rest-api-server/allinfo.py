import imp
import os
import json

# Init global vars
current_dir_path = os.path.dirname(os.path.realpath(__file__))
hardware_libs_dir_path = current_dir_path+"/../hardware/"

# Init external libs/modules
cpu = imp.load_source('cpu', hardware_libs_dir_path+"cpu.py")
disks = imp.load_source('disks', hardware_libs_dir_path+"disks.py")
memory = imp.load_source('memory', hardware_libs_dir_path+"memory.py")
network = imp.load_source('network', hardware_libs_dir_path+"network.py")
othersysteminfo = imp.load_source('othersysteminfo', hardware_libs_dir_path+"othersysteminfo.py")
processes = imp.load_source('processes', hardware_libs_dir_path+"processes.py")
sensors = imp.load_source('sensors', hardware_libs_dir_path+"sensors.py")

class AllInfo:
    def __init__(self):
        self.get_all_cpu_info()
        self.get_all_disks_info()
        self.get_all_memory_info()
        self.get_all_network_info()
        self.get_all_othersysteminfo_info()
        self.get_all_processes_info()
        self.get_all_sensors_info()
    def get_all_cpu_info(self):
        cpu_info = cpu.Cpu().get_cpu_info()
        cpu_percent = cpu.Cpu().get_cpu_percent()
        cpu_freq = cpu.Cpu().get_cpu_freq()
        cpu_stats = cpu.Cpu().get_cpu_stats()
        cpu_count = cpu.Cpu().get_cpu_count()
        cpu_times_percent = cpu.Cpu().get_cpu_times_percent()
        cpu_times = cpu.Cpu().get_cpu_times_percent()
        all_cpu_info_o  = {
            "cpu_info": json.loads(cpu_info),
            "cpu_percent": json.loads(cpu_percent),
            "cpu_freq": json.loads(cpu_freq),
            "cpu_stats": json.loads(cpu_stats),
            "cpu_count": json.loads(cpu_count),
            "cpu_times_percent": json.loads(cpu_times_percent),
            "cpu_times": json.loads(cpu_times)
        }
        self.all_cpu_info = json.dumps(all_cpu_info_o)
    def get_all_disks_info(self):
        disk_partitions = disks.Disks().get_disk_partitions()
        disk_usage = disks.Disks().get_disk_usage("/")
        disk_io_counters = disks.Disks().get_disk_io_counters()
        all_disks_info_o = {
            "disk_partitions": json.loads(disk_partitions),
            "disk_usage": json.loads(disk_usage),
            "disk_io_counters": json.loads(disk_io_counters)
        }
        self.all_disks_info = json.dumps(all_disks_info_o)
    def get_all_memory_info(self):
        virt_memory = memory.Memory().get_virt_memory()
        swap_memory = memory.Memory().get_swap_memory()
        all_memory_info_o = {
            "virt_memory": json.loads(virt_memory),
            "swap_memory": json.loads(swap_memory)
        }
        self.all_memory_info = json.dumps(all_memory_info_o)
    def get_all_network_info(self):
        net_io_counters = network.Network().get_net_io_counters()
        net_connections = network.Network().get_net_connections()
        net_if_addrs = network.Network().get_net_if_addrs()
        net_if_stats = network.Network().get_net_if_stats()
        all_network_info_o = {
            "net_io_counters": json.loads(net_io_counters),
            "net_connections": json.loads(net_connections),
            "net_if_addrs": json.loads(net_if_addrs),
            "net_if_stats": json.loads(net_if_stats)
        }
        self.all_network_info = json.dumps(all_network_info_o)
    def get_all_othersysteminfo_info(self):
        boot_time = othersysteminfo.OtherSystemInfo().get_boot_time()
        users = othersysteminfo.OtherSystemInfo().get_users()
        get_all_othersysteminfo_info_o = {
            "boot_time": json.loads(boot_time),
            "users": json.loads(users)
        }
        self.all_othersysteminfo_info = json.dumps(get_all_othersysteminfo_info_o)
    def get_all_processes_info(self):
        pids = processes.Processes().get_pids()
        process_iter = processes.Processes().get_process_iter()
        # get_pid_exists required pid parameter
        all_processes_info_o = {
            "pids": json.loads(pids),
            "process_iter": json.loads(process_iter)
        }
        self.all_processes_info = json.dumps(all_processes_info_o)
    def get_all_sensors_info(self):
        sensors_temperatures = sensors.Sensors().get_sensors_temperatures()
        sensors_fans = sensors.Sensors().get_sensors_fans()
        sensors_battery = sensors.Sensors().get_sensors_battery()
        all_sensors_info_o = {
            "sensors_temperatures": json.loads(sensors_temperatures),
            "sensors_fans": json.loads(sensors_fans),
            "sensors_battery": json.loads(sensors_battery)
        }
        self.all_sensors_info = json.dumps(all_sensors_info_o)

# allinfo = AllInfo()
# print(allinfo.all_sensors_info)