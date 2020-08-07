import json
import psutil

class Network:
    def __init__(self):
        pass
    def get_net_io_counters(self):
        net_io_counters = psutil.net_io_counters(pernic=True);
        net_io_counters_o = []
        for key, val in net_io_counters.items():
            val_o = {
                "bytes_sent": val.bytes_sent,
                "bytes_recv": val.bytes_recv,
                "packets_sent": val.packets_sent, 
                "packets_recv": val.packets_recv,
                "errin": val.errin,
                "errout": val.errout,
                "dropin": val.dropin,
                "dropout": val.dropout
            }
            net_io_counter = {
                key: val_o
            }
            net_io_counters_o.append(net_io_counter)
        return json.dumps(net_io_counters_o)
    def get_net_connections(self):
        net_connections = psutil.net_connections()
        net_connections_o = []
        for net_connection in net_connections:
            net_connection_o = {
                "fd": net_connection.fd,
                "family": net_connection.family,
                "type": net_connection.type,
                "laddr": net_connection.laddr,
                "raddr": net_connection.raddr,
                "status": net_connection.status
            }
            net_connections_o.append(net_connection_o)
        return json.dumps(net_connections_o)
    def get_net_if_addrs(self):
        net_if_addrs = psutil.net_if_addrs()
        net_if_addrs_o = []
        for key, val in net_if_addrs.items():
            #net_if_addr_o = []
            val_o = []
            for net_if_addr in val:
                net_if_addr_o = {
                    "family": net_if_addr.family,
                    "address": net_if_addr.address,
                    "netmask": net_if_addr.netmask,
                    "broadcast": net_if_addr.broadcast,
                    "ptp": net_if_addr.ptp
                }
                val_o.append(net_if_addr_o)
            net_if_addrs_o.append({key: val_o})
        return json.dumps(net_if_addrs_o)
    def get_net_if_stats(self):
        net_if_stats = psutil.net_if_stats()
        net_if_stats_o = []
        for key, val in net_if_stats.items():
            val_o = {
                "isup:": val.isup,
                "duplex": val.duplex,
                "speed": val.speed,
                "mtu": val.mtu
            }
            net_if_stats_o.append({key: val_o})
        return json.dumps(net_if_stats_o)
