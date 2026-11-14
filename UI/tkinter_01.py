import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Tkinter Test")
root.geometry("300x200")

# Disable window resizing
root.resizable(width=False, height=False)

# Load window icon
icon = ImageTk.PhotoImage(
    Image.open(r"C:\Users\user\Desktop\python SLIPD\UI\src\images.jfif")
)

root.iconphoto(False, icon)

# Set background colour
root.configure(bg="#f0f0f0")

root.mainloop()