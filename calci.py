import tkinter
from tkinter import *

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()
window.title("CALCULATOR")
window.geometry("300x500")
window.config(bg='white')
equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('concolas',20), bg="white", width=24, height=2,highlightbackground="black",highlightthickness=2)
label.pack()

frame = Frame(window)
frame.pack()

button_border=tkinter.Frame(window,highlightbackground ="black",highlightthickness= 10, bd=0)

button1 = Button(frame, text=1,fg='white', height=3, width=6, font=35,bg='black',
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, fg='white',height=3, width=6, font=35,bg='black',
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3,fg='white', height=3, width=6, font=35,bg='black',
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, fg='white',height=3, width=6, font=35,bg='black',
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5,fg='white', height=3, width=6, font=35,bg='black',
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6,fg='white', height=3, width=6, font=35,bg='black',
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, fg='white',height=3, width=6, font=35,bg='black',
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, fg='white',height=3, width=6, font=35,bg='black',
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9,fg='white', height=3, width=6, font=35,bg='black',
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0,fg='white', height=3, width=6, font=35,bg='black',
                 command=lambda: button_press(0))
button0.grid(row=3, column=1)

plus = Button(frame, text='+',fg='white', height=3, width=6, font=35,bg='red',
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)



minus = Button(frame, text='-',fg='white', height=3, width=6, font=35,bg='red',
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*',fg='white', height=3, width=6, font=35,bg='red',
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/',fg='white', height=3, width=6, font=35,bg='red',
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)


equal = Button(frame, text='=',fg='white', height=3, width=6, font=35,bg='red',
                 command=equals)
equal.grid(row=3, column=2)


decimal = Button(frame, text='.', fg='white',height=3, width=6, font=35,bg='red',
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=0)

clear = Button(window, text='clear',fg='white', height=3, width=30, font=35,bg='blue',
                 command=clear)
clear.pack()

window.mainloop()
