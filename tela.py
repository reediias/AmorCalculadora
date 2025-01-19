from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

# Função de cálculo
def calculo():
    global resultado

    nome1 = enterNome1.get()
    nome2 = enterNome2.get()

    if not nome1 or not nome2:
        resultado.config(text="Preencha\n os\n campos\n !")
        return

    pontuacao = 0

    if pergunta1_var.get() == 'Sim':
        pontuacao += 10
    if pergunta2_var.get() == 'Sim':
        pontuacao += 10
    if pergunta3_var.get() == 'Sim':
        pontuacao += 10
    if pergunta4_var.get() == 'Sim':
        pontuacao += 10

    if pergunta1_var.get() == 'Não':
        pontuacao -= 5
    if pergunta2_var.get() == 'Não':
        pontuacao -= 5
    if pergunta3_var.get() == 'Não':
        pontuacao -= 5
    if pergunta4_var.get() == 'Não':
        pontuacao -= 5

    compatibilidade = min(100, max(0, pontuacao + random.randint(0, 20)))
    resultado.config(text=f'{compatibilidade}%')

# Função de escolher as imagens
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
            botaoImage = Image.open('coracao1.png')
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

cor1 = '#D32F2F'  # vermelho
cor2 = '#FFDEAD'  # pêssego
cor3 = '#FFFFFF'  # branco
cor4 = '#000000'  # preto

janela = Tk()
janela.title("Calculadora do Amor")
janela.geometry('410x600')  # Ajuste a altura da janela para acomodar as perguntas
janela.configure(background=cor1)
janela.resizable(width=False, height=False)

# Frame principal
frameCima = Frame(janela, width=418, height=200, bg=cor1)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=418, height=400, bg=cor1)  # Aumentei a altura para acomodar perguntas
frameMeio.grid(row=1, column=0)

# Título na tela principal
tela = Label(frameCima, text="Calculadora do Amor", width=0, padx=3, anchor=NW, font=('Arial 20 bold'), bg=cor1, fg=cor4)
tela.place(x=55, y=10)

# Logo
telaImg = Image.open('coracao1.png')
telaImg = telaImg.resize((120, 120))
telaImg = ImageTk.PhotoImage(telaImg)

telaLogo = Label(frameCima, image=telaImg, width=150, height=140, bg=cor1)
telaLogo.place(x=10, y=50)

# Resultado
resultado = Label(frameCima, text="", width=10, padx=10, anchor=CENTER, font=('Arial 20 bold'), bg=cor1, fg=cor4)
resultado.place(x=180, y=60)

# Entradas de nome
nome1 = Label(frameMeio, text="Seu nome", anchor=NW, font=('Arial 12 bold'), bg=cor1, fg=cor4)
nome1.place(x=70, y=10)

enterNome1 = Entry(frameMeio, width=15, font=('Arial 14'), justify='center', relief='solid')
enterNome1.place(x=25, y=40)

nome2 = Label(frameMeio, text="Nome do parceiro(a)", anchor=NW, font=('Arial 12 bold'), bg=cor1, fg=cor4)
nome2.place(x=216, y=10)

enterNome2 = Entry(frameMeio, width=15, font=('Arial 14'), justify='center', relief='solid')
enterNome2.place(x=210, y=40)

# Opções de gênero
selecionado1 = StringVar()
rad1 = Radiobutton(frameMeio, command=escolher, text='Homem', bg=cor1, font=('Arial 12 bold'), value='Homem', variable=selecionado1)
rad1.place(x=20, y=80)

rad2 = Radiobutton(frameMeio, command=escolher, text='Mulher', bg=cor1, font=('Arial 12 bold'), value='Mulher', variable=selecionado1)
rad2.place(x=20, y=100)

selecionado2 = StringVar()
rad3 = Radiobutton(frameMeio, command=escolher, text='Homem', bg=cor1, font=('Arial 12 bold'), value='Homem', variable=selecionado2)
rad3.place(x=206, y=80)

rad4 = Radiobutton(frameMeio, command=escolher, text='Mulher', bg=cor1, font=('Arial 12 bold'), value='Mulher', variable=selecionado2)
rad4.place(x=206, y=100)

linha1 = Label(frameMeio, width=0, height=1, anchor=NW, font=('Arial 10'), bg=cor1)
linha1.place(x=195, y=42)

linha2 = Label(frameMeio, width=0, height=1, anchor=NW, font=('Arial 10'), bg=cor1)
linha2.place(x=203, y=42)

# Perguntas
pergunta1 = Label(frameMeio, text='Vocês acreditam em amor à primeira vista?', bg=cor1, fg=cor4, font=('Arial 12'))
pergunta1.place(x=70, y=140)

pergunta1_var = StringVar()
pergunta1sim = Radiobutton(frameMeio, text="Sim", bg=cor1, font=('Arial 12 bold'), value="Sim", variable=pergunta1_var)
pergunta1sim.place(x=70, y=180)
pergunta1nao = Radiobutton(frameMeio, text="Não", bg=cor1, font=('Arial 12 bold'), value="Não", variable=pergunta1_var)
pergunta1nao.place(x=150, y=180)

pergunta2 = Label(frameMeio, text='Vocês gostam de sair para festas e baladas?', bg=cor1, fg=cor4, font=('Arial 12'))
pergunta2.place(x=70, y=220)

pergunta2_var = StringVar()
pergunta2sim = Radiobutton(frameMeio, text="Sim", bg=cor1, font=('Arial 12 bold'), value="Sim", variable=pergunta2_var)
pergunta2sim.place(x=70, y=260)
pergunta2nao = Radiobutton(frameMeio, text="Não", bg=cor1, font=('Arial 12 bold'), value="Não", variable=pergunta2_var)
pergunta2nao.place(x=150, y=260)

pergunta3 = Label(frameMeio, text='Vocês têm hobbies ou interesses em comum?', bg=cor1, fg=cor4, font=('Arial 12'))
pergunta3.place(x=70, y=300)

pergunta3_var = StringVar()
pergunta3sim = Radiobutton(frameMeio, text="Sim", bg=cor1, font=('Arial 12 bold'), value="Sim", variable=pergunta3_var)
pergunta3sim.place(x=70, y=340)
pergunta3nao = Radiobutton(frameMeio, text="Não", bg=cor1, font=('Arial 12 bold'), value="Não", variable=pergunta3_var)
pergunta3nao.place(x=150, y=340)

pergunta4 = Label(frameMeio, text='Vocês concordam em muitas decisões importantes?', bg=cor1, fg=cor4, font=('Arial 12'))
pergunta4.place(x=70, y=380)

pergunta4_var = StringVar()
pergunta4sim = Radiobutton(frameMeio, text="Sim", bg=cor1, font=('Arial 12 bold'), value="Sim", variable=pergunta4_var)
pergunta4sim.place(x=70, y=420)
pergunta4nao = Radiobutton(frameMeio, text="Não", bg=cor1, font=('Arial 12 bold'), value="Não", variable=pergunta4_var)
pergunta4nao.place(x=150, y=420)

# Botão para calcular resultado
botaoImage = Image.open('coracao1.png')
botaoImage = botaoImage.resize((30, 30))
botaoImage = ImageTk.PhotoImage(botaoImage)

calcularBotao = Button(frameMeio, command=calculo, image=botaoImage, width=150, text='Calcular \n Porcentagem'.upper(), height=24, compound=RIGHT, anchor=CENTER, font=('Arial 10 bold'), bg=cor3)
calcularBotao.place(x=120, y=460)

janela.mainloop()
