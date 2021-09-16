from typing import List

import pySMART


def get_hdd_temperatures() -> List[float]:
    return [float(device.temperature) for device in pySMART.DeviceList()]
