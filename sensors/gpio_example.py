"""
Example: how to read a simple GPIO sensor (e.g. a button, IR sensor, or
digital output pulse sensor) once you know your hardware.

This is a TEMPLATE - pin numbers and logic will change based on your
actual sensor's datasheet.
"""

from gpiozero import DigitalInputDevice
import time

# Example: sensor connected to GPIO pin 17
SENSOR_PIN = 17
sensor = DigitalInputDevice(SENSOR_PIN)


def read_sensor_data():
    """Returns 1 if sensor triggered, 0 otherwise. Adjust for your sensor's behavior."""
    return sensor.value


if __name__ == "__main__":
    # quick standalone test - run this file directly to check wiring works
    print("Reading GPIO pin", SENSOR_PIN, "- Ctrl+C to stop")
    try:
        while True:
            print("Value:", read_sensor_data())
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Stopped.")
