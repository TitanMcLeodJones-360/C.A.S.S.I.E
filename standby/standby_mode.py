from standby.standby_mode import StandbyMode

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("C.A.S.S.I.E Dashboard")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        # Modules
        self.standby_mode = StandbyMode(inactivity_threshold=300)

    def create_dashboard(self):
        # Logo
        logo_label = tk.Label(self.root, text="C.A.S.S.I.E", font=("Arial", 24, "bold"), fg="white", bg="black")
        logo_label.pack(pady=20)

        # Buttons
        buttons_frame = tk.Frame(self.root, bg="black")
        buttons_frame.pack(pady=10)

        button_labels = [
            "Logs/Documents",
            "Storage Systems",
            "System Diagnostics",
            "Hardware Controls",
            "Settings",
            "Browser",
            "Notifications",
            "Toggle Standby"
        ]
        for label in button_labels:
            btn = tk.Button(
                buttons_frame,
                text=label,
                font=("Arial", 14),
                bg="gray",
                fg="white",
                width=20,
                height=2,
                command=lambda l=label: self.handle_button_click(l)
            )
            btn.pack(pady=5)

    def handle_button_click(self, label):
        if label == "Toggle Standby":
            self.standby_mode.toggle_standby()
        else:
            messagebox.showinfo("Button Clicked", f"You clicked: {label}")

    def launch(self):
        self.standby_mode.start_monitoring(parent_gui=self.root)
        self.create_dashboard()
        self.root.mainloop()
