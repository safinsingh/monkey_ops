import docker


def running_container_stats():
    ret = {}
    client = docker.from_env()
    containers = client.containers.list()

    for container in containers:
        stats = container.stats(stream=False)

        uid = container.id

        container_cpu_usage = stats["cpu_stats"]["cpu_usage"]["total_usage"]
        system_cpu_usage = stats["cpu_stats"]["system_cpu_usage"]
        online_cpus = stats["cpu_stats"]["online_cpus"]
        cpu_percentage = (container_cpu_usage / (system_cpu_usage * online_cpus)) * 100
        mem_usage = stats["memory_stats"]["usage"]

        ret[uid] = {"cpu_percentage": cpu_percentage, "mem_usage": mem_usage}

    return ret
