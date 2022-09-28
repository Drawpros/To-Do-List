# Adding tasks into one text widget
import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.geometry("310x400")

text = tk.Text(root, width=30, height=10)
text.pack(pady = 15)

entry = ttk.Entry(root, width = 30, font=20)
entry.focus()
entry.pack(ipady = 10)

def new_task():
    if entry.get() == "" or entry.get() == " ":
        pass
    else:
        text.insert(INSERT, f"{entry.get()} \n")
        entry.delete(0, END)

def nsk(event):
    if entry.get() == "" or entry.get() == " ":
        pass
    else:
        text.insert(INSERT, f"{entry.get()} \n")
        entry.delete(0, END)

def delete(event):
    text.delete("end-2l","end-1l")
    entry.delete(0, END)

add_task = tk.Button(root, text="Add task", height=2, width=20, font=50, command=new_task)
root.bind('<Control-r>', nsk)
root.bind('<Control-t>', delete)
add_task.pack(pady=5)

def delete_last_task():
    text.delete("end-2l","end-1l")
    entry.delete(0, END)

delete_task = tk.Button(root, text="Delete last task", height=2, width=20, font=50, command=delete_last_task)
delete_task.pack(pady=5)


root.mainloop()