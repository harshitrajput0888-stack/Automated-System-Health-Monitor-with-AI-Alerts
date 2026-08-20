def calculate_health_score(metrics):
    score = 100

    if metrics["cpu"] >= 80:
        score -= 25
    elif metrics["cpu"] >= 60:
        score -= 10

    if metrics["memory"] >= 90:
        score -= 30
    elif metrics["memory"] >= 80:
        score -= 20
    elif metrics["memory"] >= 60:
        score -= 10

    if metrics["disk"] >= 90:
        score -= 25
    elif metrics["disk"] >= 80:
        score -= 10

    return max(score, 0)


def get_health_status(score):
    if score >= 80:
        return "Healthy"
    elif score >= 60:
        return "Warning"
    else:
        return "Critical"