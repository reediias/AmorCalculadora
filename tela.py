from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
import random

def calculo():
    global calcularBotao, selecionado1, selecionado2, resultado

    if selecionado1.get() != '' and selecionado2.get() != '':
        porc = '0123456789'
        dig = 2
        resultado2_gerado = ''.join(random.sample(porc, dig))
        print(resultado2_gerado)
        resultado.config(text=resultado2_gerado + '%')

def escolher():
    global telaImg, botaoImage

    escolha1 = selecionado1.get() 
    escolha2 = selecionado2.get()

    imagem = None 
    lgbtimagem = None

    if escolha1 == 'Homem' and escolha2 == 'Homem':
        imagem = 'casal2.png'
        lgbtimagem = 'coracaolgbt.png'

    elif escolha1 == 'Mulher' and escolha2 == 'Mulher':
        imagem = 'casal3.png'
        lgbtimagem = 'coracaolgbt.png'

    elif escolha1 == 'Homem' and escolha2 == 'Mulher':
        imagem = 'casal1.png'

    elif escolha1 == 'Mulher' and escolha2 == 'Homem':
        imagem = 'casal1.png'

    if imagem is not None:

        telaImg = Image.open(imagem)
        telaImg = telaImg.resize((120, 120)) 
        telaImg = ImageTk.PhotoImage(telaImg)

        telaLogo.config(image=telaImg)
        telaLogo.image = telaImg 

        if lgbtimagem:
            botaoImage = Image.open(lgbtimagem)
            botaoImage = botaoImage.resize((30, 30))
            botaoImage = ImageTk.PhotoImage(botaoImage)

            calcularBotao.config(image=botaoImage)
            calcularBotao.image = botaoImage

        else:
            botaoImage = Image.open('coracao2.png')
            botaoImage = botaoImage.resize((30, 30))
            botaoImage = ImageTk.PhotoImage(botaoImage)

            calcularBotao.config(image=botaoImage) 
            calcularBotao.image = botaoImage
    else:
        telaImg = Image.open('coracao1.png')
        telaImg = telaImg.resize((120, 120))
        telaImg = ImageTk.PhotoImage(telaImg)
        
        telaLogo.config(image=telaImg)
        telaLogo.image = telaImg

cor1 = '#D32F2F'#vermelho
cor2 = '#FFDEAD' #pessego
cor3 = '#FFFFFF' #branco
cor4 = '#000000' #preto

janela = Tk()
janela.title("")
janela.geometry('410x400')
janela.configure(background=cor1)
janela.resizable(width=False, height=False)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

frameCima = Frame(janela, width=418, height=200, bg=cor1)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=418, height=200, bg=cor1)
frameMeio.grid(row=1, column=0)

tela = Label(frameCima, text="Calculadora do Amor", width=0, padx=3, anchor=NW, font=('Arial 20 bold'), bg=cor1, fg=cor4)
tela.place(x=55, y=10)

telaImg = Image.open('coracao1.png')
telaImg = telaImg.resize((120, 120))
telaImg = ImageTk.PhotoImage(telaImg)

telaLogo = Label(frameCima, image=telaImg, width=150, height=140, bg=cor1)
telaLogo.place(x=10, y=50)

resultado = Label(frameCima, text="50%", width=3, padx=10, anchor=CENTER, font=('Arial 25 bold'), bg=cor1, fg=cor4)
resultado.place(x=250, y=100)

nome1 = Label(frameMeio, text="Seu nome", anchor=NW, font=('Arial 12 bold'), bg=cor1, fg=cor4)
nome1.place(x=70, y=10)

enterNome1 = Entry(frameMeio, width=15, font=('Arial 14'), justify='center', relief='solid')
enterNome1.place(x=25, y=40)

nome2 = Label(frameMeio, text="Nome do parceiro(a)", anchor=NW, font=('Arial 12 bold'), bg=cor1, fg=cor4)
nome2.place(x=216, y=10)

enterNome2 = Entry(frameMeio, width=15, font=('Arial 14'), justify='center', relief='solid')
enterNome2.place(x=210, y=40)

selecionado1 = StringVar()

rad1 = Radiobutton(frameMeio, command=escolher, text='Homem', bg=cor1, font=('Arial 12 bold'), value='Homem', variable=selecionado1).place(x=20, y=80)

rad2 = Radiobutton(frameMeio, command=escolher, text='Mulher', bg=cor1, font=('Arial 12 bold'), value='Mulher', variable=selecionado1).place(x=20, y=100)

selecionado2 = StringVar()

rad3 = Radiobutton(frameMeio, command=escolher, text='Homem', bg=cor1, font=('Arial 12 bold'), value='Homem', variable=selecionado2).place(x=206, y=80)

rad4 = Radiobutton(frameMeio, command=escolher, text='Mulher', bg=cor1, font=('Arial 12 bold'), value='Mulher', variable=selecionado2).place(x=206, y=100)

linha1 = Label(frameMeio, width=0, height=1, anchor=NW, font=('Arial 10'), bg=cor1)
linha1.place(x=195, y=42)

linha2 = Label(frameMeio, width=0, height=1, anchor=NW, font=('Arial 10'), bg=cor1)
linha2.place(x=203, y=42)

botaoImage = Image.open('coracao1.png')
botaoImage = botaoImage.resize((30, 30))
botaoImage = ImageTk.PhotoImage(botaoImage)

calcularBotao = Button(frameMeio, command=calculo, image=botaoImage, width=150, text='Calcular \n Porcentagem'.upper(), height=24, compound=RIGHT, anchor=CENTER, font=('Arial 10 bold'), bg=cor3)
calcularBotao.place(x=120, y=145)

janela.mainloop()
