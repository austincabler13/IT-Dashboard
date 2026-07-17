import platform
import psutil


class API:
    def __init__(self):

        psutil.cpu_percent(interval=None)

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

    def get_performance_info(self):
        memory = psutil.virtual_memory()
        return {
            "cpu_percent": round(psutil.cpu_percent(interval=None), 1),
            "memory_percent": round(memory.percent, 1),
            "memory_used": memory.used,
            "memory_total": memory.total,
        }