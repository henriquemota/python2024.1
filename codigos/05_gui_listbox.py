import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Listbox in Tk")
listbox = tk.Listbox()
items = tk.StringVar()
items.set(
    "Python "
    "C "
    "C++ "
    "Java "
)
listbox = tk.Listbox(listvariable=items)
listbox.pack()
root.mainloop()