import json
import psutil

class Memory:
    def __init__(self):
        pass
    def get_virt_memory(self):
        virtual_memory = psutil.virtual_memory()
        virtual_memory_o = {
            "total": float('{:.3f}'.format(virtual_memory.total / 1024 / 1024 / 1024)),
            "available": float('{:.3f}'.format(virtual_memory.available / 1024 / 1024 / 1024)) ,
            "percent": virtual_memory.percent ,
            "used": float('{:.3f}'.format(virtual_memory.used / 1024 / 1024 / 1024)) ,
            "free": float('{:.3f}'.format(virtual_memory.free / 1024 / 1024 / 1024)) ,
            "active": float('{:.3f}'.format(virtual_memory.active / 1024 / 1024 / 1024)) ,
            "inactive": float('{:.3f}'.format(virtual_memory.inactive / 1024 / 1024 / 1024)) ,
            "buffers": float('{:.3f}'.format(virtual_memory.buffers / 1024 / 1024 / 1024)) ,
            "cached": float('{:.3f}'.format(virtual_memory.cached / 1024 / 1024 / 1024)) ,
            "shared": float('{:.3f}'.format(virtual_memory.shared / 1024 / 1024 / 1024)) ,
            "slab": float('{:.3f}'.format(virtual_memory.slab / 1024 / 1024 / 1024))
        }
        return json.dumps(virtual_memory_o)
    def get_swap_memory(self):
        swap_memory = psutil.swap_memory()
        swap_memory_o = {
            "total": float('{:.3f}'.format(swap_memory.total / 1024 / 1024 / 1024)),
            "used": float('{:.3f}'.format(swap_memory.used / 1024 / 1024 / 1024)),
            "free": float('{:.3f}'.format(swap_memory.free / 1024 / 1024 / 1024)),
            "percent": swap_memory.percent,
            "sin": float('{:.3f}'.format(swap_memory.sin / 1024 / 1024 / 1024)),
            "sout": float('{:.3f}'.format(swap_memory.sout / 1024 / 1024 / 1024))
        }
        return json.dumps(swap_memory_o)