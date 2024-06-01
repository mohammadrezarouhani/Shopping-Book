
import tkinter as tk
from tkinter import ttk

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = ttk.Label(self, text="This is the Start Page")
        label.grid(row=0, column=0, padx=10, pady=30)
        
        button1 = ttk.Button(self, text="Go to Page One",
                             command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=1, column=0, padx=10, pady=10)
        
        button2 = ttk.Button(self, text="Go to Page Two",
                             command=lambda: controller.show_frame("PageTwo"))
        button2.grid(row=2, column=0, padx=10, pady=10)