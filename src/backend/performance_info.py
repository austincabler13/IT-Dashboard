import psutil 
from utils.formatters import format_bytes, format_percent

def get_performance_info(self):
        memory = psutil.virtual_memory()
        return {
            "cpu_percent": format_percent(psutil.cpu_percent(interval=0.1)),
            "memory_percent": format_percent(memory.percent),
            "memory_used": format_bytes(memory.used),
            "memory_total": format_bytes(memory.total),
        }