import winreg
import platform
import psutil
from utils.formatters import format_bytes

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
    


def get_hardware_info(self):
        return {
            "cpu_name":get_cpu_name(),
            "physical_cores": psutil.cpu_count(logical=False),
            "logical_processors": psutil.cpu_count(logical=True),
            "total_memory": format_bytes(psutil.virtual_memory().total),
            "cpu_frequency": psutil.cpu_freq().max if psutil.cpu_freq() else None,
            "available_memory": format_bytes(psutil.virtual_memory().available) if psutil.virtual_memory() else None,
            "Motherboard": {
                "manufacturer": None,
                "model": None,
                "serial_number": None
            },
            "BIOS": {
                "manufacturer": None,
                "version": None,
                "release_date": None
            },
            "GPU": {
                "name": None,
                "manufacturer": None,
                "driver_version": None,
                "video_memory": None
            }
        }