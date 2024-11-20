import tkinter as tk
from tkinter import scrolledtext
import os

class LogViewer:
    def __init__(self, log_file="logs/cassie.log"):
        self.log_file = log_file
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    def show_logs(self):
        """
        Launches a GUI to display the logs.
        """
        window = tk.Toplevel()
        window.title("C.A.S.S.I.E Logs")
        window.geometry("800x600")
        window.configure(bg="black")

        label = tk.Label(window, text="System Logs", font=("Arial", 18, "bold"), fg="white", bg="black")
        label.pack(pady=10)

        log_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=30, bg="gray", fg="white", font=("Arial", 12))
        log_text.pack(pady=10, padx=10)

        try:
            with open(self.log_file, "r") as log_file:
                logs = log_file.read()
                log_text.insert(tk.END, logs)
        except FileNotFoundError:
            log_text.insert(tk.END, "No logs available.")
        
        log_text.config(state=tk.DISABLED)

        close_button = tk.Button(window, text="Close", font=("Arial", 14), bg="gray", fg="white", command=window.destroy)
        close_button.pack(pady=10)
