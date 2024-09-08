from tkinter import *

#Configuração da Janela:
janela = Tk()
#janela.geometry("400x400")
janela.title("Calculadora")

#Variaveis de Cores:
preto="black"
laraja="#FE5F2F"
cinza="#ccc"

#Display de numeros:
textoDeEntrada = StringVar()

displayDeNumeros = Entry(
    janela,
    font=("Arial 20 bold"),
    textvariable=textoDeEntrada,
    border=5,
    bg="#BBB",
    fg="black"
).grid(row=1, columnspan=5, padx=10, pady=15)


#Buttons da linha 1:
btn7 = Button(
    janela,
    font="Arial 20",
    text="7",
    border=10,
    bg=cinza,
    fg=preto,

).grid(row=2, column=0, padx=0,pady=0)

btn8 = Button(
    janela,
    font="Arial 20",
    text="8",
    border=10,
    bg=cinza,
    fg=preto,

).grid(row=2, column=1, padx=0,pady=0)

btn9 = Button(
    janela,
    font="Arial 20",
    text="9",
    border=10,
    bg=cinza,
    fg=preto,

).grid(row=2, column=2, padx=0,pady=0)

btnDEL = Button(
    janela,
    font="Arial 20 bold",
    text="DEL",
    border=10,
    bg=laraja,
    fg=preto,
    width=3
).grid(row=2, column=3, padx=0,pady=0)

btnAC = Button(
    janela,
    font="Arial 20 bold",
    text="AC",
    border=10,
    bg=laraja,
    fg=preto,
    width=3
).grid(row=2, column=4, padx=0,pady=0)

#Buttons da linha 2:
btn4 = Button(
    janela,
    font="Arial 20",
    text="4",
    border=10,
    bg=cinza,
    fg=preto,

).grid(row=3, column=0, padx=0,pady=0)

btn5 = Button(
    janela,
    font="Arial 20",
    text="5",
    border=10,
    bg=cinza,
    fg=preto,

).grid(row=3, column=1, padx=0,pady=0)

btn6 = Button(
    janela,
    font="Arial 20",
    text="6",
    border=10,
    bg=cinza,
    fg=preto,

).grid(row=3, column=2, padx=0,pady=0)

btnMultiplica = Button(
    janela,
    font="Arial 20 bold",
    text="*",
    border=10,
    bg=cinza,
    fg=preto,
    width=3
).grid(row=3, column=3, padx=0,pady=0)

btnDividi = Button(
    janela,
    font="Arial 20 bold",
    text="/",
    border=10,
    bg=cinza,
    fg=preto,
    width=3
).grid(row=3, column=4, padx=0,pady=0)


#Buttons da linha 3:
btn1 = Button(
    janela,
    font="Arial 20",
    text="1",
    border=10,
    bg=cinza,
    fg=preto,

).grid(row=4, column=0, padx=0,pady=0)

btn2 = Button(
    janela,
    font="Arial 20",
    text="2",
    border=10,
    bg=cinza,
    fg=preto,

).grid(row=4, column=1, padx=0,pady=0)

btn3 = Button(
    janela,
    font="Arial 20",
    text="3",
    border=10,
    bg=cinza,
    fg=preto,

).grid(row=4, column=2, padx=0,pady=0)

btnMultiplica = Button(
    janela,
    font="Arial 20 bold",
    text="+",
    border=10,
    bg=cinza,
    fg=preto,
    width=3
).grid(row=4, column=3, padx=0,pady=0)

btnMenos = Button(
    janela,
    font="Arial 20 bold",
    text="-",
    border=10,  
    bg=cinza,
    fg=preto,
    width=3
).grid(row=4, column=4, padx=0,pady=0)

#Buttons da linha 4:
btn0 = Button(
    janela,
    font="Arial 20",
    text="0",
    border=10,
    bg=cinza,
    fg=preto,
    width=1
).grid(row=5, column=0, padx=0,pady=0)

btnPonto = Button(
    janela,
    font="Arial 20",
    text=".",
    border=10,
    bg=cinza,
    fg=preto,
    width=1
).grid(row=5, column=1, padx=0,pady=0)

btnValor = Button(
    janela,
    font="Arial 20 bold",
    text="=",
    border=10,
    bg=cinza,
    fg=preto,
    width=13
).grid(row=5, column=2,columnspan=4, padx=0,pady=0)


#Loop do Janela e Start;
janela.mainloop()