from cpuinfo import get_cpu_info as cpuinfo_get_cpu_info
from typing import Optional
import psutil
import logging
import platform
import distro


logger = logging.getLogger(__name__)

def get_cpu_temp() -> Optional[float]:

    try:
        temps = psutil.sensors_temperatures()
    except Exception as e:
        logger.warning(f"Nie udało się odczytać czujników temperatury: {e}")
        return None

    coretemps = temps.get("coretemp")
    if not coretemps:
        return None

    package_temp = None
    core_values = []

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
    

def get_system_metrics() -> dict:
    return {
        "cpu": get_cpu_info(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "system": get_system_info()
    }