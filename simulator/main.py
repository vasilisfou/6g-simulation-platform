from simulator.simulation import run_simulation


def main():
    result = run_simulation(
        users=100,
        duration=60,
        traffic_rate=10,
    )

    print(result)


if __name__ == "__main__":
    main()