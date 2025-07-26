import tkinter as tk
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x400")
        self.root.title("NoxList")
        self.main = tk.Listbox(self.root,bg="light sky blue",width=self.root.winfo_width(),height="400",justify="center",font=("Times New Roman",20))
        self.head = tk.Frame(self.root,bg="deep sky blue")
        self.head.pack(fill="x",ipady="10")
        self.main.pack(fill="x",ipady="50")
        self.title = tk.Label(self.head,text="NoxList",anchor="center",font=("Courier", 30),bg="deep sky blue")
        self.title.pack()
        self.add = tk.Button(self.head,text="Add Task",command=self.add_task)
        self.task_entry = tk.Entry(self.head)
        self.task_entry.pack()
        self.main.bind('<<ListboxSelect>>', self.task_detail)
        self.add.pack()
    def add_task(self):
        name_task = self.task_entry.get()
        self.task_entry.delete(0,tk.END)
        self.main.insert(1,name_task)
        return name_task
    def task_detail(self,e):
        print(self.main.get("active"))

if __name__ == "__main__":
    gui = GUI()
    gui.root.mainloop()