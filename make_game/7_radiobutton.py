from tkinter import *

root = Tk()
root.title("Park's UI")
root.geometry("640x480")

label1 = Label(root, text="menu").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="hamburger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="cheese_hamburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chicken_hamburger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root,text="drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="coke", value="coke",variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="cider", value="cider",variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
