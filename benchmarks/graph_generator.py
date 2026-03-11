import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def generate_graph():

    runtimes = defaultdict(list)

    with open("benchmarks/results.csv", "r") as f:

        reader = csv.DictReader(f)

        for row in reader:
            runtimes[row["environment"]].append(float(row["runtime"]))

    environments = []
    averages = []

    for env, values in runtimes.items():
        environments.append(env)
        averages.append(sum(values) / len(values))

    plt.figure()

    plt.bar(environments, averages)

    plt.xlabel("Execution Environment")
    plt.ylabel("Average Runtime (seconds)")
    plt.title("IRAVS Environment Performance Comparison")

    plt.savefig("benchmarks/performance.png")

    print("Graph saved as benchmarks/performance.png")
