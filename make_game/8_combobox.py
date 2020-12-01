import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Park's UI")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("card payday")

readcombobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readcombobox.current(0)
readcombobox.pack()

def btncmd():
    print(combobox.get())
    print(readcombobox.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
