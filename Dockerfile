FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY simulator ./simulator

CMD ["python", "-c", "from simulator.simulation import run_simulation; print(run_simulation(100, 60, 10))"]