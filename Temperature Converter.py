from tkinter import *
from tkinter import INSERT
import dis

def Temperature_Conversion():
    temp = int((var.get() - 32) * 5/9)
    convert = str(temp) + u'\N{DEGREE SIGN}' +" Celcsius"
    label2.config(text=convert)


convertApp = Tk()
convertApp.title(" Temperature Converter")
convertApp.resizable(0, 0)

var = DoubleVar()

label1 = Label(convertApp, text="Temperature Converter\nFarenheit to Celsius", padx=16, pady=16, bd=16,
               fg="#000000", font=('arial', 30, 'bold'), bg="sky blue", relief='raise',
               width=20, height=4)
label1.pack()

slider = Scale(convertApp, variable=var, from_=-40, to=300, length=500, tickinterval=20, orient=HORIZONTAL)
slider.pack(anchor=CENTER)

label2 = Label(convertApp, padx=16, pady=16, bd=16,fg="#000000", font=('arial', 30, 'bold'),
               bg="sky blue", relief='sunk', width=20, height=4)
label2.pack()

label3 = Label(convertApp, text="")
label3.pack()

button = Button(convertApp, text="Covert to Calcius",  padx=16, pady=16, bd=16,
                width=20, font=('arial', 30, 'bold'), command=Temperature_Conversion)
button.pack(anchor=CENTER)
convertApp.mainloop()