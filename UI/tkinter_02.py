#login form 
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

#adding items to the window
lbl_email.pack()
ent_email.pack()    
lbl_psswd.pack()
ent_psswd.pack()
btn_login.pack()

# Set background colour
root.configure(bg="#bd2020")
pywinstyles.apply_style(root, "dark")

root.mainloop()