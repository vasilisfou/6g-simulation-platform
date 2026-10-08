from simulator.simulation import run_simulation


def test_simulation_returns_results():
    result = run_simulation(
        users=100,
        duration=60,
        traffic_rate=10,
    )

    assert result["users"] == 100
    assert result["duration"] == 60
    assert result["traffic_rate"] == 10


def test_total_packets():
    result = run_simulation(
        users=10,
        duration=10,
        traffic_rate=5,
    )

    assert result["total_packets"] == 500