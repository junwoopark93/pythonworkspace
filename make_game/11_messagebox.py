import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Park's UI")
root.geometry("640x480")

def info():
    msgbox.showinfo("alert","good condition")

def warn():
    msgbox.showwarning("warn","no left seat")

def error():
    msgbox.showerror("error","pay error!!")


def okcancel():
    msgbox.askokcancel("choose ok or cancel","this seat for baby?")


def retrycancel():
    msgbox.askretrycancel("retry or cancel","retry or cancel")


def yesno():
    msgbox.askyesno("yes or no","yes or no?")


def yesnocancel():
    response = msgbox.askyesnocancel(title=None,message="yes or no or cancel")

    print(response)
    if response == 1:
        print("yes")
    elif response == 0:
        print("no")
    else:
        print("cancel")

Button(root, command=info, text="alert!!!").pack()
Button(root, command=warn, text="warning!!!").pack()
Button(root, command=error, text="error!!!").pack()

Button(root, command=okcancel, text="choose one").pack()

Button(root, command=retrycancel, text="retry?").pack()

Button(root, command=yesno, text="yes or no").pack()

Button(root, command=yesnocancel, text="yes or no or cancel").pack()




root.mainloop()
