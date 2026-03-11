import requests

for _ in range(20):
    requests.get("https://example.com")

print("Network workload finished")
