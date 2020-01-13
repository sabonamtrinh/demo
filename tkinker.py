from tkinter import *

window = Tk()
window.title("Hello")
lb = Label(window, text ="A")
lb.grid(column=0, row=0)
lb1 = Label(window, text ="b")
lb1.grid(column=0, row=1)
window.mainloop()
