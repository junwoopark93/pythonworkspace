from tkinter import *

root = Tk()
root.title("Park's UI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0,"사과")
listbox.insert(1,"straw")
listbox.insert(2,"banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    #listbox.delete(0)

    #print("리스트에는", listbox.size(),"개가 있습니다.")
    #print(listbox.get(0,2))
    print(listbox.curselection())
btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
