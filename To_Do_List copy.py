import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.geometry("310x400")

entry = ttk.Entry(root, width = 30, font=20)
entry.focus()
entry.pack(ipady = 10)

def new_task():
    if entry.get() == "" or entry.get() == " ":
        pass
    else:
        def del_task():
            text.destroy()
            checkbox.destroy()

        text = tk.Text(root, width=30, height=1)
        text.pack()

        checkbox = ttk.Checkbutton(root, variable = tk.StringVar, text='Done', command=del_task)
        checkbox.pack()
        
        text.insert(INSERT, f"{entry.get()}")
        entry.delete(0, END)

def nsk(event):
    if entry.get() == "" or entry.get() == " ":
        pass
    else:
        def del_task():
            text.destroy()
            checkbox.destroy()

        text = tk.Text(root, width=30, height=1)
        text.pack()
        
        checkbox = ttk.Checkbutton(root, variable = tk.StringVar, text='Done', command=del_task)
        checkbox.pack()
        
        text.insert(INSERT, f"{entry.get()}")
        entry.delete(0, END)

add_task = tk.Button(root, text="Add task", height=2, width=20, font=50, command=new_task)
# when event binding, you have to bind to the widget (or just root) that the user is in (using, focused) when the shortcut is clicked
root.bind('<Control-r>', nsk)
add_task.pack(pady=5)


root.mainloop()