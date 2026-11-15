"""Container widget used to group and organize other widgets.
Frames are especially useful for creating multiple sections or screens in an application."""

import tkinter as tk

root = tk.Tk()
root.title("Switch Frames Without Classes")
root.geometry("400x300")


# Create a function to switch between frames
def show_frame(frame):
    """Bring the specified frame to the front."""
    frame.tkraise()


# Create Frame1
frame1 = tk.Frame(root, bg="lightblue")
frame1.place(relwidth=1, relheight=1)

# Add widgets to Frame1
tk.Label(frame1, text="This is Frame 1", font=("Arial", 18), bg="lightblue").pack(pady=20)
tk.Button(frame1, text="Go to Frame 2", command=lambda: show_frame(frame2)).pack()


# Create Frame2
frame2 = tk.Frame(root, bg="lightgreen")
frame2.place(relwidth=1, relheight=1)

# Add widgets to Frame2
tk.Label(frame2, text="This is Frame 2", font=("Arial", 18), bg="lightgreen").pack(pady=20)
tk.Button(frame2, text="Back to Frame 1", command=lambda: show_frame(frame1)).pack()


# Set the initial frame
frame1.tkraise()

# Start the application
root.mainloop()