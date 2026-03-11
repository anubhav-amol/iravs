import subprocess
import time


def measure_native_startup():

    start = time.time()

    subprocess.run(
        ["python3", "-c", "print(1)"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return time.time() - start


def measure_docker_startup():

    start = time.time()

    subprocess.run(
        ["docker", "run", "--rm", "ubuntu:24.04", "echo", "hello"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return time.time() - start


def measure_kvm_startup(vm_name="ubuntu24.04"):

    start = time.time()

    subprocess.run(
        ["virsh", "start", vm_name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(5)

    subprocess.run(
        ["virsh", "shutdown", vm_name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return time.time() - start
