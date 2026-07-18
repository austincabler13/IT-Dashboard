import platform
import winreg
import psutil
from utils.formatters import format_percent, format_bytes


def get_cpu_name():
    try:
        registry_path = (
            r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
        )

        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            registry_path
        ) as registry_key:
            cpu_name, _ = winreg.QueryValueEx(
                registry_key,
                "ProcessorNameString"
            )

        return cpu_name.strip()

    except OSError:
        return platform.processor() or "Unknown Processor"
    
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
            "cpu_name":get_cpu_name(),
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

    def get_storage_info(self):
        drives = []

        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
            except (PermissionError, OSError):
                continue

            drives.append({
                "drive_letter": partition.device,
                "mount_point": partition.mountpoint,
                "file_system": partition.fstype or "Unknown",
                "total_space": format_bytes(usage.total),
                "used_space": format_bytes(usage.used),
                "free_space": format_bytes(usage.free),
                "drive_usage": format_percent(usage.percent),
            })

        return {
            "drives": drives
        }