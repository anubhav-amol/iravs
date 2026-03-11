from analyzer.static_analyzer import analyze_script
from analyzer.decision_engine import choose_environment

from executors.native_executor import run_native
from executors.docker_executor import run_docker
from executors.kvm_executor import run_kvm


def main():

    # Script to analyze and execute
    script = "workloads/cpu_test.py"

    print("\n========== IRAVS SYSTEM ==========\n")

    # Step 1 — Analyze workload
    scores = analyze_script(script)

    print("Workload Scores:")
    print(scores)

    # Step 2 — Choose best environment
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

        print("Unknown environment selected.")
        return

    # Step 4 — Show results
    print("\n========== EXECUTION RESULT ==========\n")

    print("Runtime:", result["runtime"], "seconds")

    if result.get("stdout"):
        print("\nProgram Output:")
        print(result["stdout"])

    if result.get("stderr"):
        print("\nErrors:")
        print(result["stderr"])


if __name__ == "__main__":
    main()
