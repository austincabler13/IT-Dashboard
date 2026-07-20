import platform
import winreg
import psutil
from utils.formatters import format_percent, format_bytes
import socket


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


    def get_network_info(self): 
        ipaddresses = psutil.net_if_addrs()
        net_stats = psutil.net_if_stats()
        net_io = psutil.net_io_counters()
        adapters = []

        for interface, addresses in ipaddresses.items():
            adapter_info = {
                "name": interface,
                "ipv4": None,
                "ipv6": None,
                "mac": None,
                "is_up": False,
                "speed_mbps": 0
            }

            af_packet = getattr(socket, "AF_PACKET", None)
            for address in addresses:
                if address.family == socket.AF_INET:
                    adapter_info["ipv4"] = address.address
                elif address.family == socket.AF_INET6:
                    adapter_info["ipv6"] = address.address
                elif getattr(psutil, "AF_LINK", None) is not None and address.family == psutil.AF_LINK:
                    adapter_info["mac"] = address.address
                else:
                    # fallback for platforms using socket.AF_PACKET for MAC
                    if af_packet is not None and address.family == af_packet:
                        adapter_info["mac"] = address.address

            stats = net_stats.get(interface)
            if stats:
                adapter_info["is_up"] = stats.isup
                adapter_info["speed_mbps"] = stats.speed

            adapters.append(adapter_info)
        return {
             "network_usage": {
                "bytes_sent": format_bytes(net_io.bytes_sent),
                "bytes_received": format_bytes(net_io.bytes_recv),
                "packets_sent": net_io.packets_sent,
                "packets_received": net_io.packets_recv,
        },
        "adapters": adapters
    }