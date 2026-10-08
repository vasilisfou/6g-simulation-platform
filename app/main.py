from fastapi import FastAPI
from simulator.simulation import run_simulation

app = FastAPI(title="6G Simulation Platform")


@app.get("/")
def root():
    return {"message": "6G Simulation Platform API"}


@app.get("/simulate")
def simulate(
    users: int = 100,
    duration: int = 60,
    traffic_rate: int = 10,
):
    return run_simulation(
        users=users,
        duration=duration,
        traffic_rate=traffic_rate,
    )