from analyzer.static_analyzer import analyze_script
from executors.native_executor import run_native
from executors.docker_executor import run_docker


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

    print("\nRunning Native Execution...\n")

    native_result = run_native(script)

    print("Native Runtime:", native_result["runtime"])

    print("\nRunning Docker Execution...\n")

    docker_result = run_docker(script)

    print("Docker Runtime:", docker_result["runtime"])


if __name__ == "__main__":
    main()
