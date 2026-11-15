#there are 3 layout managers in tkinter: pack, grid, and place. Each layout manager has its own way of arranging widgets within a container. Here's a brief overview of each layout manager:
import tkinter as tk
import pywinstyles

root = tk.Tk()

root.title("layout managers")
root.geometry("300x200")
btn = tk.Button(root, text="Click Me")

""" pack layout manager: The pack layout manager arranges 
widgets in blocks before placing them in the parent 
widget. It is simple to use and works well for basic 
layouts. You can specify the side of the parent widget 
where the widget should be placed (top, bottom, left, right) and 
whether it should fill the available space (x, y, or both).

#  side="top“,”left”,” bottom”,”right”
# fill = “x”,”y”
# padx=5
# pady=5
 """
btn.pack(side="top", fill="x", padx=5, pady=5)
root.mainloop()