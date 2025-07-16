import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    label.config(text=current_time)
    root.after(1000, update_time)  # Update every second

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("350x150")
root.resizable(False, False)
root.configure(bg = "black")

label = tk.Label(root, font=("Helvetica", 35), bg="black", fg="cyan")
label.pack(expand=True)

update_time() 

root.mainloop()
