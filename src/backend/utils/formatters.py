def format_bytes(value):
    units = ["B", "KB", "MB", "GB", "TB"]

    value = float(value)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"
        
        value /= 1024
    return value

def format_percent(value):
    return f"{float(value):.1f}%"