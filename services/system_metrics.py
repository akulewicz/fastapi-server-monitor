from cpuinfo import get_cpu_info as cpuinfo_get_cpu_info
from typing import Optional, List
import psutil
import logging
import platform
import distro
import subprocess


logger = logging.getLogger(__name__)

def get_cpu_temp() -> Optional[float]:

    try:
        temps = psutil.sensors_temperatures()
    except Exception as e:
        logger.warning(f"Nie udało się odczytać czujników temperatury: {e}")
        return None

    coretemps = temps.get("coretemp")

    package_temp = None
    core_values = []

    if coretemps:
        for t in coretemps:
            if "Package" in t.label:
                package_temp = t.current
            elif "Core" in t.label:
                core_values.append(t.current)
    
    if package_temp is not None:
        return package_temp
    
    if len(core_values) > 0:
        avg_cpu_temp = sum(core_values) / len(core_values)
        return avg_cpu_temp

    if "raspberrypi" in platform.uname().node.lower():
        output = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
        return float(output.split('=')[1].split("'")[0])

    
    return None

def get_cpu_info() -> dict:

    info = {
        "temp": get_cpu_temp()
    }

    try:
        cpu_info = cpuinfo_get_cpu_info()
        info["brand"] = cpu_info.get("brand_raw")
        info["arch"] = cpu_info.get("arch")
        info["bits"] = cpu_info.get("bits")
    except Exception as e:
        logger.warning(f"Nie udało się pobrać informacji o CPU: {e}")
        return {}
    
    return info
       
def get_disk_usage() -> dict:

    try:
        disk = psutil.disk_usage("/")
        return {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": disk.percent
        }
    except Exception as e:
        logger.warning(f"Nie udało się pobrać użycia dysku: {e}")
        return {}
    

def get_system_info() -> dict:

    info = {}

    try:
        info['system'] = platform.system()
    except Exception as e:
        logger.warning(f'Błąd przy pobieraniu systemu: {e}')

    try:
        info['release'] = platform.release()
    except Exception as e:
        logger.warning(f'Błąd przy pobieraniu wersji systemu: {e}')

    try:
        info['distro'] = distro.name(pretty=True)
    except Exception as e:
        logger.warning(f'Błąd przy pobieraniu dystrybcji: {e}')

    return info

def get_memory_usage() -> dict:

    try:
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "used": mem.used,
            "percent": mem.percent
        }
    except Exception as e:
        logger.warning(f"Nie udało się pobrać danych o pamięci: {e}")
        return {}


def get_connected_users() -> dict:
    users = {"connected_users": []}
   
    try:
        result = subprocess.run(["who"], capture_output=True, text=True)
        lines = result.stdout.strip().split("\n")

        for line in lines:
            if not line.strip():
                continue
            parts = line.split()
            name = parts[0]
            host = parts[-1]
            users["connected_users"].append({
                "name": name,
                "host": host
            })
        return users
    except Exception as e:
        logger.warning(f"Nie udał osię pobrać listy użytkowników: {e}")
    return users 

    
def get_system_metrics() -> dict:
    return {
        "cpu": get_cpu_info(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "system": get_system_info(),
        "users": get_connected_users()
    }