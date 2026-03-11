import subprocess
import time
import os


def run_docker(script_path):

    project_dir = os.getcwd()

    docker_command = [
        "docker",
        "run",
        "--rm",
        "-v", f"{project_dir}:/app",
        "-w", "/app",
        "python:3.10",
        "python",
        script_path
    ]

    start_time = time.time()

    try:
        process = subprocess.run(
            docker_command,
            capture_output=True,
            text=True,
            timeout=120
        )
    except subprocess.TimeoutExpired:
        return {
            "runtime": None,
            "stdout": "",
            "stderr": "Docker execution timed out"
        }

    end_time = time.time()

    runtime = end_time - start_time

    return {
        "runtime": runtime,
        "stdout": process.stdout,
        "stderr": process.stderr
    }
