from monitor import get_system_metrics
from alerts import generate_alerts
from health import calculate_health_score, get_health_status
from process_monitor import get_top_processes
from process_alerts import generate_process_alerts

from logger import logger


def main():

    logger.info("System health monitoring started")

    try:

        # Get system metrics
        metrics = get_system_metrics()

        # Calculate health
        health_score = calculate_health_score(metrics)
        health_status = get_health_status(health_score)

        # Get processes
        processes = get_top_processes()

        # Generate alerts
        system_alerts = generate_alerts(metrics)
        process_alerts = generate_process_alerts(processes)

        # Log monitoring information
        logger.info(
            f"System metrics collected | "
            f"CPU={metrics['cpu']}% | "
            f"Memory={metrics['memory']}% | "
            f"Disk={metrics['disk']}%"
        )

        logger.info(
            f"Health score calculated: "
            f"{health_score}/100 | "
            f"Status={health_status}"
        )

        if system_alerts:
            for alert in system_alerts:
                logger.warning(
                    f"System alert: {alert}"
                )

        if process_alerts:
            for alert in process_alerts:
                logger.warning(
                    f"Process alert: {alert}"
                )

        # =========================
        # DISPLAY RESULTS
        # =========================

        print("\n=== SYSTEM HEALTH MONITOR ===")

        print(
            f"CPU Usage    : {metrics['cpu']}%"
        )

        print(
            f"Memory Usage : {metrics['memory']}%"
        )

        print(
            f"Disk Usage   : {metrics['disk']}%"
        )

        print(
            f"\nHealth Score : {health_score}/100"
        )

        print(
            f"Status       : {health_status}"
        )

        # =========================
        # PROCESSES
        # =========================

        print(
            "\n=== TOP RESOURCE-CONSUMING PROCESSES ==="
        )

        for process in processes:

            print(
                f"{process['name']} "
                f"(PID: {process['pid']}) | "
                f"CPU: {process['cpu']}% | "
                f"Memory: {process['memory']}%"
            )

        # =========================
        # ALERTS
        # =========================

        print("\n=== ALERTS ===")

        if system_alerts:

            for alert in system_alerts:
                print(f"⚠️ {alert}")

        else:

            print(
                "✅ No system-level alerts."
            )

        if process_alerts:

            for alert in process_alerts:
                print(f"⚠️ {alert}")

        logger.info(
            "System health monitoring completed successfully"
        )

    except Exception as e:

        logger.exception(
            f"System monitoring failed: {str(e)}"
        )

        print(
            f"\n❌ System monitoring error: {str(e)}"
        )


if __name__ == "__main__":
    main()