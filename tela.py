from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

# Definindo as cores
cor1 = '#D32F2F'  # vermelho
cor2 = '#FFDEAD'  # pêssego
cor3 = '#FFFFFF'  # branco
cor4 = '#000000'  # preto

def tela1():
    janela = Tk()
    janela.title("Calculadora do Amor")
    janela.geometry('500x500')
    janela.configure(background=cor1)
    janela.resizable(width=False, height=False)

    estilo = ttk.Style(janela)
    estilo.theme_use('clam')

    frameCima = Frame(janela, width=418, height=200, bg=cor1)
    frameCima.grid(row=0, column=0)

    frameMeio = Frame(janela, width=418, height=200, bg=cor1)
    frameMeio.grid(row=1, column=0)

    tela = Label(frameCima, text="Calculadora do Amor", width=0, padx=3, anchor=NW, font=('Arial 20 bold'), bg=cor1, fg=cor4)
    tela.place(x=100, y=20)

    telaImg = Image.open('coracao1.png')
    telaImg = telaImg.resize((140, 140))
    telaImg = ImageTk.PhotoImage(telaImg)

    telaLogo = Label(frameCima, image=telaImg, width=150, height=140, bg=cor1)
    telaLogo.place(x=160, y=70)

    nome1 = Label(frameMeio, text="Seu nome", anchor=NW, font=('Arial 12 bold'), bg=cor1, fg=cor4)
    nome1.place(x=115, y=50)

    enterNome1 = Entry(frameMeio, width=15, font=('Arial 14'), justify='center', relief='solid')
    enterNome1.place(x=70, y=80)

    nome2 = Label(frameMeio, text="Nome do parceiro(a)", anchor=NW, font=('Arial 12 bold'), bg=cor1, fg=cor4)
    nome2.place(x=255, y=50)

    enterNome2 = Entry(frameMeio, width=15, font=('Arial 14'), justify='center', relief='solid')
    enterNome2.place(x=250, y=80)

    if enterNome1 == None and enterNome2 == None:
        return tela1()

    selecionado1 = StringVar()

    rad1 = Radiobutton(frameMeio, text='Homem', bg=cor1, font=('Arial 12 bold'), value='Homem', variable=selecionado1).place(x=65, y=120)

    rad2 = Radiobutton(frameMeio, text='Mulher', bg=cor1, font=('Arial 12 bold'), value='Mulher', variable=selecionado1).place(x=65, y=150)

    selecionado2 = StringVar()

    rad3 = Radiobutton(frameMeio, text='Homem', bg=cor1, font=('Arial 12 bold'), value='Homem', variable=selecionado2).place(x=245, y=120)

    rad4 = Radiobutton(frameMeio, text='Mulher', bg=cor1, font=('Arial 12 bold'), value='Mulher', variable=selecionado2).place(x=245, y=150)

    def atualizarImagem():

        escolha1 = selecionado1.get()
        escolha2 = selecionado2.get()

        if escolha1 == 'Homem' and escolha2 == 'Mulher':
            telaImg = Image.open('casal1.png')

        elif escolha1 == 'Mulher' and escolha2 == 'Homem':
            telaImg = Image.open('casal1.png')

        elif escolha1 == 'Homem' and escolha2 == 'Homem':
            telaImg = Image.open('casal2.png')

        elif escolha1 == 'Mulher' and escolha2 == 'Mulher':
            telaImg = Image.open('casal3.png')

        else:
            telaImg = Image.open('coracao1.png')
        
        telaImg = telaImg.resize((140, 140))
        telaImg = ImageTk.PhotoImage(telaImg)
        telaLogo.config(image=telaImg)
        telaLogo.image = telaImg

    selecionado1.trace("w", lambda *args: atualizarImagem())
    selecionado2.trace("w", lambda *args: atualizarImagem())

    def irParaPerguntas():

        nome1Valor = enterNome1.get().strip()
        nome2Valor = enterNome2.get().strip()

        if not nome1Valor or not nome2Valor:

            msg = Label(janela, text="Por favor, preencha os campos!", font=('Arial 12 bold'), bg=cor1, fg=cor4)
            msg.place(x=105, y= 460)

            return

        janela.destroy()
        tela2(selecionado1.get(), selecionado2.get())

    botaoPerguntas = Button(janela, text="Ir para perguntas", command=irParaPerguntas, font=('Arial 12 bold'), bg=cor3, fg=cor4)
    botaoPerguntas.place(x=182, y=410)

    janela.mainloop()

def tela2(escolha1, escolha2):

    janela2 = Tk()
    janela2.title("Perguntas")
    janela2.geometry('500x500')
    janela2.configure(background=cor1)
    janela2.resizable(width=False, height=False)

    frameCima = Frame(janela2, width=418, height=200, bg=cor1)
    frameCima.grid(row=0, column=0)

    frameMeio = Frame(janela2, width=418, height=200, bg=cor1)
    frameMeio.grid(row=1, column=0)

    global pergunta1_var, pergunta2_var, pergunta3_var, pergunta4_var

    pergunta1 = Label(janela2, text='Vocês acreditam em amor à primeira vista?', bg=cor1, fg=cor4, font=('Arial 12'))
    pergunta1.place(x=70, y=60)

    pergunta1_var = StringVar()
    pergunta1sim = Radiobutton(janela2, text="Sim", bg=cor1, font=('Arial 12 bold'), value="Sim", variable=pergunta1_var)
    pergunta1sim.place(x=70, y=95)

    pergunta1nao = Radiobutton(janela2, text="Não", bg=cor1, font=('Arial 12 bold'), value="Não", variable=pergunta1_var)
    pergunta1nao.place(x=150, y=95)

    pergunta2 = Label(janela2, text='Vocês gostam de sair para festas e baladas?', bg=cor1, fg=cor4, font=('Arial 12'))
    pergunta2.place(x=70, y=140)

    pergunta2_var = StringVar()
    pergunta2sim = Radiobutton(janela2, text="Sim", bg=cor1, font=('Arial 12 bold'), value="Sim", variable=pergunta2_var)
    pergunta2sim.place(x=70, y=175)

    pergunta2nao = Radiobutton(janela2, text="Não", bg=cor1, font=('Arial 12 bold'), value="Não", variable=pergunta2_var)
    pergunta2nao.place(x=150, y=175)

    pergunta3 = Label(janela2, text='Vocês têm hobbies ou interesses em comum?', bg=cor1, fg=cor4, font=('Arial 12'))
    pergunta3.place(x=70, y=220)

    pergunta3_var = StringVar()
    pergunta3sim = Radiobutton(janela2, text="Sim", bg=cor1, font=('Arial 12 bold'), value="Sim", variable=pergunta3_var)
    pergunta3sim.place(x=70, y=255)

    pergunta3nao = Radiobutton(janela2, text="Não", bg=cor1, font=('Arial 12 bold'), value="Não", variable=pergunta3_var)
    pergunta3nao.place(x=150, y=255)

    pergunta4 = Label(janela2, text='Vocês concordam em muitas decisões importantes?', bg=cor1, fg=cor4, font=('Arial 12'))
    pergunta4.place(x=70, y=300)

    pergunta4_var = StringVar()
    pergunta4sim = Radiobutton(janela2, text="Sim", bg=cor1, font=('Arial 12 bold'), value="Sim", variable=pergunta4_var)
    pergunta4sim.place(x=70, y=340)

    pergunta4nao = Radiobutton(janela2, text="Não", bg=cor1, font=('Arial 12 bold'), value="Não", variable=pergunta4_var)
    pergunta4nao.place(x=150, y=340)

    def irParaResultado():
        janela2.destroy()
        tela3()

    botao_respostas = Button(janela2, text="Enviar Respostas", command=irParaResultado, font=('Arial 12 bold'), bg=cor3, fg=cor4)
    botao_respostas.place(x=182, y=415)

    janela2.mainloop()

def tela3():

    janela3 = Tk()
    janela3.title("Calculando compatibilidade")
    janela3.geometry('500x500')
    janela3.configure(background=cor1)
    janela3.resizable(width=False, height=False)

    frameCima = Frame(janela3, width=418, height=200, bg=cor1)
    frameCima.grid(row=0, column=0)

    frameMeio = Frame(janela3, width=418, height=200, bg=cor1)
    frameMeio.grid(row=1, column=0)

    tela = Label(frameCima, text="A compatibilidade \n entre vocês é:", width=0, padx=3, anchor=NW, font=('Arial 20 bold'), bg=cor3, fg=cor4)
    tela.place(x=115, y=30)

    resultado = Label(frameCima, text='0%', width=10, padx=10, anchor=CENTER, font=('Arial 20 bold'), bg=cor1, fg=cor4)
    resultado.place(x=150, y=120)

    pontuacao = 0

    if pergunta1_var.get() == 'Sim':
        pontuacao += 20
    if pergunta2_var.get() == 'Sim':
        pontuacao += 20
    if pergunta3_var.get() == 'Sim':
        pontuacao += 20
    if pergunta4_var.get() == 'Sim':
        pontuacao += 20

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

    if compatibilidade < 40:
        imagemResultado = Image.open('triste.png')
        textoResultado1 = 'Acho que vocês não têm muito em comum!' 

    elif compatibilidade > 40 and compatibilidade <= 70:
        imagemResultado = Image.open('medio.png')
        textoResultado2 = 'Vá em frente!' 

    elif compatibilidade > 70 and compatibilidade <= 100:
        imagemResultado = Image.open('feliz.png')
        textoResultado3 = 'Vocês são um casal perfeito!'

    imagemResultado = imagemResultado.resize((140, 140))
    imagemResultado = ImageTk.PhotoImage(imagemResultado)

    imagemLabel = Label(frameMeio, image=imagemResultado, bg=cor1)
    imagemLabel.place(x=180, y=5)

    imagemLabel.image = imagemResultado

    textoLabel1 = Label(frameMeio, text=textoResultado1, font=('Arial 12 bold'), bg=cor1, fg=cor4)
    textoLabel1.place(x=80, y=170)

    textoLabel2 = Label(frameMeio, text=textoResultado2, font=('Arial 12 bold'), bg=cor1, fg=cor4)
    textoLabel2.place(x=100, y=170)

    textoLabel3 = Label(frameMeio, text=textoResultado3, font=('Arial 12 bold'), bg=cor1, fg=cor4)
    textoLabel3.place(x=80, y=170)

    janela3.mainloop()

tela1()