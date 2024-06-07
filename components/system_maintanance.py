from cgitb import text
from functools import wraps
from importlib.abc import ResourceReader
from re import X
import tkinter as tk
from tkinter import (
    CENTER,
    E,
    NO,
    RIGHT,
    W,
    Y,
    Button,
    Entry,
    Frame,
    Label,
    LabelFrame,
    Scrollbar,
    ttk,
)

from .main_frame import MainFrame


class SystemPage(MainFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        #main label
        main_label=Label(self,text="System Maintanance",font=("Arial",16,"bold"))
        main_label.pack(fill='x',expand=True)
