import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview Table")
root.geometry("400x300")

# Create the table
tbl = ttk.Treeview(root, columns=("Name", "Age"), show="headings")

# Set column headings
tbl.heading("Name", text="Name")
tbl.heading("Age", text="Age")

# Set column widths
tbl.column("Name", width=150)
tbl.column("Age", width=100)

# Add data
tbl.insert("", tk.END, values=("John", 25))
tbl.insert("", tk.END, values=("Peter", 30))
tbl.insert("", tk.END, values=("Sarah", 22))

# Display the table
tbl.pack(fill="both", expand=True)

root.mainloop()