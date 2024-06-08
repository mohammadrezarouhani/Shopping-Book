from re import X
import tkinter as tk
from tkinter import (
    Label,
)

from .main_frame import MainFrame


class ReportPage(MainFrame):
    def init(self):
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        #main label
        main_label=Label(self,text="Report Page",font=("Arial",16,"bold"))
        main_label.pack(fill='x',expand=True)
