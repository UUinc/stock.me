from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.label = ttk.Label(self, text="DASHBOARD")
        self.label.pack(padx=10, pady=10)

        from src.pages.settings_page import SettingsPage
        self.btn = ttk.Button(self, text="Go to SETTINGS", command=lambda: controller.show_page(SettingsPage))
        self.btn.pack(padx=10, pady=10)

        self.controller = controller
