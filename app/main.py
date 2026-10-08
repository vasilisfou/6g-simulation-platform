from fastapi import FastAPI
from simulator.simulation import run_simulation
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="6G Simulation Platform")
Instrumentator().instrument(app).expose(app)


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