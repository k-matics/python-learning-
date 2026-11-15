import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Menu Example")
root.geometry("400x300")

# Create the menu bar at the top of the window
menu_bar = tk.Menu(root)``

# Create the File menu and add menu items
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_command(label="Save", command=lambda: print("Save File"))
file_menu.add_separator()  # Add a divider line
file_menu.add_command(label="Exit", command=root.quit)

# Attach the File menu to the main menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Create the Edit menu and add menu items
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="cut", command=lambda: print("cut"))
edit_menu.add_command(label="paste", command=lambda: print("paste"))

# Attach the Edit menu to the main menu bar
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Display the menu bar in the root window
root.config(menu=menu_bar)

# Run the application window
root.mainloop()