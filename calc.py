from tkinter import *
from tkinter import ttk

window = Tk()
window.title("calc")
window.geometry("280x200+600+200")
window.resizable(False, False)

label = ttk.Label(text="", background="#FFCDD2")
label.place(x=20, y=10)

sym = ["X", "+", "-", "*", "/"]

label2 = ttk.Label(text="")
label2.place(x=20, y=160)

sum = []

def equals():
    label2["text"] = label["text"]
    label2["background"] = ""
    try:
        label["text"] = eval(label["text"])
    except:
        label["text"] = ""
        label2["background"] = "#FFCDD2"
        label2["text"] = "Error"

def plus(): label["text"] = str(label["text"]) + " + "
def minus(): label["text"] = str(label["text"]) + " - "
def multiply(): label["text"] = str(label["text"]) + " * "
def divide(): label["text"] = str(label["text"]) + " / "

def clear():
    label["text"] = ""
    label2["text"] = ""
    label2["background"] = ""

def btn_0(): label["text"] = str(label["text"]) + "0"
def btn_1(): label["text"] = str(label["text"]) + "1"
def btn_2(): label["text"] = str(label["text"]) + "2"
def btn_3(): label["text"] = str(label["text"]) + "3"
def btn_4(): label["text"] = str(label["text"]) + "4"
def btn_5(): label["text"] = str(label["text"]) + "5"
def btn_6(): label["text"] = str(label["text"]) + "6"
def btn_7(): label["text"] = str(label["text"]) + "7"
def btn_8(): label["text"] = str(label["text"]) + "8"
def btn_9(): label["text"] = str(label["text"]) + "9"

func_nums = [0, btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9]
x_coord = 20
y_coord = 40
count_nums = 1
for i in range(3):
    for j in range(1, 4):
        ttk.Button(text=count_nums, command=func_nums[count_nums], width=8).place(
            x=x_coord, y=y_coord)
        x_coord += 60
        count_nums += 1
    x_coord = 20
    y_coord += 30

func_sym = [0, plus, minus, multiply, divide]
x_coord = 210
y_coord = 40
for i in range(1, 5):
    ttk.Button(text=sym[i], command=func_sym[i],
               width=8).place(x=x_coord, y=y_coord)
    y_coord += 30

ttk.Button(text="=", command=equals, width=8).place(x=20, y=130)
ttk.Button(text="clear", command=clear,  width=8).place(x=140, y=130)
ttk.Button(text=0, command=btn_0,  width=8).place(x=80, y=130)

window.mainloop()