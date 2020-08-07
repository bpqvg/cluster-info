import json
import psutil

class Sensors:
    def __init__(self):
        pass
    def get_sensors_temperatures(self):
        sensors_temperatures = psutil.sensors_temperatures()
        sensors_temperatures_o = []
        for key, val in sensors_temperatures.items():
            val_o = []
            for sensors_temperature in val:
                sensors_temperature_o = {
                    "label": sensors_temperature.label,
                    "current": sensors_temperature.current,
                    "high": sensors_temperature.high,
                    "critical": sensors_temperature.critical
                }
                val_o.append(sensors_temperature_o)
            sensors_temperatures_o.append({key: val_o})
        return json.dumps(sensors_temperatures_o)
    def get_sensors_fans(self):
        sensors_fans = psutil.sensors_fans()
        sensors_fans_o = []
        for key, val in sensors_fans.items():
            val_o = []
            for sensors_fan in val:
                sensors_fan_o = {
                    "label": sensors_fan.label,
                    "current": sensors_fan.current
                }
                val_o.append(sensors_fan_o)
            sensors_fans_o.append({key: val_o})
        return json.dumps(sensors_fans_o)
    def get_sensors_battery(self):
        sensors_battery = psutil.sensors_battery()
        def secs2hours(secs):
            mm, ss = divmod(secs, 60)
            hh, mm = divmod(mm, 60)
            return "%d:%02d:%02d" % (hh, mm, ss)
        sensors_battery_o = {
            "percent": sensors_battery.percent,
            "secsleft": sensors_battery.secsleft,
            "power_plugged": sensors_battery.power_plugged,
            "timeleft": secs2hours(sensors_battery.secsleft)
        }
        return json.dumps(sensors_battery_o)
