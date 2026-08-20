def generate_process_alerts(processes):
    alerts = []

    for process in processes:
        name = process["name"]
        cpu = process["cpu"]
        memory = process["memory"]

        if cpu >= 80:
            alerts.append(
                f"High CPU usage by {name}: {cpu}%"
            )

        if memory >= 10:
            alerts.append(
                f"High memory usage by {name}: {memory}%"
            )

    return alerts