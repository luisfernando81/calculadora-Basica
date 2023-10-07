from tkinter import *

ventana = Tk()
ventana.title("calculadora")
ventana.configure(bg="blue",)
marco = Frame(ventana, bg="black",bd= 22,relief=SUNKEN, )
marco.pack(padx=20, pady= 20)

i=0

e_texto = Entry (marco, font= ("Arial", 30, "italic") )
e_texto.grid(row =0, column= 0, columnspan= 6, padx=5, pady =5)

def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1
    
def borrar():
    e_texto.delete(0, END)
    i=0
    
def opercacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0 
def Back():
    global i 
    i = i-1 
    e_texto.delete(i, END)
def switchBottonState():
        botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton0,
               boton_div, boton_mult, boton_suma, boton_resta, boton_borrar, boton_igual,
               boton_Punto, boton_Parentesis1, boton_Parentesis2, boton_err]

        for boton in botones:
            if boton['state'] == NORMAL:
                boton['state'] = DISABLED
            else:
                boton['state'] = NORMAL

        if boton_abili['text'] == 'abili':
           boton_abili['text'] = 'desabili'
        else:
           boton_abili['text'] = 'abili'
def toggleButtonState():
    if checkbox_var.get() == 1:  # Si el checkbox está marcado
        for widget in marco.winfo_children():
            if isinstance(widget, Button):
                widget.configure(state=NORMAL)
    else:
        for widget in marco.winfo_children():
            if isinstance(widget, Button):
                widget.configure(state=DISABLED)
fuente_personalizada = ("Arial", 12, "italic")
boton1 = Button(marco, text="1", width=5, height=2,state=DISABLED, command = lambda: click_boton(1), bg ="white",font = fuente_personalizada )
boton2 = Button(marco, text="2", width=5, height=2,state=DISABLED, command = lambda: click_boton(2), bg ="white",font = fuente_personalizada )
boton3 = Button(marco, text="3", width=5, height=2,state=DISABLED, command = lambda: click_boton(3), bg ="white",font = fuente_personalizada )
boton4 = Button(marco, text="4", width=5, height=2,state=DISABLED, command = lambda: click_boton(4), bg ="white", font = fuente_personalizada)
boton5 = Button(marco, text="5", width=5, height=2,state=DISABLED, command = lambda: click_boton(5), bg ="white",font = fuente_personalizada )
boton6 = Button(marco, text="6", width=5, height=2,state=DISABLED, command = lambda: click_boton(6), bg ="white",font = fuente_personalizada )
boton7 = Button(marco, text="7", width=5, height=2,state=DISABLED, command = lambda: click_boton(7), bg ="white",font = fuente_personalizada )
boton8 = Button(marco, text="8", width=5, height=2,state=DISABLED, command = lambda: click_boton(8), bg ="white",font = fuente_personalizada )
boton9 = Button(marco, text="9", width=5, height=2,state=DISABLED, command = lambda: click_boton(9), bg ="white",font = fuente_personalizada )
boton0 = Button(marco, text="0", width=13, height=2,state=DISABLED, command = lambda: click_boton(0), bg ="white",font = fuente_personalizada )

boton_borrar = Button(marco, text="AC", width=5, height=2,state=DISABLED, command = lambda: borrar(), bg ="red",font = fuente_personalizada)
boton_err = Button(marco, text="c", width=5, height=2,state=DISABLED, command = lambda: Back())
boton_Parentesis1 = Button(marco, text="(", width=5, height=2,state=DISABLED, command = lambda: click_boton("("))
boton_Parentesis2 = Button(marco, text=")", width=5, height=2,state=DISABLED, command = lambda: click_boton(")"))
boton_Punto = Button(marco, text=".", width=5, height=2,state=DISABLED, command = lambda: click_boton("."))

boton_div = Button(marco, text="/", width=5, height=2,state=DISABLED, command = lambda: click_boton("/"))
boton_mult = Button(marco, text="x", width=5, height=2,state=DISABLED, command = lambda: click_boton("*"))
boton_suma = Button(marco, text="+", width=5, height=7,state=DISABLED, command = lambda: click_boton("+"))
boton_resta = Button(marco, text="-", width=5, height=2,state=DISABLED, command = lambda: click_boton("-"))
boton_igual = Button(marco, text="=", width=5, height=2,state=DISABLED, command = lambda: opercacion())
boton_abili = Button(marco, text="abili", width=5, height=2, command = lambda: switchBottonState(),font = fuente_personalizada)
checkbox_var = IntVar()
checkbox = Checkbutton(marco, text="ON/OFF", variable=checkbox_var, onvalue=1, offvalue=0, command=toggleButtonState, bg='blue')

checkbox.grid(row=5, column=5, padx=5, pady=5, sticky="e")
boton_borrar.grid(row =1, column= 0, padx = 5, pady = 5)
boton_Parentesis1.grid(row =1, column= 2, padx = 5, pady = 5)
boton_Parentesis2.grid(row =1, column= 3, padx = 5, pady = 5)
boton_div.grid(row =3, column= 5, padx = 5, pady = 5)

boton7.grid(row =2, column= 0, padx=5, pady =5)
boton8.grid(row =2, column= 1, padx=5, pady =5)
boton9.grid(row =2, column= 2, padx=5, pady =5)
boton_mult.grid(row =2, column= 3, padx=5, pady =5)

boton4.grid(row =3, column= 0, padx=5, pady =5)
boton5.grid(row =3, column= 1, padx=5, pady =5)
boton6.grid(row =3, column= 2, padx=5, pady =5)
boton_suma.grid(row =3, column= 3,rowspan=2, padx=5, pady =5)

boton1.grid(row =4, column= 0, padx=5, pady =5)
boton2.grid(row =4, column= 1, padx=5, pady =5)
boton3.grid(row =4, column= 2, padx=5, pady =5)
boton_resta.grid(row =4, column= 5, padx=5, pady =5)

boton0.grid(row =5, column= 0,columnspan=2, padx=5, pady =5)
boton_err.grid(row =1,column=1, padx=5, pady =5)
boton_Punto.grid(row =5, column= 2, padx=5, pady =5)
boton_igual.grid(row =5, column= 3, padx=5, pady =5)
boton_abili. grid(row =1,column=5, padx=5, pady =5)

ventana.mainloop() 