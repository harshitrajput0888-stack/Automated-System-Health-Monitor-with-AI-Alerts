from app.alerts import generate_alerts


def test_no_alerts():

    metrics = {
        "cpu": 30,
        "memory": 50,
        "disk": 60
    }

    alerts = generate_alerts(metrics)

    assert alerts == []


def test_high_cpu_alert():

    metrics = {
        "cpu": 85,
        "memory": 50,
        "disk": 60
    }

    alerts = generate_alerts(metrics)

    assert "High CPU usage detected" in alerts


def test_high_memory_alert():

    metrics = {
        "cpu": 30,
        "memory": 85,
        "disk": 60
    }

    alerts = generate_alerts(metrics)

    assert "High memory usage detected" in alerts


def test_high_disk_alert():

    metrics = {
        "cpu": 30,
        "memory": 50,
        "disk": 90
    }

    alerts = generate_alerts(metrics)

    assert "High disk usage detected" in alerts