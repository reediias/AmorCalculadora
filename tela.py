from tkinter import*
from tkinter import Tk, ttk
from PIL import Image, ImageTk

cor1 = '#FF6347' #vermelho
cor2 = '#FFDEAD' #pessego
cor3 = '#3CB371' #verde
cor4 = '#4682B4' #azul
cor5 = '#FFFFFF' #branco
cor6 = '#000000' #preto
cor7 = '#8A2BE2' #roxo

janela = Tk()
janela.title("")
janela.geometry('410x400')
janela.configure(background=cor1)
janela.resizable(width=False, height=False)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

frameCima = Frame(janela, width=418, height=200, bg=cor2)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=418, height=200, bg=cor2)
frameMeio.grid(row=1, column=0)

tela = Label(frameCima, text="Calculadora do Amor", width=0, padx=3, anchor=NW, font=('Arial 20 bold'), bg=cor2, fg=cor6)
tela.place(x=55, y=0)

def escolher():
    global telaImg, botaoImage

    escolha1 = selecionado1.get()
    escolha2 = selecionado2.get()

    if escolha1 == 'Homem' and escolha2 == 'Homem':
        imagem1 = 'casal2.png'

        telaImg = Image.open(imagem1)
        telaImg = telaImg.resize((120, 120))
        telaImg = ImageTk.PhotoImage(telaImg)
        telaLogo.config(image=telaImg)
        telaLogo.image = telaImg 

    elif escolha1 == 'Homem' and escolha2 == 'Mulher':
        imagem2 = 'casal1.png'

    elif escolha1 == 'Mulher' and escolha2 == 'Mulher':
        imagem3 = 'casal3.png'

    else:
        imagem4 = 'coracao1.png'
        
telaImg = Image.open('coracao1.png')
telaImg = telaImg.resize((120, 120))
telaImg = ImageTk.PhotoImage(telaImg)

telaLogo = Label(frameCima, image = telaImg, width=150, height=140, bg=cor2)
telaLogo.place(x=10, y=50)

resultado2 = Label(frameCima, text="50%", width=3, padx=10, anchor=CENTER, font=('Arial 25 bold'), bg=cor2, fg=cor6)
resultado2.place(x=250, y=100)

nome1 = Label(frameMeio, text="Seu nome",anchor=NW, font=('Arial 10 bold'), bg=cor2, fg=cor6)
nome1.place(x=75, y=10)

enterNome1 = Entry(frameMeio, width=15, font=('Arial 14'), justify='center', relief='solid')
enterNome1.place(x=25, y=40)

nome2 = Label(frameMeio, text="Nome do parceiro(a)",anchor=NW, font=('Arial 10 bold'), bg=cor2, fg=cor6)
nome2.place(x=225, y=10)

enterNome2 = Entry(frameMeio, width=15, font=('Arial 14'), justify='center', relief='solid')
enterNome2.place(x=210, y=40)

selecionado1 = StringVar()

rad1 = Radiobutton(frameMeio, command=escolher, text='Homem', bg=cor2, font=('Arial 10'), value='Homem', variable=selecionado1).place(x=20, y=80)

rad2 = Radiobutton(frameMeio, command=escolher, text='Mulher', bg=cor2, font=('Arial 10'), value='mulher', variable=selecionado1).place(x=20, y=100)

selecionado2 = StringVar()

rad1 = Radiobutton(frameMeio, command=escolher, text='Homem', bg=cor2, font=('Arial 10'), value='Homem', variable=selecionado2).place(x=206, y=80)

rad2 = Radiobutton(frameMeio, command=escolher, text='Mulher', bg=cor2, font=('Arial 10'), value='mulher', variable=selecionado2).place(x=206, y=100)

linha1 = Label(frameMeio, width=0, height=1, anchor=NW, font=('Arial 10'), bg=cor4)
linha1.place(x=195, y=42)

linha2 = Label(frameMeio, width=0, height=1, anchor=NW, font=('Arial 10'), bg=cor4)
linha2.place(x=203, y=42)

botaoImage = Image.open('coracao2.png')
botaoImage = botaoImage.resize((30, 30))
botaoImage = ImageTk.PhotoImage(botaoImage)

calcularBotao = Button(frameMeio, image=botaoImage, width=150, text='Calcular \n Porcentagem'.upper(), height=24, compound=RIGHT, anchor=CENTER, font=('Arial 10 bold'), bg=cor4)
calcularBotao.place(x=120, y=145)

janela.mainloop()