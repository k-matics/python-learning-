#sub window 
import tkinter as tk
import pywinstyles

root = tk.Tk()

root.title("Tkinter Test")
root.geometry("300x200")

# Disable window resizing
root.resizable(width=False, height=False)

#functon to open subwindow
def open_subwindow():
    subwindow = tk.Toplevel(root)
    subwindow.title("Subwindow")
    subwindow.geometry("200x100")
    lbl_sub = tk.Label(subwindow, text="This is a subwindow")
    lbl_sub.pack()
    lbl_sub2 = tk.Label(subwindow, text="You can add more widgets here")
    lbl_sub2.pack()
    
#button to open subwindow
btn_open_subwindow = tk.Button(root, text="Open Subwindow", command=lambda: open_subwindow()).pack()


# Set background colour
root.configure(bg="#bd2020")
pywinstyles.apply_style(root, "dark")

root.mainloop()