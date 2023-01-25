from tkinter import *
from tkinter import ttk
import math

fundo = "#2F2F4F"
cor1 = "#3b3b3b"
cor3 = "#38576b"
cor4 = "#FFAB40"
cor5 = "#feffff"
cor7 = "#ab8918"
cor8 = "#ECEFF1"
cor9 = "#424345"

janela = Tk()
janela.title("")
janela.geometry("233x281")
janela.config(bg = cor1)

style = ttk.Style(janela)
style.theme_use("clam")

ttk.Separator(janela, orient = HORIZONTAL).grid(row = 0, columnspan = 1, ipadx = 280)

frame_tela = Frame(janela, width = 300, height = 54 , bg = cor1, pady = 0, padx = 0, relief = "flat",)
frame_tela.grid(row = 1, column = 0, sticky = NW)
frame_cientifica = Frame(janela, width = 300, height = 85, bg = cor1, pady = 0, padx = 0, relief = "flat",)
frame_cientifica.grid(row = 2, column = 0, sticky = NW)
frame_corpo = Frame(janela, width = 300, height = 340, bg = cor1, pady = 0, padx = 0, relief = "flat",)
frame_corpo.grid(row = 3, column = 0, sticky = NW)

def entering_values(event):
    global all_values
    all_values = all_values + str(event)
    value_text.set(all_values)

def calculate():
    global all_values
    global texto
    texto = all_values
    mod = ['math.sqrt','math.e', 'math.pow','math.pi']
    for i in mod:
        if i == 'math.sqrt':
            texto = texto.replace("sqrt",i)
        if i == 'math.e':
            texto = texto.replace("e",i)
        if i == 'math.pow':
            texto = texto.replace("pow",i)
        if i == 'math.pi':
            texto = texto.replace("pi",i)
    
    
    result = str(eval(texto))
    value_text.set(result)
    all_values = ""
          
def screen_clear():
    global all_values
    all_values = ""
    value_text.set("")

def seno():
    global all_values
    global texto
    texto = float(all_values)
    texto = math.sin(math.radians(texto))
    result = str("%.2f"%texto)
    value_text.set(result)
    all_values = ""

def cosseno():
    global all_values
    global texto
    texto = float(all_values)
    texto = math.cos(math.radians(texto))
    result = str("%.2f"%texto)
    value_text.set(result)
    all_values = ""

def tg():
    global all_values
    global texto
    texto = float(all_values)
    texto = math.tan(math.radians(texto))
    result = str("%.2f"%texto)
    value_text.set(result)
    all_values = ""

def log10():
    global all_values
    global texto
    texto = float(all_values)
    texto = math.log10(texto)
    result = str("%.2f"%texto)
    value_text.set(result)
    all_values = ""

def ln():
    global all_values
    global texto
    texto = float(all_values)
    texto = math.log(texto)
    result = str("%.2f"%texto)
    value_text.set(result)
    all_values = ""


all_values = ""
value_text = StringVar()

label_tela = Label(janela, textvariable = value_text, width = 20, height = 2 , padx = 7, anchor = 'e',bd = 0, justify = RIGHT, font = ("Ivy 14"), bg = cor1, fg = cor8)
label_tela.place(x = 0, y = 0)

b_tg = Button(frame_cientifica, text = 'tg', width = 7, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: tg())
b_tg.place(x = -7, y = 1)
b_sin = Button(frame_cientifica, text = 'sin', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: seno())
b_sin.place(x = 59, y = 1)
b_cos = Button(frame_cientifica, text = 'cos', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: cosseno())
b_cos.place(x = 117, y = 1)
b_sqrt = Button(frame_cientifica, text = '√', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values('sqrt'))
b_sqrt.place(x = 175, y = 1)

b_log = Button(frame_cientifica, text = 'ln', width = 7, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: ln())
b_log.place(x = -7, y = 29)
b_log10 = Button(frame_cientifica, text = 'log', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: log10())
b_log10.place(x = 59, y = 29)
b_euler = Button(frame_cientifica, text = 'e', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values('e'))
b_euler.place(x = 117, y = 29)
b_pow = Button(frame_cientifica, text = 'pow', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values('pow'))
b_pow.place(x = 175, y = 29)

b_pi = Button(frame_cientifica, text = 'π', width = 7, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values('pi'))
b_pi.place(x = -7, y = 57)
b_comma = Button(frame_cientifica, text = ',', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(','))
b_comma.place(x = 59, y = 57)
b_parentheses1 = Button(frame_cientifica, text = '(', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values('('))
b_parentheses1.place(x = 117, y = 57)
b_parentheses2 = Button(frame_cientifica, text = ')', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(')'))
b_parentheses2.place(x = 175, y = 57)

b_clear = Button(frame_corpo, text = 'C', width = 14 ,height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor4, fg = cor5, command = lambda: screen_clear())
b_clear.place(x = -5, y = 0)
b_mod = Button(frame_corpo, text = '%', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor4, fg = cor5,  command = lambda: entering_values('%'))
b_mod.place(x = 117, y = 0)
b_division = Button(frame_corpo, text = '/', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor4, fg = cor5, command = lambda: entering_values('/'))
b_division.place(x = 175, y = 0)

b_7 = Button(frame_corpo, text = '7', width = 7, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(7))
b_7.place(x = -7 , y = 28)
b_8 = Button(frame_corpo, text = '8', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(8))
b_8.place(x = 59, y = 28)
b_9 = Button(frame_corpo, text = '9', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(9))
b_9.place(x = 117, y = 28)
b_multiplication = Button(frame_corpo, text = '*', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor4, fg = cor5, command = lambda: entering_values('*'))
b_multiplication.place(x = 175, y = 28)

b_4 = Button(frame_corpo, text = '4', width = 7, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(4))
b_4.place(x = -7, y = 56)
b_5 = Button(frame_corpo, text = '5', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(5))
b_5.place(x = 59, y = 56)
b_6 = Button(frame_corpo, text = '6', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(6))
b_6.place(x = 117, y = 56)
b_sub = Button(frame_corpo, text = '-', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor4, fg = cor5, command = lambda: entering_values('-'))
b_sub.place(x = 175, y = 56)

b_1 = Button(frame_corpo, text = '1', width = 7, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(1))
b_1.place(x = -7, y = 84)
b_2 = Button(frame_corpo, text = '2', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(2))
b_2.place(x = 59, y = 84)
b_3 = Button(frame_corpo, text = '3', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(3))
b_3.place(x = 117, y = 84)
b_sum = Button(frame_corpo, text = '+', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor4, fg = cor5, command = lambda: entering_values('+'))
b_sum.place(x = 175, y = 84)

b_0 = Button(frame_corpo, text = '0', width = 14, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values(0))
b_0.place(x = -5, y = 112)
b_equals = Button(frame_corpo, text = '.', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor8, fg = cor1, command = lambda: entering_values('.'))
b_equals.place(x = 117, y = 112)
b_equals = Button(frame_corpo, text = '=', width = 6, height = 1, relief = RAISED ,overrelief = RIDGE ,font = ("Ivy 10 bold"), bg = cor4, fg = cor5, command = lambda: calculate())
b_equals.place(x = 175, y = 112)


janela.mainloop()