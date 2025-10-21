from tkinter import *; import re
tk = Tk()
tk.geometry("200x370")
tk.title('Calculator')
string=''
def calculation(what):
    global string
    if re.fullmatch(r"[0-9\+\-\*/\(\)\.\^ Clear=]+", what):
        if what == 'Clear':
            string=''
        if what == '=':
            string= eval(string)
        else:
            if re.fullmatch(r"[0-9\+\-\*/\(\)\.\^ =]+", what):    
                string = string+what
    else:   
        string='ERROR'
    Label(tk, text=string,font=('Arial', 14)).place(x='0',y='0',width='200',height='100')
def snoop():
    Label(tk, image=img).place(x='0',y='0',width='200',height='100')
w = 50;h=50
frame = Frame(tk,borderwidth=5, relief='sunken').place(x='0',y='0',width='200',height='100')
img = PhotoImage(file=r'C:\Users\denke\Desktop\SOMETHING\supercalculator_\snop.png')
img = img.subsample(3, 2)
Label(tk, image=img).place(x='0',y='0',width='200',height='100')
button1 = Button(tk, text='1', command=lambda: calculation('1')).place(x='0',y='100',width=w,height=h)
button2 = Button(tk, text='2', command=lambda: calculation('2')).place(x='50',y='100',width=w,height=h)
button3 = Button(tk, text='3', command=lambda: calculation('3')).place(x='100',y='100',width=w,height=h)
button4 = Button(tk, text='4', command=lambda: calculation('4')).place(x='0',y='150',width=w,height=h)
button5 = Button(tk, text='5', command=lambda: calculation('5')).place(x='50',y='150',width=w,height=h)
button6 = Button(tk, text='6', command=lambda: calculation('6')).place(x='100',y='150',width=w,height=h)
button7 = Button(tk, text='7', command=lambda: calculation('7')).place(x='0',y='200',width=w,height=h)
button8 = Button(tk, text='8', command=lambda: calculation('8')).place(x='50',y='200',width=w,height=h)
button9 = Button(tk, text='9', command=lambda: calculation('9')).place(x='100',y='200',width=w,height=h)
button10 = Button(tk, text='+', command=lambda: calculation('+')).place(x='150',y='100',width=w,height=h)
button11 = Button(tk, text='0', command=lambda: calculation('0')).place(x='0',y='250',width=w,height=h)
button12 = Button(tk, text='-', command=lambda: calculation('-')).place(x='150',y='150',width=w,height=h)
button13 = Button(tk, text='/', command=lambda: calculation('/')).place(x='150',y='200',width=w,height=h)
button14 = Button(tk, text='*', command=lambda: calculation('*')).place(x='150',y='250',width=w,height=h)
button15 = Button(tk, text='^', command=lambda: calculation('**')).place(x='50',y='250',width=w,height=h)
button16 = Button(tk, text='(', command=lambda: calculation('(')).place(x='100',y='250',width=w,height=h)
button17 = Button(tk, text=')', command=lambda: calculation(')')).place(x='0',y='300',width=w,height=h)
button18 = Button(tk, text='=', command=lambda: calculation('=')).place(x='150',y='300',width=w,height=h)
button19 = Button(tk, text='Clear', command=lambda: calculation('Clear')).place(x='50',y='300',width=100,height=h)
snoop_button = Button(tk, text='snoop', command=snoop).place(x='0',y='350',width='200',height='20')

tk.mainloop()