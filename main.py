from tkinter import *

#Configuração da Janela:
janela = Tk()
#janela.geometry("400x400")
janela.title("Calculadora")

#Variaveis de Cores:
preto="black"
laraja="#FE5F2F"
cinza="#ccc"
calculoOperacoes=""
#Lógica da Calculadora:

def enviarNumeroPara(char):
    global calculoOperacoes
    calculoOperacoes+=str(char)
    textoDeEntrada.set(calculoOperacoes)


def deletarNumero():
    global calculoOperacoes
    texto = calculoOperacoes[:-1]#Remover o ultimo elemento da String;
    calculoOperacoes=texto #Atualizar a variavel novamente com outro valor;
    textoDeEntrada.set(calculoOperacoes)

def limparDisplay():
    global calculoOperacoes
    calculoOperacoes=""
    textoDeEntrada.set(calculoOperacoes)

def funcaoIgual():
    global calculoOperacoes
    resultadoCalculo=str(eval(calculoOperacoes))
    textoDeEntrada.set(resultadoCalculo)
    calculoOperacoes=resultadoCalculo


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
    command=lambda:enviarNumeroPara("7")

).grid(row=2, column=0, padx=0,pady=0, sticky="NSEW")

btn8 = Button(
    janela,
    font="Arial 20",
    text="8",
    border=10,
    bg=cinza,
    fg=preto,
    command=lambda:enviarNumeroPara("8")

).grid(row=2, column=1, padx=0,pady=0, sticky="NSEW")

btn9 = Button(
    janela,
    font="Arial 20",
    text="9",
    border=10,
    bg=cinza,
    fg=preto,
    command=lambda:enviarNumeroPara("9")

).grid(row=2, column=2, padx=0,pady=0, sticky="NSEW")

btnDEL = Button(
    janela,
    font="Arial 20 bold",
    text="DEL",
    border=10,
    bg=laraja,
    fg=preto,
    width=3,
    command=deletarNumero
).grid(row=2, column=3, padx=0,pady=0, sticky="NSEW")

btnAC = Button(
    janela,
    font="Arial 20 bold",
    text="AC",
    border=10,
    bg=laraja,
    fg=preto,
    width=3,
    command=limparDisplay
).grid(row=2, column=4, padx=0,pady=0, sticky="NSEW")

#Buttons da linha 2:
btn4 = Button(
    janela,
    font="Arial 20",
    text="4",
    border=10,
    bg=cinza,
    fg=preto,
    command=lambda:enviarNumeroPara("4")

).grid(row=3, column=0, padx=0,pady=0, sticky="NSEW")

btn5 = Button(
    janela,
    font="Arial 20",
    text="5",
    border=10,
    bg=cinza,
    fg=preto,
    command=lambda:enviarNumeroPara("5")

).grid(row=3, column=1, padx=0,pady=0, sticky="NSEW")

btn6 = Button(
    janela,
    font="Arial 20",
    text="6",
    border=10,
    bg=cinza,
    fg=preto,
    command=lambda:enviarNumeroPara("6")

).grid(row=3, column=2, padx=0,pady=0, sticky="NSEW")

btnMultiplica = Button(
    janela,
    font="Arial 20 bold",
    text="*",
    border=10,
    bg=cinza,
    fg=preto,
    width=3,
    command=lambda:enviarNumeroPara("*")
).grid(row=3, column=3, padx=0,pady=0, sticky="NSEW")

btnDividi = Button(
    janela,
    font="Arial 20 bold",
    text="/",
    border=10,
    bg=cinza,
    fg=preto,
    width=3,
    command=lambda:enviarNumeroPara("/")
).grid(row=3, column=4, padx=0,pady=0, sticky="NSEW")


#Buttons da linha 3:
btn1 = Button(
    janela,
    font="Arial 20",
    text="1",
    border=10,
    bg=cinza,
    fg=preto,
    command=lambda:enviarNumeroPara("1")

).grid(row=4, column=0, padx=0,pady=0, sticky="NSEW")

btn2 = Button(
    janela,
    font="Arial 20",
    text="2",
    border=10,
    bg=cinza,
    fg=preto,
    command=lambda:enviarNumeroPara("2")

).grid(row=4, column=1, padx=0,pady=0, sticky="NSEW")

btn3 = Button(
    janela,
    font="Arial 20",
    text="3",
    border=10,
    bg=cinza,
    fg=preto,
    command=lambda:enviarNumeroPara("3")

).grid(row=4, column=2, padx=0,pady=0, sticky="NSEW")

btnSomar = Button(
    janela,
    font="Arial 20 bold",
    text="+",
    border=10,
    bg=cinza,
    fg=preto,
    width=3,
    command=lambda:enviarNumeroPara("+")
).grid(row=4, column=3, padx=0,pady=0, sticky="NSEW")

btnMenos = Button(
    janela,
    font="Arial 20 bold",
    text="-",
    border=10,  
    bg=cinza,
    fg=preto,
    width=3,
    command=lambda:enviarNumeroPara("-")
).grid(row=4, column=4, padx=0,pady=0, sticky="NSEW")

#Buttons da linha 4:
btn0 = Button(
    janela,
    font="Arial 20",
    text="0",
    border=10,
    bg=cinza,
    fg=preto,
    width=1,
    command=lambda:enviarNumeroPara("0")
).grid(row=5, column=0, padx=0,pady=0, sticky="NSEW")

btnPonto = Button(
    janela,
    font="Arial 20",
    text=".",
    border=10,
    bg=cinza,
    fg=preto,
    width=1,
    command=lambda:enviarNumeroPara(".")
).grid(row=5, column=1, padx=0,pady=0, sticky="NSEW")

btnValor = Button(
    janela,
    font="Arial 20 bold",
    text="=",
    border=10,
    bg=cinza,
    fg=preto,
    width=13,
    command=funcaoIgual
).grid(row=5, column=2,columnspan=4, padx=0,pady=0, sticky="NSEW")


#Loop do Janela e Start;
janela.mainloop()