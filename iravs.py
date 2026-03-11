from analyzer.static_analyzer import analyze_script


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

    print("Workload scores:", scores)

    category = classify(scores)

    print("Predicted workload type:", category)


if __name__ == "__main__":
    main()
