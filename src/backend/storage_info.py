import psutil
from utils.formatters import format_bytes, format_percent

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

        return { "drives": drives }