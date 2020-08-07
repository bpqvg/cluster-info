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
    print(arg_path)
    local_disks = disks.Disks().get_disk_usage(path=arg_path)
    return json.dumps(json.loads(local_disks))

@api.route('/disks/get_disk_io_counters', methods=['GET'])
def rest_get_disk_io_counters():
    local_disks = disks.Disks().get_disk_io_counters()
    return json.dumps(json.loads(local_disks))

# Flask. Rest api. Memory






if __name__ == "__main__":
    api.run(host='0.0.0.0', port=55802)