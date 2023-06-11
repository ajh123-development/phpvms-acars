import tkinter as tk
from tkinter import messagebox
from ..api_handler import ApiHandler


class LoginWindow(tk.Frame):
    def __init__(self, parent: tk.Toplevel, login_callback: callable):
        super().__init__(parent)
        self.parent = parent
        self.login_callback = login_callback

        self.label = tk.Label(self, text="Enter phpVMS URL:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.label2 = tk.Label(self, text="Enter API Key:")
        self.label2.pack()

        self.entry2 = tk.Entry(self, show="*")
        self.entry2.pack()

        self.button = tk.Button(self, text="Login", command=self.login)
        self.button.pack()

    def login(self):
        api_key: str = self.entry2.get()
        base_url: str = self.entry.get()

        try:
            api_handler: ApiHandler = ApiHandler(api_key, base_url)
            api_handler.fetch_pilot_user()
            self.login_callback(api_handler)
            self.parent.destroy()
        except Exception as e:
            messagebox.showerror("Login Failed", str(e))
            self.entry.delete(0, tk.END)
            self.entry.focus_set()
