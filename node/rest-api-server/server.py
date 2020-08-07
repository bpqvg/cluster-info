from flask import Flask, json, request
import imp
import os

# Init global vars
current_dir_path = os.path.dirname(os.path.realpath(__file__))
hardware_libs_dir_path = current_dir_path+"/../hardware/"

api = Flask(__name__)

# Init external libs/modules
cpu = imp.load_source('cpu', hardware_libs_dir_path+"cpu.py")
disks = imp.load_source('disks', hardware_libs_dir_path+"disks.py")
memory = imp.load_source('memory', hardware_libs_dir_path+"memory.py")
network = imp.load_source('network', hardware_libs_dir_path+"network.py")
othersysteminfo = imp.load_source('othersysteminfo', hardware_libs_dir_path+"othersysteminfo.py")
processes = imp.load_source('processes', hardware_libs_dir_path+"processes.py")
sensors = imp.load_source('sensors', hardware_libs_dir_path+"sensors.py")


# Flask. Rest api. Cpu
@api.route('/cpu/get_cpu_info', methods=['GET'])
def rest_get_cpu_info():
    local_cpu = cpu.Cpu().get_cpu_info()
    return json.dumps(json.loads(local_cpu))

@api.route('/cpu/get_cpu_percent', methods=['GET'])
def rest_get_cpu_percent():
    local_cpu = cpu.Cpu().get_cpu_percent()
    return json.dumps(json.loads(local_cpu))

@api.route('/cpu/get_cpu_freq', methods=['GET'])
def rest_get_cpu_freq():
    local_cpu = cpu.Cpu().get_cpu_freq()
    return json.dumps(json.loads(local_cpu))

@api.route('/cpu/get_cpu_stats', methods=['GET'])
def rest_get_cpu_stats():
    local_cpu = cpu.Cpu().get_cpu_stats()
    return json.dumps(json.loads(local_cpu))

@api.route('/cpu/get_cpu_count', methods=['GET'])
def rest_get_cpu_count():
    local_cpu = cpu.Cpu().get_cpu_count()
    return json.dumps(json.loads(local_cpu))

@api.route('/cpu/get_cpu_times_percent', methods=['GET'])
def rest_get_cpu_times_percent():
    local_cpu = cpu.Cpu().get_cpu_times_percent()
    return json.dumps(json.loads(local_cpu))

@api.route('/cpu/get_cpu_times', methods=['GET'])
def rest_get_cpu_times():
    local_cpu = cpu.Cpu().get_cpu_times()
    return json.dumps(json.loads(local_cpu))

# Flask. Rest api. Disks
@api.route('/disks/get_disk_partitions', methods=['GET'])
def rest_get_disk_partitions():
    local_disks = disks.Disks().get_disk_partitions()
    return json.dumps(json.loads(local_disks))

@api.route('/disks/get_disk_usage', methods=['GET'])
def rest_get_disk_usage():
    arg_path = request.args.get('path')
    #print(arg_path)
    local_disks = disks.Disks().get_disk_usage(path=arg_path)
    return json.dumps(json.loads(local_disks))

@api.route('/disks/get_disk_io_counters', methods=['GET'])
def rest_get_disk_io_counters():
    local_disks = disks.Disks().get_disk_io_counters()
    return json.dumps(json.loads(local_disks))

# Flask. Rest api. Memory
@api.route('/memory/get_virt_memory', methods=['GET'])
def rest_get_virt_memory():
    local_memory = memory.Memory().get_virt_memory()
    return json.dumps(json.loads(local_memory))

@api.route('/memory/get_swap_memory', methods=['GET'])
def rest_get_swap_memory():
    local_memory = memory.Memory().get_swap_memory()
    return json.dumps(json.loads(local_memory))


# Flask. Rest api. Network
@api.route('/network/get_net_io_counters', methods=['GET'])
def rest_get_net_io_counters():
    local_network = network.Network().get_net_io_counters()
    return json.dumps(json.loads(local_network))

@api.route('/network/get_net_connections', methods=['GET'])
def rest_get_net_connections():
    local_network = network.Network().get_net_connections()
    return json.dumps(json.loads(local_network))

@api.route('/network/get_net_if_addrs', methods=['GET'])
def rest_get_net_if_addrs():
    local_network = network.Network().get_net_if_addrs()
    return json.dumps(json.loads(local_network))

@api.route('/network/get_net_if_stats', methods=['GET'])
def rest_get_net_if_stats():
    local_network = network.Network().get_net_if_stats()
    return json.dumps(json.loads(local_network))


# Flask. Rest api. OtherSystemInfo
@api.route('/othersysteminfo/get_boot_time', methods=['GET'])
def rest_get_boot_time():
    local_othersysteminfo = othersysteminfo.OtherSystemInfo().get_boot_time()
    return json.dumps(json.loads(local_othersysteminfo))

@api.route('/othersysteminfo/get_users', methods=['GET'])
def rest_get_users():
    local_othersysteminfo = othersysteminfo.OtherSystemInfo().get_users()
    return json.dumps(json.loads(local_othersysteminfo))


# Flask. Rest api. Processes
@api.route('/processes/get_pids', methods=['GET'])
def rest_get_pids():
    local_processes = processes.Processes().get_pids()
    return json.dumps(json.loads(local_processes))

@api.route('/processes/get_process_iter', methods=['GET'])
def rest_get_process_iter():
    local_processes = processes.Processes().get_process_iter()
    return json.dumps(json.loads(local_processes))

@api.route('/processes/get_pid_exists', methods=['GET'])
def rest_get_pid_exists():
    arg_pid = int(request.args.get('pid'))
    local_processes = processes.Processes().get_pid_exists(pid=arg_pid)
    return json.dumps(json.loads(local_processes))


# Flask. Rest api. Sensors
@api.route('/sensors/get_sensors_temperatures', methods=['GET'])
def rest_get_sensors_temperatures():
    local_sensors = sensors.Sensors().get_sensors_temperatures()
    return json.dumps(json.loads(local_sensors))

@api.route('/sensors/get_sensors_fans', methods=['GET'])
def rest_get_sensors_fans():
    local_sensors = sensors.Sensors().get_sensors_fans()
    return json.dumps(json.loads(local_sensors))

@api.route('/sensors/get_sensors_battery', methods=['GET'])
def rest_get_sensors_battery():
    local_sensors = sensors.Sensors().get_sensors_battery()
    return json.dumps(json.loads(local_sensors))




if __name__ == "__main__":
    api.run(host='0.0.0.0', port=55802)