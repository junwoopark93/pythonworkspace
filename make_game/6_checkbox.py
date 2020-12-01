from tkinter import *

root = Tk()
root.title("Park's UI")
root.geometry("640x480")

chkvar = IntVar()
chkbox = Checkbutton(root, text="checkbox", variable=chkvar)
#chkbox.select()
#chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="checkbox2", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())
    print(chkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
