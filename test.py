import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
ico = Image.open('test.jpg')
ico.thumbnail((25,25))  # Replace with your image file
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.mainloop()