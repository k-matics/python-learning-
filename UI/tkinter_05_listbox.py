import tkinter as tk

# Create the main window
root = tk.Tk()

root.title("List box")
root.geometry("300x200")

# Create and display the Listbox
choice = tk.Listbox(root, selectmode="multiple")
choice.pack(padx=5, pady=5, fill="both", expand=True)

# Add items to the Listbox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

for item in items:
    choice.insert(tk.END, item)

# Function to get selected items
def myfunction():
    selected_items = choice.curselection()

    for index in selected_items:
        print(choice.get(index))

# Create a button to get selected items
btn = tk.Button(root, text="Get Selected", command=myfunction)
btn.pack()

# Run the application
root.mainloop()
