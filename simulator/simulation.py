import random


def run_simulation(users, duration, traffic_rate):
    total_packets = users * duration * traffic_rate
    packet_loss = random.uniform(0.01, 0.05)
    latency = random.uniform(10, 50)
    throughput = traffic_rate * users * (1 - packet_loss)
    energy = users * duration * random.uniform(0.01, 0.03)

    return {
        "users": users,
        "duration": duration,
        "traffic_rate": traffic_rate,
        "total_packets": total_packets,
        "latency_ms": round(latency, 2),
        "packet_loss": round(packet_loss, 4),
        "throughput": round(throughput, 2),
        "energy": round(energy, 2),
    }