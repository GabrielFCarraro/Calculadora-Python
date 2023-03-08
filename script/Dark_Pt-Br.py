from tkinter import *
from tkinter import messagebox
import PIL

#DEF DA JANELA
janela = Tk()
janela.title('Calculadora')
janela.geometry('450x650')
janela.iconbitmap('ico/calculator.ico')
janela.resizable(False, False)
janela.config(background='#BEBEBE')

#FUNDO
img_bgfundo = PhotoImage(file = 'png/darkbr.png')
img_fundo = Label(janela, image = img_bgfundo)
img_fundo.config(width = 450, height = 650)
img_fundo.place(x = -2, y = 0)


#DISPLAY 1
display = StringVar()
datadisplay = Entry(janela, textvariable = display, font = "Serif 30", fg = 'white', justify = 'right', background = '#414141', border = 0)
datadisplay.grid(row = 0,columnspan = 3, ipadx=50, ipady=10)
datadisplay.place(x = 5, y = 60)


#DISPLAY2
display2 = StringVar()
datadisplay2 = Entry(janela, textvariable = display2, font = 'Serif 15', fg = 'white', justify = 'right', background = '#414141', border = 0)
datadisplay2.place(x = 225, y = 5)

#DISPLAY 3
display3 = StringVar()
datadisplay3 = Entry(janela, textvariable = display3, font = 'Serif 15', fg = 'white', justify = 'right', background = '#414141', border = 0)
datadisplay3.place(x = 225, y = 32)

#=======================================================DEFS DISPLAY E ESQUAÇÕES=====================================
#COLOCA O NÚMERO 0 QUANDO NÃO TIVER NADA
if datadisplay.get() == '':
    display.set('0')

#DEF NÚMEROS
expression = ''
def botao (x):
    global expression
    expression = expression + str(x)
    display.set(expression)

#DEF DISPLAY DO MEIO (APRECE OS OPERADORES)    
def display_do_meio():
    if '+' in datadisplay.get():
        display3.set('+')                 
    if '-' in datadisplay.get():
        display3.set('-')
    if '*' in datadisplay.get():
        display3.set('*')
    if '/' in datadisplay.get():
        display3.set('/')
    if '%|' in datadisplay.get():
        display3.set('%|')
    if '%?' in datadisplay.get():
        display3.set('%?')          

#DEF APARECER NÚMERO NO DISPLAY DE CIMA
def display_de_cima():
    global expression
    if '+' in datadisplay.get():
        display2.set(expression)
        if '+' in datadisplay2.get():
            lendi = len(datadisplay2.get())
            datadisplay2.delete(lendi-1, 'end')            
    if '-' in datadisplay.get():
        display2.set(expression)
        if '-' in datadisplay2.get():
            lendi2 = len(datadisplay2.get())
            datadisplay2.delete(lendi2-1, 'end')
    if '*' in datadisplay.get():
        display2.set(expression)
        if '*' in datadisplay2.get():
            lendi3 = len(datadisplay2.get())
            datadisplay2.delete(lendi3-1, 'end')                     
    if '/' in datadisplay.get():
        display2.set(expression)
        if '/' in datadisplay2.get():
            lendi4  = len(datadisplay2.get())
            datadisplay2.delete(lendi4-1, 'end')
    if '%|' in datadisplay.get():
        display2.set(expression)
        if '%|' in datadisplay2.get():
            lendi5 = len(datadisplay2.get())
            datadisplay2.delete(lendi5-2, 'end') 
    if '%?' in datadisplay.get():
        display2.set(expression)
        if '%?' in datadisplay2.get():
            lendi6 = len(datadisplay2.get())
            datadisplay2.delete(lendi6-2, 'end')             

#EQUAÇÃO 
def equação ():
    global expression
    if '+' in datadisplay3.get():
        soma = float(datadisplay2.get()) + float(datadisplay.get())
        display.set(soma)
        expression = str(soma)        
    if '-' in datadisplay3.get():
        sub = float(datadisplay2.get()) - float(datadisplay.get())
        display.set(sub)
        expression = str(sub)
    if '*' in datadisplay3.get():
        multi = float(datadisplay2.get()) * float(datadisplay.get())
        display.set(multi)
        expression = str(multi)
    if '/' in datadisplay3.get():
        div = float(datadisplay2.get()) / float(datadisplay.get())
        display.set(div)
        expression = str(div)                    
    if  '%|' in datadisplay3.get(): 
        totalporc = float(datadisplay2.get()) * float(datadisplay.get()) / 100
        display.set(totalporc)
        expression = str(totalporc)
        print(datadisplay.get(), datadisplay2.get())
    if  '%?' in datadisplay3.get():
        porcent2 = float(datadisplay2.get()) * (float(datadisplay.get()) / 100) + float(datadisplay2.get())
        display.set(porcent2)
        expression = str(porcent2)        

#LIMITE DE CARACTERES
def limite():
    le = len(datadisplay.get())    
    if le > 20:
        messagebox.showwarning(title = 'Carácteres', message = 'Você passou o Limite de Carácteres')
 

#BOTÃO CLEAR
def clear():
    global expression
    display.set('0')
    display2.set('')
    display3.set('')
    expression = ''

#BOTÃO BACKSPACE
def backspace():
    global expression
    back  = len(datadisplay.get())
    datadisplay.delete(back-1, 'end')
    expression = datadisplay.get()
    if back == 1:
        datadisplay.insert(0, '0')
        expression = '' 

#TIRA OS OPERADORES DO DISPLAY 
def cleardiplay1():
    global expression
    if '%' or '+' or '*' or '-' or '/' in datadisplay3.get():
        display.set('') 
        expression = ''      
       
#SEPARADOR DE MILHARES////DESENVOLVENDO AINDA
def separador():
    for c in range(len(display.get())):
        f = display.get()
        if c%3 == 0 and c != 0:
            display.set(f + '.')

#============================================DEFS BOTÕES==============================================================

#BOTÕES

bt_7 = PhotoImage(file = 'png/buttons/blackbr/btn_7.png')
botao_7 = Button (janela, text = '7', image = bt_7, height = 85, width = 90, border = 0, command = lambda: [botao(7), limite(),])#fg="white" para mudar a cor do botão
botao_7.place(x = 8, y = 268)

bt_8 = PhotoImage(file = 'png/buttons/blackbr/btn_8.png')
botao_8 = Button (janela, text = '8', image = bt_8, height = 85, width = 90, border = 0, command = lambda: [botao(8), limite()])
botao_8.place(x = 111, y = 269)

bt_9 = PhotoImage(file = 'png/buttons/blackbr/btn_9.png')
botao_9 = Button (janela, text = '9',image = bt_9, height = 85, width = 90, border = 0, command = lambda: [botao(9), limite()])
botao_9.place(x = 214, y = 268)

bt_4  = PhotoImage(file = 'png/buttons/blackbr/btn_4.png')
botao_4 = Button (janela, text = '4', image = bt_4, width = 90, height = 85, border = 0, command = lambda: [botao(4), limite()])
botao_4.place(x = 8, y = 365)

bt_5 = PhotoImage(file = 'png/buttons/blackbr/btn_5.png')
botao_5 = Button (janela, text = '5', image = bt_5, height = 85, width = 90, border = 0, command = lambda: [botao(5), limite()])
botao_5.place(x = 111, y = 365)

bt_6 = PhotoImage(file = 'png/buttons/blackbr/btn_6.png')
botao_6 = Button (janela, text = '6', image = bt_6, height = 85, width = 90, border = 0, command = lambda: [botao(6), limite()])
botao_6.place(x = 215, y = 365)

bt_1 = PhotoImage(file = 'png/buttons/blackbr/btn_1.png')
botao_1 = Button (janela, text = '1', image = bt_1, height = 85, width = 90, border = 0, command = lambda: [botao(1), limite()])
botao_1.place(x = 7, y = 461)

bt_2 = PhotoImage(file = 'png/buttons/blackbr/btn_2.png')
botao_2 = Button (janela, text = '2', image = bt_2, width = 90, height = 85, border = 0, command = lambda: [botao(2), limite()])
botao_2.place(x = 111, y = 461)

bt_3 = PhotoImage(file = 'png/buttons/blackbr/btn_3.png')
botao_3 = Button (janela, text = '3', image = bt_3, height = 85, width = 90, border = 0, command = lambda: [botao(3), limite()])
botao_3.place(x = 214, y = 461)

bt_0 = PhotoImage(file = 'png/buttons/blackbr/btn_0.png')
botao_0 = Button (janela, text = '0', image = bt_0, height = 84, width = 197, border = 0, command = lambda: [botao(0), limite()])
botao_0.place(x = 7, y = 558)

bt_virg = PhotoImage(file = 'png/buttons/blackbr/btn_virg.png')
botao_virgula = Button (janela, text = ',', image = bt_virg, height = 85, width = 90, border = 0, command = lambda: botao('.'))
botao_virgula.place(x = 213, y = 558)

bt_por1 = PhotoImage(file = 'png/buttons/blackbr/btn_por1.png')
botao_porcent = Button (janela, text = '*%', image = bt_por1, height = 43, width = 93, border = 0, command = lambda: [botao('%|'), display_de_cima(), display_do_meio(), cleardiplay1()])
botao_porcent.place(x = 6, y = 171)

bt_por2 = PhotoImage(file = 'png/buttons/blackbr/btn_por2.png')
botao_porcent = Button (janela, text = '+%', image = bt_por2, height = 40, width = 93, border = 0, command = lambda: [botao('%?'), display_de_cima(), display_do_meio(), cleardiplay1()])
botao_porcent.place(x = 6, y = 219)

bt_c = PhotoImage(file = 'png/buttons/blackbr/btn_c.png')
botao_c = Button(janela, text = 'C', image = bt_c, height = 85, width = 90, border = 0,  command = clear)
botao_c.place(x = 213, y = 172)

bt_back = PhotoImage(file = 'png/buttons/blackbr/btn_back.png')
botao_backspace = Button(janela, text = '⌫', image = bt_back, height = 88, width = 125, border = 0, command = backspace)
botao_backspace.place(x = 315, y = 172)

bt_ig = PhotoImage(file = 'png/buttons/blackbr/btn_igual.png')
botao_igual = Button (janela, text = '=', image = bt_ig, height = 87, width = 125, border = 0, command = equação)
botao_igual.place(x = 315, y = 557)

bt_mais = PhotoImage(file = 'png/buttons/blackbr/btn_mais.png')
botao_mais = Button (janela, text = '+', image = bt_mais, height = 87, width = 125, border = 0, command = lambda: [botao('+'), display_de_cima(), display_do_meio(), cleardiplay1()])
botao_mais.place(x = 315, y = 267)

bt_menos = PhotoImage(file = 'png/buttons/blackbr/btn_menos.png')
botao_menos = Button (janela, text = '-', image = bt_menos, height = 87, width = 125, border = 0, command = lambda: [botao('-'), display_de_cima(), display_do_meio(), cleardiplay1()])
botao_menos.place(x = 315, y = 365)

bt_div = PhotoImage(file = 'png/buttons/blackbr/btn_div.png')
botao_div = Button (janela, text = '/', image = bt_div, height = 87, width = 125, border = 0, command = lambda: [botao('/'), display_de_cima(), display_do_meio(), cleardiplay1()])
botao_div.place(x = 315, y = 461)

bt_mult = PhotoImage(file = 'png/buttons/blackbr/btn_mult.png')
botao_mult = Button (janela, text = '*', image = bt_mult, height = 85, width = 90, border = 0, command = lambda: [botao('*'), display_de_cima(), display_do_meio(), cleardiplay1()])
botao_mult.place(x = 110, y = 173)


janela.mainloop()    



#===========================================CÓDIGOS ANTIGOS==============================================

#MODO ANTIGO 
    # try:
    #     global expression
    #     total = str(eval(expression))
    #     display.set(total)
    #     display2.set('')
    #     display3.set('')
    #     expression = total 
    # except:
    #     display.set('Error')
    #     expression = ''             
