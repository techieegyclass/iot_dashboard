from django.apps import AppConfig
import threading
from .mqtt_subscriber import start_mqtt

class DevicesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "devices"

    def ready(self):
        mqtt_thread = threading.Thread(target=start_mqtt, daemon=True)
        mqtt_thread.start()

