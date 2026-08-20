import csv
import os
import matplotlib.pyplot as plt


DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "metrics.csv"
)


def load_metrics():
    timestamps = []
    cpu_values = []
    memory_values = []
    disk_values = []

    if not os.path.exists(DATA_FILE):
        return timestamps, cpu_values, memory_values, disk_values

    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            timestamps.append(row["timestamp"])
            cpu_values.append(float(row["cpu"]))
            memory_values.append(float(row["memory"]))
            disk_values.append(float(row["disk"]))

    return timestamps, cpu_values, memory_values, disk_values


def create_charts():
    timestamps, cpu, memory, disk = load_metrics()

    if not timestamps:
        print("No historical data available.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, cpu, marker="o")
    plt.title("CPU Usage History")
    plt.xlabel("Time")
    plt.ylabel("CPU Usage (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/cpu_history.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, memory, marker="o")
    plt.title("Memory Usage History")
    plt.xlabel("Time")
    plt.ylabel("Memory Usage (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/memory_history.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, disk, marker="o")
    plt.title("Disk Usage History")
    plt.xlabel("Time")
    plt.ylabel("Disk Usage (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/disk_history.png")
    plt.close()

    print("✅ Historical charts generated successfully.")


if __name__ == "__main__":
    create_charts()