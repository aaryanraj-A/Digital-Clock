import tkinter as tk
import time as time_module

root = tk.Tk()
root.title("Digital Clock")

def update_time():
    string = time_module.strftime('%H:%M:%S %p\n %d/%m/%y')
    label.config(text=string)
    label.after(1000, update_time)


label = tk.Label(root, font=('calibri', 50, 'bold'), background='light blue', foreground='black')

label.pack(anchor='center')

update_time()

root.mainloop()