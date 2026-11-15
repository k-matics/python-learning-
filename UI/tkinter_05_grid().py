#grid layout manager: The grid layout manager arranges widgets in a table-like structure, where you can specify the row and column for each widget. It is more flexible than pack and allows for more complex layouts. You can also specify the rowspan and columnspan to make a widget span multiple rows or columns.
import tkinter as tk
import pywinstyles

root = tk.Tk()

root.title("Tkinter Test")
root.geometry("300x200")

# Disable window resizing
root.resizable(width=False, height=False)


#login items
lbl_email =tk.Label(root, text="Email:")
lbl_psswd =tk.Label(root, text="Password:")

#adding entry fields
ent_email = tk.Entry(root)
ent_psswd = tk.Entry(root, show="*")


#add login button


#login function
def login():
    email = str(ent_email.get())
    password = str(ent_psswd.get())
    if email =="admin" and password == "admin":
        print("Login successful")
    else:
        print("Login failed")


btn_login = tk.Button(root, text="Login", command=login)

""" grid layout manager: The grid layout manager arranges widgets in a table-like structure, where you can specify the row and column for each widget. 
It is more flexible than pack and allows for more complex layouts. You can also specify the rowspan and columnspan to make a widget span multiple rows or columns. """
lbl_email.grid(row=0, column=0, padx=5, pady=5)
ent_email.grid(row=0, column=1, padx=5, pady=5)
lbl_psswd.grid(row=1, column=0, padx=5, pady=5)
ent_psswd.grid(row=1, column=1, padx=5, pady=5)
btn_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Set background colour
root.configure(bg="#bd2020")
pywinstyles.apply_style(root, "dark")

root.mainloop()