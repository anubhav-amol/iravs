def choose_environment(scores):

    cpu = scores["cpu"]
    disk = scores["disk"]
    network = scores["network"]

    if cpu >= disk and cpu >= network:
        return "native"

    elif disk >= cpu and disk >= network:
        return "docker"

    else:
        return "kvm"
