""" widget for creating graphics, drawings, and other visual 
representations. It allows for drawing shapes, lines &images. """

import tkinter as tk
root = tk.Tk()
root.title("Drawing Shapes")
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()
# Draw a line
canvas.create_line(50, 50, 200, 50, fill="blue", width=3)
# Draw a rectangle
canvas.create_rectangle(50, 100, 200, 150, fill="green", outline="black")
# Draw an oval (circle or ellipse)
canvas.create_oval(250, 50, 350, 150, fill="red", outline="black")
# Draw a polygon
canvas.create_polygon(100, 200, 200, 250, 150, 300, fill="yellow", 
outline="black")
# Add text
canvas.create_text(200, 50, text="Hello, Canvas!", font=("Arial", 16), fill="purple")
root.mainloop()
