import csv
import os

RESULT_FILE = "benchmarks/results.csv"


def log_result(environment, runtime):

    file_exists = os.path.isfile(RESULT_FILE)

    with open(RESULT_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["environment", "runtime"])

        writer.writerow([environment, runtime])
