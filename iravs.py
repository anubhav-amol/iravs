from analyzer.static_analyzer import analyze_script
from analyzer.decision_engine import choose_environment

from executors.native_executor import run_native
from executors.docker_executor import run_docker
from executors.kvm_executor import run_kvm

from benchmarks.performance_logger import log_result
from benchmarks.graph_generator import generate_graph


def main():

    print("\n========== IRAVS SYSTEM ==========\n")

    # Script to execute
    script = "workloads/cpu_test.py"

    # Step 1 — Analyze workload
    scores = analyze_script(script)

    print("Workload Scores:")
    print(scores)

    # Step 2 — Select environment
    env = choose_environment(scores)

    print("\nSelected Execution Environment:", env)

    # Step 3 — Execute workload
    print("\nExecuting workload...\n")

    if env == "native":

        result = run_native(script)

    elif env == "docker":

        result = run_docker(script)

    elif env == "kvm":

        result = run_kvm(script)

    else:

        print("Unknown execution environment.")
        return

    runtime = result["runtime"]

    # Step 4 — Display results
    print("\n========== EXECUTION RESULT ==========\n")

    print("Runtime:", runtime, "seconds")

    if result.get("stdout"):
        print("\nProgram Output:")
        print(result["stdout"])

    if result.get("stderr"):
        print("\nErrors:")
        print(result["stderr"])

    # Step 5 — Log results
    log_result(env, runtime)

    # Step 6 — Generate performance graph
    generate_graph()

    print("\nResults saved in benchmarks/results.csv")
    print("Graph saved in benchmarks/performance.png")


if __name__ == "__main__":
    main()
