from cpuinfo import get_cpu_info as cpuinfo_get_cpu_info
import psutil
import logging
import platform
import distro


logger = logging.getLogger(__name__)

def get_cpu_temp():

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

def get_cpu_info():
    info = {
        "brand": None,
        "arch": None,
        "bits": None,
        "temp": get_cpu_temp()
    }

    try:
        cpu_info = cpuinfo_get_cpu_info()
        info["brand"] = cpu_info.get("brand_raw")
        info["arch"] = cpu_info.get("arch")
        info["bits"] = cpu_info.get("bits")
    except Exception as e:
        logger.warning(f"Nie udało się pobrać informacji o CPU: {e}")
    
    return info
       
def get_disk_usage():

    info = {
        "total": None,
        "used": None,
        "free": None,
        "percent": None
    }

    try:
        disk = psutil.disk_usage("/")
        info["total"] = disk.total
        info["used"] = disk.used
        info["free"] = disk.free
        info["percent"] = disk.percent

    except Exception as e:
        logger.warning(f"Nie udało się pobrać użycia dysku: {e}")
    
    return info
    

def get_system_info():

    info = {
        "system": None,
        "release": None,
        "distro": None
    }

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

def get_memory_usage():

    info = {
        "total": None,
        "used": None,
        "percent": None
    }

    try:
        mem = psutil.virtual_memory()
        info["total"] = mem.total
        info["used"] = mem.used,
        info["percent"] = mem.percent
        
    except Exception as e:
        logger.warning(f"Nie udało się pobrać danych o pamięci: {e}")
    
    return info


def get_system_metrics():
    return {
        "cpu": get_cpu_info(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "system": get_system_info()
    }