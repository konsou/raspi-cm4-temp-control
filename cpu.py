def get_cpu_temperature() -> float:
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        return float(f.read()) / 1000
