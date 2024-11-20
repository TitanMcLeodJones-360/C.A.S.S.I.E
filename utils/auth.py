from tkinter import Tk, Label, Entry, Button

class Auth:
    def authenticate_user(self):
        """
        Displays a GUI login screen and validates user credentials.
        """
        self.authenticated = False
        self.root = Tk()
        self.root.title("C.A.S.S.I.E Login")
        self.root.geometry("400x300")
        self.root.configure(bg="black")

        # UI Elements
        Label(self.root, text="C.A.S.S.I.E Login", fg="white", bg="black", font=("Arial", 16)).pack(pady=20)
        self.username_entry = Entry(self.root, fg="white", bg="gray", font=("Arial", 12))
        self.username_entry.pack(pady=5)
        self.password_entry = Entry(self.root, show="*", fg="white", bg="gray", font=("Arial", 12))
        self.password_entry.pack(pady=5)
        Button(self.root, text="Login", command=self.validate_login).pack(pady=20)

        # Start the GUI event loop
        self.root.mainloop()
        return self.authenticated

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":  # Example credentials
            self.authenticated = True
            self.root.destroy()
        else:
            self.authenticated = False
            self.root.destroy()
