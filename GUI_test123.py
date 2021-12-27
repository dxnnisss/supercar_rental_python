from tkinter import *



top = Tk()
top.title("SuperCar Rental Services")
top.geometry("500x700")

label = Label(top, text='This is a label')
label.pack(ipadx=10, ipady=10)

label.config("Verdana")



# mb = Menubutton(top, text="condiments", relief=RAISED)
# mb.grid()
# mb.menu = Menu(mb, tearoff = 0)
# mb["menu"] = mb.menu
#
# mayoVar = IntVar()
# ketchVar = IntVar()
#
# mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
# mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)
#
# mb.pack()
top.mainloop()