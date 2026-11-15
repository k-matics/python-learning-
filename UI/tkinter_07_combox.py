#combox in a dropdown menu: A combobox is a widget that combines a text entry field with a dropdown list of options. It allows users to select an option from the list or enter their own value. Comboboxes are commonly used for selecting from a predefined set of choices.
import tkinter as tk            
from tkinter import ttk


# Create the main window
root = tk.Tk()
root.title("Combobox")
root.geometry("300x200")

# Add items to the Combobox 
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

# Create and display the Combobox
choice = ttk.Combobox(root, values= items)
choice.set("Select an item")  # Set the default value
choice.pack(padx=5, pady=5 )

# Function to get selected items
def myfunction():
    selected_item = choice.get()
    print(selected_item)

# Create a button to get selected items
btn = tk.Button(root, text="Get Selected", command=myfunction)
btn.pack()

# Run the application
root.mainloop()