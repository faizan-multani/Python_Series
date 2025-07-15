import tkinter as tk
import pyautogui

def take_ss():
    add_data = entry.get()
    path = add_data + "\\test12.png"
    ss = pyautogui.screenshot()
    ss.save(path)

root = tk.Tk()
root.title("Screenshot Tool")
root.geometry("500x150")


label = tk.Label(root, text="Enter directory path:")
label.pack(pady=5)


entry = tk.Entry(root, width=40)
entry.pack(pady=5)


btn = tk.Button(root, text="Take Screenshot", command=take_ss)
btn.pack(pady=10)

root.mainloop()
