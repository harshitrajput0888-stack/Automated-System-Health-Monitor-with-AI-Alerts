import psutil


def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "cpu": cpu,
        "memory": memory.percent,
        "disk": disk.percent
    }