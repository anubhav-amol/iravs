import csv
import matplotlib.pyplot as plt


def generate_graph():

    environments = []
    runtimes = []

    with open("benchmarks/results.csv", "r") as f:

        reader = csv.DictReader(f)

        for row in reader:
            environments.append(row["environment"])
            runtimes.append(float(row["runtime"]))

    plt.figure()

    plt.bar(environments, runtimes)

    plt.xlabel("Execution Environment")
    plt.ylabel("Runtime (seconds)")
    plt.title("IRAVS Environment Performance Comparison")

    plt.savefig("benchmarks/performance.png")

    print("Graph saved as benchmarks/performance.png")
