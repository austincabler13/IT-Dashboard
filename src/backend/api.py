import platform

import psutil


class API:
    def get_system_info(self):
        return {
            "os": platform.system(),
            "computer_name": platform.node(),
            "bitness": platform.architecture()[0],
            "architecture": platform.machine(),
            "python_version": platform.python_version(),
        }

    def get_hardware_info(self):
        total_memory_gb = psutil.virtual_memory().total / (1024 ** 3)

       