from tkinter import *


window = Tk()
window.geometry('395x410')
window.title('Huỳnh Vĩnh Tiến - Calculator')
window.configure(bg='#5260d9')
window.iconbitmap('171352_calculator_icon.ico')

exp=''

def press(n):
    global exp
    exp += str(n)
    equation.set(exp)

def equal():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        exp=''
    except:
        equation.set('Error')
        exp=''

def clear():
    global exp
    exp=''
    equation.set('0')

def backspace():
    global exp
    exp=exp[:-1]
    equation.set(exp)

exp_frame=Frame(window, bg='#5260d9')
button_frame=Frame(window , bg='#5260d9')
exp_frame.pack()
button_frame.pack()



font_entry=('ariel',20,'bold')
font_button=('new times roman')

equation=StringVar()
equation.set('0')
eqfield= Entry(exp_frame,textvariable=equation,font=font_entry, justify='right')
eqfield.pack(ipadx=10,ipady=10,pady=20)

button1=Button(button_frame, text='1', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press(1))
button2=Button(button_frame, text='2', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press(2))
button3=Button(button_frame, text='3', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press(3))
plus=Button(button_frame, text='+', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press('+'))

button4=Button(button_frame, text='4', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press(4))
button5=Button(button_frame, text='5', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press(5))
button6=Button(button_frame, text='6', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press(6))
minus=Button(button_frame, text='-', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press('-'))

button7=Button(button_frame, text='7', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press(7))
button8=Button(button_frame, text='8', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press(8))
button9=Button(button_frame, text='9', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press(9))
multiply=Button(button_frame, text='x', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press('*'))

button0=Button(button_frame, text='0', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press(0))
decimal=Button(button_frame, text='.', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press('.'))
clear=Button(button_frame, text='C', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2, command= clear)
divide=Button(button_frame, text='/', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= lambda: press('/'))
equal=Button(button_frame, text='=', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2,command= equal)
backspace=Button(button_frame, text='Back', font='font_button', relief='raised' , bg='#d8f2f0', borderwidth=1, width=8,height=2, command=backspace)


button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
plus.grid(row=0,column=3)

button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
minus.grid(row=1,column=3)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
multiply.grid(row=2,column=3)

button0.grid(row=3,column=0)
decimal.grid(row=3,column=1)
clear.grid(row=3,column=2)
divide.grid(row=3,column=3)

backspace.grid(row=4,column=0, columnspan=3 ,sticky='nsew')
equal.grid(row=4,column=3)



window.mainloop() 