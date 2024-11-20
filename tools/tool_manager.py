import logging
from web.notifications_communications import Notifications

class ToolManager:
    def __init__(self):
        self.devices = {}  # Store devices with their properties
        self.notifications = Notifications()

    def add_device(self, device_type, device_name, ip_address):
        """
        Adds a new device to the system.
        :param device_type: Type of the device (e.g., camera, smartplug, thermostat).
        :param device_name: User-friendly name for the device.
        :param ip_address: Device's IP address.
        """
        if device_name in self.devices:
            logging.warning(f"Device {device_name} already exists.")
            self.notifications.add_notification(f"Device {device_name} already exists.", "warning")
            return

        self.devices[device_name] = {
            "type": device_type,
            "ip_address": ip_address,
            "status": "connected"
        }
        logging.info(f"Device added: {device_name} ({device_type}) at {ip_address}")
        self.notifications.add_notification(f"Device added: {device_name} ({device_type}).", "info")

    def remove_device(self, device_name):
        """
        Removes a device from the system.
        :param device_name: Name of the device to remove.
        """
        if device_name in self.devices:
            del self.devices[device_name]
            logging.info(f"Device removed: {device_name}")
            self.notifications.add_notification(f"Device {device_name} removed.", "info")
        else:
            logging.error(f"Device {device_name} not found.")
            self.notifications.add_notification(f"Device {device_name} not found.", "error")

    def control_device(self, device_name, action, value=None):
        """
        Controls a connected device.
        :param device_name: Name of the device to control.
        :param action: Action to perform (e.g., 'on', 'off', 'set temperature').
        :param value: Optional value for the action (e.g., temperature).
        """
        if device_name not in self.devices:
            logging.error(f"Device {device_name} not found.")
            self.notifications.add_notification(f"Device {device_name} not found.", "error")
            return

        device = self.devices[device_name]
        device_type = device["type"]

        if device_type == "camera" and action == "view":
            logging.info(f"Viewing footage from {device_name}")
            self.notifications.add_notification(f"Viewing footage from {device_name}.", "info")
            # Implement live camera footage viewing here
        elif device_type == "smartplug" and action in ["on", "off"]:
            logging.info(f"Turning {device_name} {action}")
            self.notifications.add_notification(f"Smartplug {device_name} turned {action}.", "info")
        elif device_type == "thermostat" and action == "set temperature":
            if value is not None:
                logging.info(f"Setting {device_name} to {value}°C")
                self.notifications.add_notification(f"Thermostat {device_name} set to {value}°C.", "info")
            else:
                logging.error("Temperature value not provided for thermostat.")
                self.notifications.add_notification("Temperature value not provided.", "error")
        else:
            logging.warning(f"Action {action} not supported for device type {device_type}")
            self.notifications.add_notification(f"Action {action} not supported for device type {device_type}.", "warning")

    def list_devices(self):
        """
        Lists all connected devices.
        """
        if not self.devices:
            logging.info("No devices connected.")
            self.notifications.add_notification("No devices connected.", "info")
            return "No devices connected."

        device_list = "\n".join([
            f"{name} ({info['type']}) - {info['status']}" for name, info in self.devices.items()
        ])
        logging.info("Connected devices:\n" + device_list)
        self.notifications.add_notification("Device list retrieved.", "info")
        return device_list
