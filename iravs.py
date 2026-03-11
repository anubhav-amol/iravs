from analyzer.static_analyzer import analyze_script
from executors.native_executor import run_native


def classify(scores):

    cpu = scores["cpu"]
    disk = scores["disk"]
    network = scores["network"]

    if cpu >= disk and cpu >= network:
        return "CPU_INTENSIVE"

    if disk >= cpu and disk >= network:
        return "DISK_IO"

    return "NETWORK"


def main():

    script = "workloads/cpu_test.py"

    scores = analyze_script(script)

    print("\nWorkload Scores:", scores)

    workload_type = classify(scores)

    print("Predicted Workload:", workload_type)

    print("\nRunning in Native Environment...\n")

    result = run_native(script)

    print("Execution Time:", result["runtime"], "seconds")
    print("Average CPU Usage:", result["avg_cpu"])
    print("Program Output:\n", result["stdout"])


if __name__ == "__main__":
    main()
