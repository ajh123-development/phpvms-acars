import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
from ..api_handler import ApiHandler

class MainWindow(tk.Frame):
    def __init__(self, parent: tk.Tk):
        super().__init__(parent)
        self.parent = parent
        self.user = None
        self.api_handler: ApiHandler = None

        self.menu_bar = Menu(self.parent)
        self.parent.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.parent.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.details_label = tk.Label(self, text="Pilot Name: ")
        self.details_label.pack()
        self.airlineDetails_label = tk.Label(self, text="Airline: ")
        self.airlineDetails_label.pack()

        self.update()

    def update(self):
        super().update()  # Call the update method from the tk.Frame superclass

        if self.api_handler is not None:
            try:
                self.user = self.api_handler.fetch_pilot_user()
                self.details_label.configure(text=f"Pilot Name: {self.user.name}")
                self.airlineDetails_label.configure(text=f"Airline: {self.user.airline.name}")

                print(self.api_handler.fetch_pireps())
            except Exception as e:
                messagebox.showerror("Error", str(e))
