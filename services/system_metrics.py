import psutil
import logging

logger = logging.getLogger(__name__)

def get_cpu_temp():
    try:
        temps = psutil.sensors_temperatures()
    except Exception:
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
  

def get_disk_usage():
    try:
        return psutil.disk_usage("/").percent
    except Exception as e:
        logging.warning(f"Nie udało się pobrać użycia dysku: {e}")
        return None