import platform
import psutil


class API:
    def get_system_info(self):
        return {
            "os": platform.system(),
            "computer_name": platform.node(),
            "bitness": platform.architecture()[0],
            "architecture": platform.machine(),
            "python_version": platform.python_version()
        }
    def get_hardware_info(self):
            return {
            "cpu_name": platform.processor(),
            "physical_cores": psutil.cpu_count(logical=False),
            "logical_processors": psutil.cpu_count(logical=True),
            "total_memory": psutil.virtual_memory().total,
        }