import subprocess
import time
import os


VM_NAME = "ubuntu24.04"
VM_USER = "ryuk"
VM_IP = "192.168.122.40"

REMOTE_DIR = "~/iravs"


def vm_running():

    state = subprocess.run(
        ["virsh", "domstate", VM_NAME],
        capture_output=True,
        text=True
    )

    return "running" in state.stdout


def run_kvm(script_path):

    filename = os.path.basename(script_path)

    if not vm_running():
        subprocess.run(["virsh", "start", VM_NAME])
        time.sleep(15)

    subprocess.run([
        "ssh",
        f"{VM_USER}@{VM_IP}",
        f"mkdir -p {REMOTE_DIR}"
    ])

    subprocess.run([
        "scp",
        script_path,
        f"{VM_USER}@{VM_IP}:{REMOTE_DIR}/{filename}"
    ])

    start_time = time.time()

    process = subprocess.run(
        [
            "ssh",
            f"{VM_USER}@{VM_IP}",
            f"python3 {REMOTE_DIR}/{filename}"
        ],
        capture_output=True,
        text=True
    )

    end_time = time.time()

    runtime = end_time - start_time

    subprocess.run(["virsh", "shutdown", VM_NAME])

    return {
        "runtime": runtime,
        "stdout": process.stdout,
        "stderr": process.stderr
    }
