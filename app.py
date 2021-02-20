from tkinter import *
import tkinter.messagebox as tsmg
root = Tk()
root.geometry("480x546")
root.title("Flight Booking Plane")
Label(root,text="Which country do you want to visit?").pack()
country = ["Ukraine","England","Turkey","Montenegro"]
var = StringVar()
new_var = var.set("nonewhere")
def journey():
    tsmg.showinfo("Let's Travel!",f"So you're booking your flight to {var.get()}\nWe hope that you will have a happy journey!:)")
for x in range(4):
    Radiobutton(root,text=country[x],variable=var,value=country[x]).pack()
Button(root,text="Let's travel with us!",command=journey).pack()
root.mainloop()