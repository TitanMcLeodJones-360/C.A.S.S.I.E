import logging

class ToolManager:
    def __init__(self):
        self.devices = {}  # Store devices in a dictionary with their properties

    def add_device(self, device_type, device_name, ip_address):
        """
        Adds a new device to the system.
        :param device_type: Type of the device (e.g., camera, smartplug, thermostat).
        :param device_name: User-friendly name for the device.
        :param ip_address: Device's IP address.
        """
        self.devices[device_name] = {
            "type": device_type,
            "ip_address": ip_address,
            "status": "connected"
        }
        logging.info(f"Device added: {device_name} ({device_type}) at {ip_address}")

    def control_device(self, device_name, action, value=None):
        """
        Controls a connected device.
        :param device_name: Name of the device to control.
        :param action: Action to perform (e.g., 'on', 'off', 'set temperature').
        :param value: Optional value for the action (e.g., temperature).
        """
        if device_name not in self.devices:
            logging.error(f"Device not found: {device_name}")
            return f"Device {device_name} not found."

        device = self.devices[device_name]
        device_type = device["type"]

        if device_type == "camera" and action == "view":
            logging.info(f"Viewing footage from {device_name}")
            return f"Viewing footage from {device_name}"
        elif device_type == "smartplug" and action in ["on", "off"]:
            logging.info(f"Turning {device_name} {action}")
            return f"Smartplug {device_name} turned {action}"
        elif device_type == "thermostat" and action == "set temperature":
            if value is not None:
                logging.info(f"Setting {device_name} to {value}°C")
                return f"Thermostat {device_name} set to {value}°C"
            else:
                logging.error("Temperature value not provided for thermostat.")
                return "Temperature value not provided."
        else:
            logging.warning(f"Action {action} not supported for device type {device_type}")
            return f"Action {action} not supported for device type {device_type}"

    def remove_device(self, device_name
