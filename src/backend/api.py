import platform
import psutil
from utils.formatters import format_percent, format_bytes


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
            "total_memory": format_bytes(psutil.virtual_memory().total)
        }

    def get_performance_info(self):
        memory = psutil.virtual_memory()
        return {
            "cpu_percent": format_percent(psutil.cpu_percent(interval=0.1)),
            "memory_percent": format_percent(memory.percent),
            "memory_used": format_bytes(memory.used),
            "memory_total": format_bytes(memory.total),
        }