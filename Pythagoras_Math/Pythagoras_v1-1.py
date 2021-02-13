import math
from tkinter import *
from tkinter import messagebox as tsmg
from datetime import datetime


def getvals():
	now = datetime.now()
	current_time = now.strftime("%Y:%H:%M:%S")

	num1 = int(e1.get())
	num2 = int(e2.get())
	ans = (num1**2 + num2**2)
	ans1 = math.sqrt(ans)
	tsmg.showinfo('Answer', ans1)

	hf = open("HistoryOfPythagoras.txt", "a")
	hf.write(f"{num1} and {num2} Answer: {ans1} Time: {current_time}\n")
	hf.close()


root = Tk()
root.title("Pythagoras Theorems Solutions Software")
root.geometry("500x500")

ll = Label(root, text="Hello, I am the problem solver software for Pythagoras Theorems", font="comicsans 14 bold").pack()
label1 = Label(root, text="Enter the first number:", font="comicsans 15 bold").pack()

e = IntVar()
e1 = Entry(root, textvariable=e, font="comicsans 14 bold")
e1.pack()

label2 = Label(root, text="Enter the second number:", font="comicsans 14 bold").pack()

ee = IntVar()
e2 = Entry(root, textvariable=ee, font="comicsans 14 bold")
e2.pack()

bu_1 = Button(root, text="Submit", font="comicsans 14 bold", command=getvals).pack()
root.mainloop()