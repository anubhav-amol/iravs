import os

data = "A" * 1024 * 1024

with open("tempfile.dat", "w") as f:
    for _ in range(100):
        f.write(data)

os.remove("tempfile.dat")

print("Disk workload finished")
