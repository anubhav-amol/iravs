import sys

from analyzer.static_analyzer import analyze_script
from analyzer.decision_engine import choose_environment

from executors.native_executor import run_native
from executors.docker_executor import run_docker
from executors.kvm_executor import run_kvm

from benchmarks.performance_logger import log_result
from benchmarks.graph_generator import generate_graph


def benchmark_mode():

    print("\nRunning Benchmark Mode...\n")

    scripts = [
        "workloads/cpu_test.py",
        "workloads/disk_test.py",
        "workloads/network_test.py"
    ]

    for script in scripts:

        print("\n===============================")
        print("Testing workload:", script)
        print("===============================\n")

        print("Running Native Execution...")
        native_result = run_native(script)
        print("Native Runtime:", native_result["runtime"])

        print("\nRunning Docker Execution...")
        docker_result = run_docker(script)
        print("Docker Runtime:", docker_result["runtime"])

        print("\nRunning KVM Execution...")
        kvm_result = run_kvm(script)
        print("KVM Runtime:", kvm_result["runtime"])

        # Log results
        log_result("native", native_result["runtime"])
        log_result("docker", docker_result["runtime"])
        log_result("kvm", kvm_result["runtime"])


def decision_mode(script):

    scores = analyze_script(script)

    print("\nWorkload Scores:")
    print(scores)

    print("\nRunning Decision Mode...\n")

    env = choose_environment(scores)

    print("Selected Execution Environment:", env)

    if env == "native":

        result = run_native(script)

    elif env == "docker":

        result = run_docker(script)

    else:

        result = run_kvm(script)

    runtime = result["runtime"]

    print("\n========== EXECUTION RESULT ==========\n")

    print("Runtime:", runtime, "seconds")

    if result.get("stdout"):
        print("\nProgram Output:")
        print(result["stdout"])

    if result.get("stderr"):
        print("\nErrors:")
        print(result["stderr"])

    log_result(env, runtime)


def main():

    print("\n========== IRAVS SYSTEM ==========\n")

    if len(sys.argv) < 2:

        print("Usage:")
        print("  python iravs.py benchmark")
        print("  python iravs.py decision workloads/cpu_test.py")
        return

    mode = sys.argv[1]

    if mode == "benchmark":

        benchmark_mode()

    elif mode == "decision":

        if len(sys.argv) < 3:
            print("Please provide a workload script.")
            print("Example: python iravs.py decision workloads/cpu_test.py")
            return

        script = sys.argv[2]

        decision_mode(script)

    else:

        print("Invalid mode.")
        print("Use 'benchmark' or 'decision'.")
        return

    generate_graph()

    print("\nResults saved in benchmarks/results.csv")
    print("Graph saved in benchmarks/performance.png")


if __name__ == "__main__":
    main()
