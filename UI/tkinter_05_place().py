#place layout manager: The place layout manager allows you to specify the exact position of a widget within its parent widget using x and y coordinates. It provides precise control over the placement of widgets, but it can be less flexible than pack or grid, especially when resizing the window.
import tkinter as tk


root = tk.Tk()

root.title("Layout managers")
root.geometry("300x200")
btn = tk.Button(root, text="Click Me")

""" place layout manager: 
The place layout manager allows you to specify the exact position of a widget within its parent widget using x and y coordinates. It provides precise control over the placement of widgets, 
but it can be less flexible than pack or grid, especially when resizing the window.
"""
btn.place(x=150, y=50, anchor="center", rely=0.5)  # Place the button at coordinates (150, 100) with the center as the anchor    


root.mainloop()