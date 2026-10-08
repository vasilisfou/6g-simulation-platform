from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "6G Simulation Platform API"
    }


def test_simulate():
    response = client.get(
        "/simulate",
        params={
            "users": 100,
            "duration": 60,
            "traffic_rate": 10,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["users"] == 100
    assert data["duration"] == 60
    assert data["traffic_rate"] == 10
    assert "latency_ms" in data
    assert "packet_loss" in data
    assert "throughput" in data
    assert "energy" in data