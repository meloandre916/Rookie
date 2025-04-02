import json
import os

import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    name = entry_task.get()
    priority = priority_var.get()

    if name:
        task = {"name": name, "priority": priority}
        tasks.append(task)
        update_task_list()
        save_tasks()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task name.")

def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        listbox_tasks.insert(tk.END, f"{i}. {task['name']} - {task['priority']}")

def delete_task():
    selection = listbox_tasks.curselection()
    if selection:
        index = selection[0]
        del tasks[index]
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            update_task_list()
# GUI Setup
window = tk.Tk()
window.title("To-Do List")

frame = tk.Frame(window)
frame.pack(pady=10)

entry_task = tk.Entry(frame, width=30)
entry_task.grid(row=0, column=0, padx=5)

priority_var = tk.StringVar(value="Medium")
dropdown = tk.OptionMenu(frame, priority_var, "High", "Medium", "Low")
dropdown.grid(row=0, column=1, padx=5)

btn_add = tk.Button(frame, text="Add Task", command=add_task)
btn_add.grid(row=0, column=2, padx=5)

listbox_tasks = tk.Listbox(window, width=50)
listbox_tasks.pack(pady=10)

btn_delete = tk.Button(window, text="Delete Selected Task", command=delete_task)
btn_delete.pack()

load_tasks()
window.mainloop()
