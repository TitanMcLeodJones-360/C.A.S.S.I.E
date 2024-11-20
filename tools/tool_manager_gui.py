import tkinter as tk
from tools.tool_manager import ToolManager

class ToolManagerGUI:
    def __init__(self, tool_manager):
        self.tool_manager = tool_manager

    def show_tool_manager(self):
        """
        Launches a GUI for managing connected devices.
        """
        window = tk.Toplevel()
        window.title("Tool Manager")
        window.geometry("800x600")
        window.configure(bg="black")

        label = tk.Label(window, text="Connected Devices", font=("Arial", 18, "bold"), fg="white", bg="black")
        label.pack(pady=10)

        devices_frame = tk.Frame(window, bg="black")
        devices_frame.pack(pady=10, padx=10)

        devices = self.tool_manager.devices
        if devices:
            for device_name, device_info in devices.items():
                frame = tk.Frame(devices_frame, bg="gray", padx=10, pady=5)
                frame.pack(fill=tk.X, pady=5)

                name_label = tk.Label(frame, text=device_name, font=("Arial", 14), bg="gray", fg="white")
                name_label.pack(side=tk.LEFT, padx=10)

                type_label = tk.Label(frame, text=f"({device_info['type']})", font=("Arial", 12), bg="gray", fg="white")
                type_label.pack(side=tk.LEFT, padx=5)

                status_label = tk.Label(frame, text=device_info["status"], font=("Arial", 12), bg="gray", fg="white")
                status_label.pack(side=tk.LEFT, padx=5)

                control_button = tk.Button(frame, text="Control", font=("Arial", 12), bg="white", fg="black",
                                           command=lambda d=device_name: self.control_device(d))
                control_button.pack(side=tk.RIGHT, padx=10)
        else:
            no_devices_label = tk.Label(devices_frame, text="No devices connected.", font=("Arial", 14), bg="black", fg="white")
            no_devices_label.pack()

        close_button = tk.Button(window, text="Close", font=("Arial", 14), bg="gray", fg="white", command=window.destroy)
        close_button.pack(pady=10)

    def control_device(self, device_name):
        """
        Opens a simple popup to simulate device control.
        """
        device_info = self.tool_manager.devices.get(device_name)
        if not device_info:
            return

        control_window = tk.Toplevel()
        control_window.title(f"Control {device_name}")
        control_window.geometry("400x200")
        control_window.configure(bg="black")

        label = tk.Label(control_window, text=f"Control {device_name}", font=("Arial", 16), fg="white", bg="black")
        label.pack(pady=10)

        action_button = tk.Button(control_window, text="Toggle On/Off", font=("Arial", 14), bg="gray", fg="white",
                                  command=lambda: self.tool_manager.control_device(device_name, "toggle"))
        action_button.pack(pady=10)

        close_button = tk.Button(control_window, text="Close", font=("Arial", 14), bg="gray", fg="white", command=control_window.destroy)
        close_button.pack(pady=10)
