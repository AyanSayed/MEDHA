# MediPi Hackathon Starter

## Setup on the Raspberry Pi

```bash
git clone <your-repo-url>
cd medipi-hackathon
pip3 install -r requirements.txt --break-system-packages
python3 app.py
```

Then open `http://<pi-ip-address>:5000` in a browser (find the Pi's IP with `hostname -I`).

## How this is structured

- `app.py` — Flask server. Runs a background thread that polls the sensor every second and serves the latest reading as JSON at `/api/data`.
- `sensors/mock_sensor.py` — fake data generator. Currently wired into `app.py` so you can build/test the whole app before your real sensor arrives or before the problem statement drops.
- `sensors/gpio_example.py` — template for reading a real GPIO-connected sensor once you know which one you're using.
- `templates/index.html` — simple live dashboard, auto-refreshes every second.

## Swapping in your real sensor

1. Create a new file in `sensors/`, e.g. `sensors/heart_rate.py`
2. Write a `read_sensor_data()` function in it that returns your real reading
3. In `app.py`, change:
   ```python
   from sensors.mock_sensor import read_sensor_data
   ```
   to:
   ```python
   from sensors.heart_rate import read_sensor_data
   ```
4. Restart `python3 app.py` — dashboard now shows real data, no other changes needed.
