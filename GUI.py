import tkinter as tk
from tkinter import messagebox
import os

def run_add_faces():
    """Runs the add_faces.py script with the entered name as an argument."""
    name = name_entry.get().strip()
    if name:
        os.system(f"python add_faces.py {name}")
    else:
        messagebox.showwarning("Input Error", "Please enter a name before proceeding.")

def run_take_attendance():
    """Runs the test.py script."""
    os.system("python test.py")

# Create main application window
root = tk.Tk()
root.title("Attendance System")
root.geometry("400x300")
root.configure(bg="lightblue")

# Title Label
title_label = tk.Label(root, text="Attendance System", font=("Helvetica", 16), bg="lightblue")
title_label.pack(pady=20)

# Name Input Section
name_label = tk.Label(root, text="Enter Name:", font=("Helvetica", 12), bg="lightblue")
name_label.pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Buttons
btn_add_faces = tk.Button(root, text="Add Face Data", command=run_add_faces, width=20, height=2)
btn_add_faces.pack(pady=10)

btn_take_attendance = tk.Button(root, text="Take Attendance", command=run_take_attendance, width=20, height=2)
btn_take_attendance.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", command=root.quit, width=20, height=2)
btn_exit.pack(pady=10)

# Start the main event loop
root.mainloop()
