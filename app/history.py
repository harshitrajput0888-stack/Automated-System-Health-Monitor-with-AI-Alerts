import csv
import os
from datetime import datetime


DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "metrics.csv"
)


def save_metrics(metrics):
    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(DATA_FILE) == 0:
            writer.writerow([
                "timestamp",
                "cpu",
                "memory",
                "disk"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            metrics["cpu"],
            metrics["memory"],
            metrics["disk"]
        ])