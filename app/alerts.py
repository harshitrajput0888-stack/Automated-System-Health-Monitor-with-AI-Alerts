def generate_alerts(metrics):
    alerts = []

    if metrics["cpu"] >= 80:
        alerts.append("High CPU usage detected")

    if metrics["memory"] >= 80:
        alerts.append("High memory usage detected")

    if metrics["disk"] >= 80:
        alerts.append("High disk usage detected")

    return alerts