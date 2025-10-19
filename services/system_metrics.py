import psutil

def get_cpu_temp():
    try:
        temps = psutil.sensors_temperatures()
    except Exception:
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
        return None