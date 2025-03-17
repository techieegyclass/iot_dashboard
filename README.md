# IoT Dashboard using Django and Mosquitto

## Overview

This project is a scalable IoT dashboard built using Django and Mosquitto MQTT. It allows users to register IoT devices, receive sensor data via MQTT, and visualize it in real time.

## Features

### Basic Features
- **User Authentication**: Register and log in to manage devices securely.
- **Device Registration**: Add IoT devices like ESP32, Raspberry Pi, etc.
- **MQTT Integration**: Receive sensor data via Mosquitto MQTT broker.
- **Data Storage**: Save device and sensor data in a database.
- **Real-time Visualization**: Display sensor readings in a web interface.

### Scalable Features (Future Enhancements)
- **Multi-User Support**: Each user manages their own devices.
- **Alert System**: Notify users of critical sensor values.
- **Historical Data Analysis**: View trends over time.
- **AI-based Analytics**: Use AI to detect anomalies in sensor data.

## Installation

### 1. Set Up Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Django
```sh
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
python manage.py runserver
```

### 3. Install and Configure Mosquitto
- Install Mosquitto MQTT broker
- Start the broker using:
  ```sh
  mosquitto -v
  ```
- Subscribe to a topic:
  ```sh
  mosquitto_sub -h localhost -t "iot/sensors"
  ```
- Publish a test message:
  ```sh
  mosquitto_pub -h localhost -t "iot/sensors" -m '{"device_id": "esp32_001", "temperature": 25.5, "humidity": 60.2}'
  ```

## API Endpoints

| Method | Endpoint         | Description               |
|--------|----------------|--------------------------|
| POST   | /api/devices/   | Register a new device    |
| GET    | /api/devices/   | List all registered devices |
| POST   | /api/data/      | Send sensor data         |
| GET    | /api/data/      | Retrieve stored sensor data |

## Running MQTT Subscriber in Django
To ensure Django listens for MQTT messages, run the MQTT subscriber script:
```sh
python manage.py runmqtt
```

## Contributing
Feel free to submit pull requests or open issues to improve the project.

## License
This project is open-source and free to use.
