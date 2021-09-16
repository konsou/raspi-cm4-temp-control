from time import sleep

from hdd import get_hdd_temperatures
from cpu import get_cpu_temperature


TEMPERATURE_MONITOR_INTERVAL = 2  # seconds


def monitor_temperatures():
    while True:
        print(f'-----')
        print(f'CPU temperature:  {get_cpu_temperature()}')
        print(f'HDD temperatures: {get_hdd_temperatures()}')
        sleep(TEMPERATURE_MONITOR_INTERVAL)


if __name__ == '__main__':
    monitor_temperatures()
