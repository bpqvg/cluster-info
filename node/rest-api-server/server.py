from flask import Flask, json
import imp
import os

# Init global vars
current_dir_path = os.path.dirname(os.path.realpath(__file__))
hardware_libs_dir_path = current_dir_path+"/../hardware/"

api = Flask(__name__)

# Init external libs/modules
cpu = imp.load_source('cpu', hardware_libs_dir_path+"cpu.py")

# Flask. Rest api. Cpu
@api.route('/get_cpu_info', methods=['GET'])
def rest_get_cpu_info():
    local_cpu = cpu.Cpu().get_cpu_info()
    return json.dumps(json.loads(local_cpu))

@api.route('/get_cpu_percent', methods=['GET'])
def rest_get_cpu_percent():
    local_cpu = cpu.Cpu().get_cpu_percent()
    return json.dumps(json.loads(local_cpu))

@api.route('/get_cpu_freq', methods=['GET'])
def rest_get_cpu_freq():
    local_cpu = cpu.Cpu().get_cpu_freq()
    return json.dumps(json.loads(local_cpu))

@api.route('/get_cpu_stats', methods=['GET'])
def rest_get_cpu_stats():
    local_cpu = cpu.Cpu().get_cpu_stats()
    return json.dumps(json.loads(local_cpu))

@api.route('/get_cpu_count', methods=['GET'])
def rest_get_cpu_count():
    local_cpu = cpu.Cpu().get_cpu_count()
    return json.dumps(json.loads(local_cpu))

@api.route('/get_cpu_times_percent', methods=['GET'])
def rest_get_cpu_times_percent():
    local_cpu = cpu.Cpu().get_cpu_times_percent()
    return json.dumps(json.loads(local_cpu))

@api.route('/get_cpu_times', methods=['GET'])
def rest_get_cpu_times():
    local_cpu = cpu.Cpu().get_cpu_times()
    return json.dumps(json.loads(local_cpu))

# Flask. Rest api. Disks





if __name__ == "__main__":
    api.run(host='0.0.0.0', port=55802)