import subprocess
import time


VM_NAME = "ubuntu24.04"
VM_USER = "ryuk"
VM_IP = "192.168.122.40"


def run_kvm(script_path):

    print("Starting VM...")

    subprocess.run(["virsh", "start", VM_NAME], stdout=subprocess.DEVNULL)

    time.sleep(20)

    print("Executing workload inside VM...")

    start_time = time.time()

    ssh_command = [
        "ssh",
        f"{VM_USER}@{VM_IP}",
        f"python3 {script_path}"
    ]

    process = subprocess.run(
        ssh_command,
        capture_output=True,
        text=True
    )

    end_time = time.time()

    runtime = end_time - start_time

    print("Shutting down VM...")

    subprocess.run(["virsh", "shutdown", VM_NAME], stdout=subprocess.DEVNULL)

    return {
        "runtime": runtime,
        "stdout": process.stdout,
        "stderr": process.stderr
    }
