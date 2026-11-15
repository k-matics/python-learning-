import tkinter as tk
from tkinter import messagebox

# Show an information message when the Info button is clicked
def show_info():
 messagebox.showinfo("Info", "This is a MessageBox!")

# Show an error message when the Error button is clicked
def show_error():
 messagebox.showerror("Error", "This is an error message.")

# Create and configure the main window
root = tk.Tk()
root.geometry("400x300")
root.title("Message Box Example")

# Create buttons and connect them to their message-box functions
button_info = tk.Button(root, text="Show info", 
command=show_info)
button_error = tk.Button(root, text="Show Error", 
command=show_error)

### Example: ask the user a Yes/No question
# response = messagebox.askyesno("Confirmation", "Do you want to proceed?") 
# if response:
#    print("User chose Yes") 
# else: 
#    print("User chose No")


### Example: ask the user whether to save, discard, or cancel
# response = messagebox.askyesnocancel("Confirmation", "Do you want to save changes?")
# if response is True:
#   print("User chose Yes")
# elif response is False:
#   print("User chose No")
# else:
#   print("User canceled")


###Example: ask the user to confirm an action
# response = messagebox.askokcancel("Confirm Action", "Do you want to delete this file?")
# if response:
#  print("User clicked OK")
# else:
#  print("User clicked Cancel")


###Example: offer the user a chance to retry an operation
# response = messagebox.askretrycancel("Retry", "An error occurred. Do you want to try again?")
# if response:
#  print("User clicked Retry")
# else:
#  print("User clicked Cancel")

# Add the buttons to the window
button_info.pack()
button_error.pack()

# Start the Tkinter event loop
root.mainloop()