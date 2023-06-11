import tkinter as tk
from phpvms_acars.gui.login_window import LoginWindow
from phpvms_acars.gui.main_window import MainWindow
from phpvms_acars.api_handler import ApiHandler

class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Window")
        self.root.geometry("300x200")
        self.root.iconify()

        self.main_window = MainWindow(self.root)
        self.main_window.pack()

        login_window = tk.Toplevel(self.root)
        login_window.title("Login")
        login_window.geometry("300x150")

        login_frame = LoginWindow(login_window, self.login_successful)
        login_frame.pack()

    def login_successful(self, api_handler):
        self.main_window.api_handler = api_handler
        self.main_window.update()
        self.root.deiconify()

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app_controller = AppController()
    app_controller.start()

