# iot_dashboard

IoT Dashboard - Project Documentation

Overview

The IoT Dashboard is a web-based application built with Django that allows users to register IoT devices, send sensor data via MQTT, store it in a database, and visualize it in real time.

This system is designed to be simple, scalable, and efficient, making it suitable for applications like home automation, industrial monitoring, and environmental sensing.

Currently, the project supports basic features such as:

Registering IoT devices in the system.

Receiving sensor data from devices via MQTT.

Storing data in a Django database.

Providing API endpoints for device management and data retrieval.


As the project evolves, additional features like authentication, alerts, and advanced analytics can be added.


---

Key Features

Device Registration

Users can register IoT devices by providing a unique device ID. This allows the system to track and manage multiple devices efficiently.

Data Collection via MQTT

The dashboard listens for incoming sensor data over MQTT. Devices, such as ESP32, can publish messages containing sensor readings, which are then processed and stored.

Data Storage in Django Database

All received data is saved in a structured format using Django’s ORM, making it easy to query and retrieve historical readings.

Basic API for Data Retrieval

The system provides REST API endpoints to fetch stored sensor data for analysis and visualization.

Dashboard for Data Visualization (Upcoming Feature)

A web-based interface will be developed to display real-time charts and graphs, allowing users to monitor sensor data effortlessly.


---

Technology Stack


---

How the System Works

1. Device Sends Data

An ESP32 or any IoT device publishes a message to an MQTT topic, for example:

{
  "device_id": "esp32_001",
  "temperature": 25.5,
  "humidity": 60.2
}

This message is sent to the MQTT broker (Mosquitto).



2. MQTT Subscriber Processes Data

The Django application subscribes to the topic "iot/sensors" and listens for incoming messages.

When a message is received, it is parsed and saved in the database.



3. Data is Stored in Django

Each sensor reading is stored in a table with timestamps for later analysis.



4. API Provides Access to Data

Users can retrieve sensor data through REST API endpoints or use it for visualization in a web dashboard.





---

Project Structure

iot_dashboard/
│── devices/         # Handles IoT devices and sensor data
│   ├── migrations/  # Database migrations
│   ├── models.py    # Defines database tables
│   ├── views.py     # API endpoints
│   ├── urls.py      # URL routing for API
│   ├── mqtt_subscriber.py  # Listens for MQTT messages
│── templates/       # HTML templates for future UI
│── static/          # Static files (CSS, JavaScript)
│── db.sqlite3       # Default database
│── manage.py        # Django management script
│── requirements.txt # Dependencies


---

Setting Up the Project

1. Install Required Dependencies

Ensure Python and Django are installed, then install the required packages:

pip install -r requirements.txt

2. Set Up the Database

Run the following commands to create the database tables:

python manage.py makemigrations
python manage.py migrate

3. Start the MQTT Broker (Mosquitto)

If Mosquitto is installed, start the broker:

mosquitto

This allows devices to send messages to the system.

4. Run the Django Application

Start the Django server to handle API requests:

python manage.py runserver

This runs the application locally at http://127.0.0.1:8000/.


---

Using the API

Example using cURL to send data manually:

curl -X POST http://127.0.0.1:8000/api/sensors/ -H "Content-Type: application/json" \
-d '{"device_id": "esp32_001", "temperature": 25.5, "humidity": 60.2}'


---

Future Enhancements

1. Web Dashboard with Charts – A frontend interface to visualize sensor readings.


2. User Authentication – Secure access to registered devices and data.


3. Alert System – Notifications when sensor values exceed predefined limits.


4. AI-based Analysis – Predictive analytics using historical data.




---

Conclusion

This project provides a simple yet powerful foundation for managing IoT devices and processing real-time data. It can be expanded to support various applications, from smart homes to industrial monitoring.

Next steps include building the web dashboard, adding authentication, and improving data visualization.

