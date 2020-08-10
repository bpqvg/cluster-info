import json
import psutil

class Disks:
    def __init__(self):
        pass 
    def get_disk_partitions(self):
        disk_partitions = psutil.disk_partitions()
        disk_partitions_o = []
        for disk_partition in disk_partitions:
            disk_partition_o = {
                "device": disk_partition.device,
                "mountpoint": disk_partition.mountpoint,
                "fstype": disk_partition.fstype,
                "opts": disk_partition.opts
            }
            disk_partitions_o.append(disk_partition_o)
        return json.dumps(disk_partitions_o)
    def get_disk_usage(self, path):
        disk_usage = psutil.disk_usage(path)
        disk_usage_o = {
            "total": float('{:.3f}'.format(disk_usage.total / 1024 / 1024 / 1024)),
            "used": float('{:.3f}'.format(disk_usage.used / 1024 / 1024 / 1024)),
            "free": float('{:.3f}'.format(disk_usage.free / 1024 / 1024 / 1024)),
            "percent": disk_usage.percent,
        }
        return json.dumps(disk_usage_o)
    def get_disks_usage(self):
        disks_usage = []
        for disk_partition in psutil.disk_partitions():
            mountpoint = disk_partition.mountpoint
            disks_usage.append({mountpoint: json.loads(self.get_disk_usage(mountpoint))})
        return json.dumps(disks_usage)
    def get_disk_io_counters(self):
        disk_io_counters = psutil.disk_io_counters(perdisk=True)
        disk_io_counters_o = []
        for key, val in disk_io_counters.items():
            val_o = {
                    "read_count": val.read_count,
                    "write_count": val.write_count, 
                    "read_bytes": val.read_bytes,
                    "write_bytes": val.write_bytes, 
                    "read_time": val.read_time,
                    "write_time": val.write_time,
                    "read_merged_count": val.read_merged_count,
                    "write_merged_count": val.write_merged_count,
                    "busy_time": val.busy_time
            }
            disk_io_counter = {
                key: val_o
            }
            disk_io_counters_o.append(disk_io_counter)
        return json.dumps(disk_io_counters_o)

# disks = Disks()
# print(disks.get_disks_usage())