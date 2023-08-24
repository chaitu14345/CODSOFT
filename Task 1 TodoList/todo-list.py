import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo List")
        self.tasks = []
        
        self.task_entry = tk.Entry(root, width=50, bg="#EDB6D5", fg="#551B8C", font=("Roboto", 10, "bold"))
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#2AF598", fg="black", font=("Arial", 10, "bold"))
        self.clear_button = tk.Button(root, text="Clear List", command=self.clear_list, bg="#F9476B", fg="white", font=("Sangu", 10, "bold"))
        self.task_list = tk.Listbox(root, width=50, bg="#909AC9", fg="#700A0F", font=("Arial", 10, "bold"))

        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)
        self.clear_button.grid(row=2, column=1, padx=5, pady=10)
        self.task_list.grid(row=1, column=0, padx=10, pady=10, rowspan=2)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")


    def clear_list(self):
        self.tasks = []
        self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

