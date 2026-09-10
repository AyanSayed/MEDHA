"""
Mock sensor - generates fake but realistic-looking data.
Use this to build/test your whole app BEFORE you know your real sensor.

Once you know the real sensor (e.g. MAX30102 for heart rate, DHT22 for temp),
replace read_sensor_data() with real hardware reading code, and swap the
import in app.py from mock_sensor to your real sensor file.
"""

import random


def read_sensor_data():
    """
    Returns a fake reading, e.g. simulating heart rate (BPM).
    Replace this with real sensor code later - e.g.:

        import board, busio
        from adafruit_mlx90614 import MLX90614
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = MLX90614(i2c)
        return sensor.object_temperature
    """
    return round(random.uniform(60, 100), 1)  # fake BPM between 60-100
