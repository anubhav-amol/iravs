import subprocess
import time
import psutil


def run_native(script_path):
    """
    Execute a Python script natively and measure runtime + CPU usage.
    """

    start_time = time.time()

    process = subprocess.Popen(
        ["python3", script_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    proc = psutil.Process(process.pid)

    cpu_samples = []

    while process.poll() is None:
        try:
            cpu_samples.append(proc.cpu_percent(interval=0.1))
        except psutil.NoSuchProcess:
            break

    end_time = time.time()

    stdout, stderr = process.communicate()

    runtime = end_time - start_time
    avg_cpu = sum(cpu_samples) / len(cpu_samples) if cpu_samples else 0

    return {
        "runtime": runtime,
        "avg_cpu": avg_cpu,
        "stdout": stdout.decode(),
        "stderr": stderr.decode()
    }
