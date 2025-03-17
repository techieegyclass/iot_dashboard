# iot_dashboard

Sure! Below is the README.md file in a GitHub-friendly format with proper Markdown formatting.


---

IoT Dashboard

Overview

The IoT Dashboard is a web-based application built with Django that allows users to:

Register IoT devices

Receive sensor data via MQTT (Mosquitto Broker)

Store data in a Django database

Provide API endpoints for data retrieval


This project is designed to be scalable and can be expanded to include authentication, alerts, and AI-based analytics.


---

Features

✅ Register IoT devices in the system
✅ Receive and store sensor data from devices via MQTT
✅ Provide REST API endpoints for data retrieval
✅ Use Django’s ORM for structured data storage
✅ (Upcoming) Web-based dashboard for data visualization


---

Technology Stack


---

How It Works

1. Device Sends Data

An ESP32 (or other IoT device) publishes a message to the MQTT broker.

Example payload:

{
  "device_id": "esp32_001",
  "temperature": 25.5,
  "humidity": 60.2
}

The message is sent to the MQTT topic "iot/sensors".



2. Django MQTT Subscriber Processes Data

The Django backend subscribes to the topic "iot/sensors".

It listens for incoming sensor data and stores it in the database.



3. Data is Stored in the Django Database

Each sensor reading is saved with a timestamp.



4. API Provides Access to Data

Users can fetch stored sensor data through REST API endpoints.





---

Project Structure

iot_dashboard/
│── devices/         # Handles IoT devices and sensor data
│   ├── migrations/  # Database migrations
│   ├── models.py    # Database models
│   ├── views.py     # API endpoints
│   ├── urls.py      # API routing
│   ├── mqtt_subscriber.py  # MQTT listener
│── templates/       # HTML templates (future UI)
│── static/          # Static files (CSS, JS)
│── db.sqlite3       # Default database
│── manage.py        # Django management script
│── requirements.txt # Dependencies


---

Installation & Setup

1. Clone the Repository

git clone https://github.com/yourusername/iot_dashboard.git
cd iot_dashboard

2. Install Dependencies

Ensure you have Python installed, then run:

pip install -r requirements.txt

3. Set Up the Database

python manage.py makemigrations
python manage.py migrate

4. Start the MQTT Broker (Mosquitto)

If you have Mosquitto installed, run:

mosquitto

5. Start the Django Server

python manage.py runserver

The application will run at:
http://127.0.0.1:8000/


---

API Usage

Register a Device

curl -X POST http://127.0.0.1:8000/api/devices/ -H "Content-Type: application/json" \
-d '{"device_id": "esp32_001"}'

Send Sensor Data

curl -X POST http://127.0.0.1:8000/api/sensors/ -H "Content-Type: application/json" \
-d '{"device_id": "esp32_001", "temperature": 25.5, "humidity": 60.2}'

Retrieve Sensor Data

curl -X GET "http://127.0.0.1:8000/api/sensors/?device_id=esp32_001"


---

Future Enhancements

Web Dashboard with real-time charts
User Authentication for secure access
Alert System for abnormal sensor values
AI-based analytics for predictive insights


---

Contributing

If you’d like to contribute:

1. Fork the repository


2. Create a new branch (git checkout -b feature-branch)


3. Commit your changes (git commit -m "Added new feature")


4. Push to your fork (git push origin feature-branch)


5. Create a Pull Request




---

License

This project is licensed under the MIT License. Feel free to modify and use it for your needs.


---
