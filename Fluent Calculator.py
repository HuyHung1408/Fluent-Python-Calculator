from tkinter import ttk
import tkinter as tk
from tkinter import*

def btnClick(numbers) :
    global operator
    operator=operator+str(numbers)
    tex_input.set(operator)

def btnClearDisplay():
    global operator
    tex_input.set("")
    operator=""

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    tex_input.set(sumup)
    operator=""

cal = Tk()
cal.title('Fluent Calculator')
operator=""
tex_input= StringVar()
cal.geometry('212x242')

cal.grid_columnconfigure(0,weight=1)
cal.grid_columnconfigure(1,weight=1)
cal.grid_columnconfigure(2,weight=1)
cal.grid_columnconfigure(3,weight=1)

#Entry to show result
txtDisplay = ttk.Entry(cal, textvariable=tex_input, font='12', justify='right').grid(columnspan=5, pady=10)

#First Column
btn7=ttk.Button(cal, text="7", command=lambda:btnClick(7)).grid(row=1, column=0, padx= 10, pady= 5)
btn4=ttk.Button(cal, text="4", command=lambda:btnClick(4)).grid(row=2, column=0, padx= 10, pady= 5)
btn1=ttk.Button(cal, text="1", command=lambda:btnClick(1)).grid(row=4, column=0, padx= 10, pady= 5)
btn1=ttk.Button(cal, text="0", command=lambda:btnClick(0)).grid(row=5, column=0, padx= 10, pady= 5)

#Second Column
btn8=ttk.Button(cal, text="8", command=lambda:btnClick(8)).grid(row=1, column=1, padx= 0, pady= 0)
btn5=ttk.Button(cal, text="5", command=lambda:btnClick(5)).grid(row=2, column=1, padx= 0, pady= 0)
btn2=ttk.Button(cal, text="2", command=lambda:btnClick(2)).grid(row=4, column=1, padx= 0, pady= 0)
btnClear=ttk.Button(cal, text="C", style="Accent.TButton", command=btnClearDisplay).grid(row=5, column=1, padx= 10, pady= 0)

#Thỉrd Column
btn9=ttk.Button(cal, text="9", command=lambda:btnClick(9)).grid(row=1, column=2, padx= 0, pady= 0)
btn6=ttk.Button(cal, text="6", command=lambda:btnClick(6)).grid(row=2, column=2, padx= 0, pady= 0)
btn3=ttk.Button(cal, text="3", command=lambda:btnClick(3)).grid(row=4, column=2, padx= 0, pady= 0)
equal=ttk.Button(cal, text="=", style="Accent.TButton", command=btnEqualsInput).grid(row=5, column=2, padx= 10, pady= 0)

#Fourth Column
Addition=ttk.Button(cal, text="+",  command=lambda:btnClick("+")). grid(row=1, column=3, padx= 10, pady= 0)
Subtraction=ttk.Button(cal, text="-", command=lambda:btnClick("-")). grid(row=2, column=3, padx= 10, pady= 0)
Multiple=ttk.Button(cal, text="x", command=lambda:btnClick("*")). grid(row=4, column=3, padx= 10, pady= 0)
Divsion=ttk.Button(cal, text=":", command=lambda:btnClick("/")). grid(row=5, column=3, padx= 10, pady= 0)

cal.tk.call("source", "sun-valley.tcl")
cal.tk.call("set_theme", "light")  #You can change to "dark"

#Min width for the calculator
cal.update()
cal.minsize(cal.winfo_width(), cal.winfo_height())
x_cordinate = int((cal.winfo_screenwidth() / 2) - (cal.winfo_width() / 2))
y_cordinate = int((cal.winfo_screenheight() / 2) - (cal.winfo_height() / 2))
cal.resizable(False, False)

cal.mainloop()