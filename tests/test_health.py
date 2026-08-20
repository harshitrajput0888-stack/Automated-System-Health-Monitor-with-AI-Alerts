from app.health import calculate_health_score, get_health_status


def test_healthy_system():

    metrics = {
        "cpu": 20,
        "memory": 40,
        "disk": 50
    }

    score = calculate_health_score(metrics)

    assert score == 100
    assert get_health_status(score) == "Healthy"


def test_high_memory():

    metrics = {
        "cpu": 20,
        "memory": 85,
        "disk": 50
    }

    score = calculate_health_score(metrics)

    assert score == 80
    assert get_health_status(score) == "Healthy"


def test_critical_system():

    metrics = {
        "cpu": 95,
        "memory": 95,
        "disk": 95
    }

    score = calculate_health_score(metrics)

    assert score < 60
    assert get_health_status(score) == "Critical"