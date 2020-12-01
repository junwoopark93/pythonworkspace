import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Park's UI")
root.geometry("640x480")

Label(root, text="choose menu").pack(side="top")

Button(root, text="order").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side = "left", fill = "both",expand=True)

Button(frame_burger, text="hamburger").pack()
Button(frame_burger, text="cheese_hamburger").pack()
Button(frame_burger, text="chicken_hamburger").pack()

frame_drink = LabelFrame(root, text="drink")
frame_drink.pack(side = "right", fill="both", expand=True)

Button(frame_drink, text="coke").pack()
Button(frame_drink, text="cider").pack()

root.mainloop()
