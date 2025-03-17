import paho.mqtt.client as mqtt
import json
import os
import django

# Ensure Django settings are configured **only if running outside Django**
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iot_dashboard.settings')
    django.setup()  # Initialize Django once

def on_message(client, userdata, msg):
    from devices.models import Device, SensorData  # Import inside function
    payload = json.loads(msg.payload.decode())

    device_id = payload.get("device_id")
    temperature = payload.get("temperature")
    humidity = payload.get("humidity")

    if device_id and temperature is not None and humidity is not None:
        device, _ = Device.objects.get_or_create(device_id=device_id)
        SensorData.objects.create(device=device, temperature=temperature, humidity=humidity)
        print(f"Saved data from {device_id}: Temp={temperature}, Hum={humidity}")

def start_mqtt():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("localhost", 1883, 60)
    client.subscribe("iot/sensors")
    client.loop_start()
