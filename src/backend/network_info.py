import psutil
import socket
from utils.formatters import format_bytes

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