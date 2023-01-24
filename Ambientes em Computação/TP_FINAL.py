import tkinter as tk #biblioteca para criação de interface visual para o programa
from tkinter import ttk
from tkinter.messagebox import showinfo
from functools import partial #usado para definir funções mais elaboradas para comandos dos botões
from datetime import datetime
import pandas as pd #plotagem e visualização de gráficos
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os.path #caminho do arquivo
import keyboard as keyboard #entrada dialog box
import random

indiceImg = 0 #variável usada para percorrer o vetor com as imagens a serem mostradas
respostasCorretas = 0 #guarda a quantidade de respostas corretas no teste que está em curso
userName = ""

#DEFINIR NO CAMPO ABAIXO O CAMINHO DA PASTA COM AS IMAGENS DO PROJETO
imageFolder = "C:/Users/guibr/OneDrive/Área de Trabalho/Projeto TP - Ambientes em Computação/Imagens/"

#DEFINIR NO CAMPO ABAIXO O CAMINHO DA PASTA ONDE SERÃO GRAVADOS/LIDOS OS RESULTADOS
savePath = 'C:/Users/guibr/OneDrive/Área de Trabalho/Projeto TP - Ambientes em Computação/resultados/'

#CRIAÇÃO DA JANELA ONDE SERÃO MOSTRADOS OS ELEMENTOS DO PRIMEIRO TREINO
def treino1():
    def imagem_prox():#FUNÇÃO UTILIZADA PARA PERCORRER O VETOR DE IMAGENS E MOSTRAR CADA IMAGEM NA TELA
        global indiceImg
        if (indiceImg >= 9):
            return
        if (indiceImg == 8):
            bt1["state"] = "disabled"
            ttk.Label(treino, image=listaTreino1[indiceImg]).grid(column=2, row=2)
            indiceImg = 0
            return
        ttk.Label(treino, image=listaTreino1[indiceImg]).grid(column=2, row=2)
        indiceImg += 1
        return

    treino = tk.Toplevel()
    treino.title('Treino 1')

    window_width = 800
    window_height = 600
    treino.grid()
    treino.columnconfigure(0, weight=0)
    treino.columnconfigure(1, weight=0)
    treino.columnconfigure(2, weight=0)
    treino.columnconfigure(3, weight=0)
    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    treino.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    # root.resizable(window_width,window_height)
    global indiceImg
    imagem_prox()

    bt1 = ttk.Button(treino, text="Próximo", command=imagem_prox)
    bt1.grid(column=0, row=0)
    bt2 = ttk.Button(treino, text="Sair", command=treino.destroy)
    bt2.grid(column=0, row=1)


#CRIAÇÃO DA JANELA ONDE SERÃO MOSTRADOS OS ELEMENTOS DO SEGUNDO TREINO
def treino2():
    def imagem_prox():#FUNÇÃO UTILIZADA PARA PERCORRER O VETOR DE IMAGENS E MOSTRAR CADA IMAGEM NA TELA
        global indiceImg
        if (indiceImg >= 4):
            return
        if (indiceImg == 3):
            bt1["state"] = "disabled"
            ttk.Label(treino, image=listaTreino2[indiceImg]).grid(column=2, row=2)
            indiceImg = 0
            return
        ttk.Label(treino, image=listaTreino2[indiceImg]).grid(column=2, row=2)
        indiceImg += 1
        return

    treino = tk.Toplevel()
    treino.title('Treino 2')

    window_width = 800
    window_height = 600
    treino.grid()
    treino.columnconfigure(0, weight=0)
    treino.columnconfigure(1, weight=0)
    treino.columnconfigure(2, weight=0)
    treino.columnconfigure(3, weight=0)
    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    treino.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    global indiceImg
    imagem_prox()

    bt1 = ttk.Button(treino, text="Próximo", command=imagem_prox)
    bt1.grid(column=0, row=0)
    bt2 = ttk.Button(treino, text="Sair", command=treino.destroy)
    bt2.grid(column=0, row=1)


#GERA A TELA COM OS ELEMENTOS DO TESTE 1 (JANELA, BOTÕES ETC)
def teste1():
    teste = tk.Toplevel()
    teste.title('Teste 1')

    window_width = 1000
    window_height = 600
    teste.grid()
    teste.columnconfigure(0, weight=0)
    teste.columnconfigure(1, weight=0)
    teste.columnconfigure(2, weight=0)
    teste.columnconfigure(3, weight=0)
    # get the screen dimension
    screen_width = teste.winfo_screenwidth()
    screen_height = teste.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    teste.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    #APÓS O USUÁRIO ESCREVER SEU NOME E CLICAR EM "INICIAR", INICIA O TESTE
    def iniciar_clicked(nome):
        global userName
        userName = nome_entry.get()

        listaTeste1[17] = nome_entry.get()
        msg = nome_entry.get()
        showinfo(
            title=f'Iniciando...',
            message= f"Iniciando o Teste de {msg}"
        )
        bt1["state"] = "enabled"
        iniciar_button["state"] = "disabled"
        iniciar_button.destroy()
        nome_entry.destroy()
        teste.focus()#FECHA O ELEMENTO DE ESCRITA DO NOME E RETORNA PARA A TELA PARA INICIAR O TESTE

    #CRIA O ELEMENTO TEXTBOX PARA ESCRITA DO NOME DO USUÁRIO
    nome = tk.StringVar()
    nome_entry = ttk.Entry(teste, textvariable=nome)
    nome_entry.grid(column=4,row=2)
    nome_entry.focus()

    comandoIniciar = partial(iniciar_clicked,nome)

    iniciar_button = ttk.Button(teste, text="Iniciar", command=comandoIniciar)
    iniciar_button.grid(column=5,row=2)

    comandoBt1 = partial(imagemProx1, teste)#FAZ A CHAMADA DA FUNÇÃO "imagemProx1" para iniciar o teste 1
    bt1 = ttk.Button(teste, text="Próximo", state="disabled", command=comandoBt1)
    bt1.grid(column=0, row=0)


#FUNÇÃO QUE MOSTRA AS IMAGENS E RESPECTIVAS OPÇÕES DE RESPOSTA (TESTE 1)
def imagemProx1(teste):

    comandoBt1 = partial(imagemProx1, teste)

    bt1 = ttk.Button(teste, text="Próximo", command=comandoBt1,state="disabled")
    bt1.grid(column=0, row=0)

    #VERIFICA SE A RESPOSTA ESTÁ CORRETA E INCREMENTA O CAMPO RESPECTIVO, EM CASO POSITIVO
    def verificarResposta(r):
        btOpc1["state"] = "disabled"
        btOpc2["state"] = "disabled"
        btOpc3["state"] = "disabled"
        if (r == opcaoCorreta):
            listaTeste1[16] += 1

        if listaTeste1[15] < 5 :
            bt1["state"] = "enabled"
        else:
            bt3 = ttk.Button(teste, text="Sair", state="enabled", command=teste.destroy)
            bt3.grid(column=4, row=0)

            escreverResultados(listaTeste1)

            listaTeste1[15] = 0
            listaTeste1[16] = 0

        opc1.destroy()
        opc2.destroy()
        opc3.destroy()
        btOpc1.destroy()
        btOpc2.destroy()
        btOpc3.destroy()
        perguntaImg.destroy()
        perguntaTxt.destroy()

    #UTILIZA O "randint" PARA RANDOMIZAR AS PERGUNTAS E OPÇÕES DE RESPOSTA
    imgPergunta = random.randint(0, 14)

    opcao1 = random.randint(0, 4)
    opcao2 = random.randint(5, 9)
    opcao3 = random.randint(10, 14)
    opcaoCorreta = imgPergunta // 5 #CÁLCULO PARA DEFINIÇÃO DA REPOSTA CORRETA
    opcaoEscolhida = -1


    #PERCORRE O VETOR COM AS IMAGENS E CRIA AS OPÇÕES DE RESPOSTA RELACIONADAS A SEREM RESPONDIDAS PELO USUÁRIO
    if listaTeste1[15] < 5:

        #CRIAÇÃO DOS ELEMENTOS DA IMAGEM REFERÊNCIA, OPÇÕES DE RESPOSTA E SEUS RESPECTIVOS BOTÕES
        perguntaImg = ttk.Label(teste, image=listaTeste1[imgPergunta])
        perguntaImg.grid(column=2, row=2)

        perguntaTxt = ttk.Label(teste,text=("Qual das opções está relacionada com a imagem acima ? \n (clicar no botão correspondente)"))
        perguntaTxt.grid(column=2, row=3)

        opc1 = ttk.Label(teste, image=listaTeste1[opcao1])
        opc2 = ttk.Label(teste, image=listaTeste1[opcao2])
        opc3 = ttk.Label(teste, image=listaTeste1[opcao3])
        listaTeste1[15] = listaTeste1[15] + 1

        opc1.grid(column=1, row=4)
        opc2.grid(column=2, row=4)
        opc3.grid(column=3, row=4)

        #AO SER CLICADO, O BOTÃO DISPARA A FUNÇÃO DE VERIFICAR RESPOSTA E PASSA PARA A PRÓXIMA TELA
        comandoOpcao1 = partial(verificarResposta, 0)
        comandoOpcao2 = partial(verificarResposta, 1)
        comandoOpcao3 = partial(verificarResposta, 2)

        btOpc1 = ttk.Button(teste, text="1", command=comandoOpcao1)
        btOpc2 = ttk.Button(teste, text="2", command=comandoOpcao2)
        btOpc3 = ttk.Button(teste, text="3", command=comandoOpcao3)

        btOpc1.grid(column=1, row=5)
        btOpc2.grid(column=2, row=5)
        btOpc3.grid(column=3, row=5)

        teste.grid()
    else:#ÚLTIMA PERGUNTA DO TESTE E FINALIZA COM A TELA COM O BOTÃO "SAIR"
        bt1 = ttk.Button(teste, text="Próximo", state= "disabled")
        bt1.grid(column=0, row=0)
        bt3 = ttk.Button(teste, text="Sair", state="enabled", command=teste.destroy)
        bt3.grid(column=4, row=0)
        ttk.Label(teste, image=listaTeste1[imgPergunta]).grid(column=2, row=2)
        tk.Label(teste,text="Qual das opções está relacionada com a imagem acima ? \n (clicar no botão correspondente)").grid(column=2, row=3)

        teste.grid()

        return


#GERA A TELA COM OS ELEMENTOS DO TESTE 2 (JANELA, BOTÕES ETC)
def teste2():
    teste = tk.Toplevel()
    teste.title('Teste 2')

    window_width = 1000
    window_height = 600
    teste.grid()
    teste.columnconfigure(0, weight=0)
    teste.columnconfigure(1, weight=0)
    teste.columnconfigure(2, weight=0)
    teste.columnconfigure(3, weight=0)
    # get the screen dimension
    screen_width = teste.winfo_screenwidth()
    screen_height = teste.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    teste.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    #APÓS O USUÁRIO ESCREVER SEU NOME E CLICAR EM "INICIAR", INICIA O TESTE
    def iniciar_clicked(nome):
        global userName
        userName = nome_entry.get()

        listaTeste2[8] = nome_entry.get()
        msg = nome_entry.get()
        showinfo(
            title=f'Iniciando...',
            message=f"Iniciando o Teste de {msg}"
        )
        bt1["state"] = "enabled"
        iniciar_button["state"] = "disabled"
        iniciar_button.destroy()
        nome_entry.destroy()
        teste.focus()#FECHA O ELEMENTO DE ESCRITA DO NOME E RETORNA PARA A TELA PARA INICIAR O TESTE

    #CRIA O ELEMENTO TEXTBOX PARA ESCRITA DO NOME DO USUÁRIO
    nome = tk.StringVar()
    nome_entry = ttk.Entry(teste, textvariable=nome)
    nome_entry.grid(column=4,row=2)
    nome_entry.focus()

    comandoIniciar = partial(iniciar_clicked,nome)
    iniciar_button = ttk.Button(teste, text="Iniciar", command=comandoIniciar)
    iniciar_button.grid(column=5,row=2)

    comandoBt1 = partial(imagemProx2, teste)  # FAZ A CHAMADA DA FUNÇÃO "imagemProx2" para iniciar o teste 2
    bt1 = ttk.Button(teste, text="Próximo", state="disabled", command=comandoBt1)
    bt1.grid(column=0, row=0)


#FUNÇÃO QUE MOSTRA AS IMAGENS E RESPECTIVAS OPÇÕES DE RESPOSTA (TESTE 2)
def imagemProx2(teste):
    comandoBt1 = partial(imagemProx2, teste)

    bt1 = ttk.Button(teste, text="Próximo", command=comandoBt1, state="disabled")
    bt1.grid(column=0, row=0)

    #VERIFICA SE A RESPOSTA ESTÁ CORRETA E INCREMENTA O CAMPO RESPECTIVO, EM CASO POSITIVO
    def verificarResposta(r):
        btOpc1["state"] = "disabled"
        btOpc2["state"] = "disabled"
        if (r == opcaoCorreta):
            listaTeste2[7] += 1

        if listaTeste2[6] < 5:
            bt1["state"] = "enabled"
        else:
            #print("respostas corretas: ", listaTeste2[7])
            bt3 = ttk.Button(teste, text="Sair", state="enabled", command=teste.destroy)
            bt3.grid(column=4, row=0)

            escreverResultados(listaTeste2)

            listaTeste2[6] = 0
            listaTeste2[7] = 0

        opc1.destroy()
        opc2.destroy()
        btOpc1.destroy()
        btOpc2.destroy()
        perguntaImg.destroy()
        perguntaTxt.destroy()

    #UTILIZA O "randint" PARA RANDOMIZAR AS PERGUNTAS E OPÇÕES DE RESPOSTA
    imgPergunta = random.randint(0, 5)
    opcao1 = random.randint(0, 2)
    opcao2 = random.randint(3, 5)
    opcaoCorreta = imgPergunta // 3 #CÁLCULO PARA DEFINIÇÃO DA REPOSTA CORRETA
    opcaoEscolhida = -1

    #PERCORRE O VETOR COM AS IMAGENS E CRIA AS OPÇÕES DE RESPOSTA RELACIONADAS A SEREM RESPONDIDAS PELO USUÁRIO
    if listaTeste2[6] < 5:
        #CRIAÇÃO DOS ELEMENTOS DA IMAGEM REFERÊNCIA, OPÇÕES DE RESPOSTA E SEUS RESPECTIVOS BOTÕES
        perguntaImg = ttk.Label(teste, image=listaTeste2[imgPergunta])
        perguntaImg.grid(column=2, row=2)

        perguntaTxt = ttk.Label(teste, text=("Qual das opções está relacionada com a imagem acima ? \n (clicar no botão correspondente)"))
        perguntaTxt.grid(column=2, row=3)

        opc1 = ttk.Label(teste, image=listaTeste2[opcao1])
        opc2 = ttk.Label(teste, image=listaTeste2[opcao2])
        listaTeste2[6] = listaTeste2[6] + 1

        opc1.grid(column=1, row=4)
        opc2.grid(column=3, row=4)

        #AO SER CLICADO, O BOTÃO DISPARA A FUNÇÃO DE VERIFICAR RESPOSTA E PASSA PARA A PRÓXIMA TELA
        comandoOpcao1 = partial(verificarResposta, 0)
        comandoOpcao2 = partial(verificarResposta, 1)

        btOpc1 = ttk.Button(teste, text="1", command=comandoOpcao1)
        btOpc2 = ttk.Button(teste, text="2", command=comandoOpcao2)

        btOpc1.grid(column=1, row=5)
        btOpc2.grid(column=3, row=5)

        teste.grid()
    else:#ÚLTIMA PERGUNTA DO TESTE E FINALIZA COM A TELA COM O BOTÃO "SAIR"
        bt1 = ttk.Button(teste, text="Próximo", state="disabled")
        bt1.grid(column=0, row=0)
        bt3 = ttk.Button(teste, text="Sair", state="enabled", command=teste.destroy)
        bt3.grid(column=4, row=0)
        ttk.Label(teste, image=listaTeste2[imgPergunta]).grid(column=2, row=2)
        tk.Label(teste,text="Qual das opções está relacionada com a imagem acima ? \n (clicar no botão correspondente)").grid(column=2, row=3)

        teste.grid()

        return


#FUNÇÃO QUE RECEBE O VETOR COM OS VALORES RESULTANTES DO TESTE REALIZADO E SALVA NO COMPUTADOR NUM .TXT
def escreverResultados(listaTeste):

    #PRIMENTO FAZ A VERIFICAÇÃO DE QUAL TESTE ESTÁ SENDO ESCRITO
    #DEPOIS ADICIONA UMA LINHA NO ARQUIVO DE TEXTO CONTENDO :
    #           1- NOME DO USUÁRIO
    #           2- TIPO DO TESTE (1 OU 2)
    #           3- QUANTIDADE DE ACERTOS OBTIDOS
    #           4- DATA/HORÁRIO DE FINALIZAÇÃO DO TESTE

    if len(listaTeste) > 9 :
        resultadoTeste = f"{listaTeste[17]},1,{listaTeste[16]},{datetime.now()}\n"

        with open(f'{savePath}resultados.txt', 'a') as myfile:
            myfile.write(resultadoTeste)

        myfile.close()
    else:
        resultadoTeste = f"{listaTeste[8]},2,{listaTeste[7]},{datetime.now()}\n"

        with open(f'{savePath}resultados.txt', 'a') as myfile:
            myfile.write(resultadoTeste)

        myfile.close()

#FUNÇÃO QUE ABRE UMA TELA EM QUE O USUÁRIO DEVE ESCREVER UM NOME A SER PESQUISADO
#ENVIA O NOME PESQUISADO PARA A FUNÇÃO "lerResultados" ONDE É FEITA A LEITURA DO ARQUIVO
def resultados():
    resultado = tk.Toplevel()
    resultado.title('resultados')

    window_width = 1000
    window_height = 600
    resultado.grid()
    resultado.columnconfigure(0, weight=0)
    resultado.columnconfigure(1, weight=0)
    resultado.columnconfigure(2, weight=0)
    resultado.columnconfigure(3, weight=0)
    # get the screen dimension
    screen_width = resultado.winfo_screenwidth()
    screen_height = resultado.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    resultado.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    comandoBt1 = partial(imagemProx1, resultado)
    bt1 = ttk.Button(resultado, text="Sair", command=resultado.destroy)
    bt1.grid(column=0, row=0)

    def ok_clicked(nome):
        global userName
        userName = nome_entry.get()
        msg = nome_entry.get()
        bt1["state"] = "enabled"
        OK_button["state"] = "disabled"
        OK_button.destroy()
        nome_entry.destroy()
        resultado.destroy()
        lerResultados(userName) #APÓS O USUÁRIO DIGITAR O NOME E CLICAR EM OK, CHAMA A FUNÇÃO QUE
        #                       VAI LER O ARQUIVO DE TEXTO

    nome = tk.StringVar()
    nome_entry = ttk.Entry(resultado, textvariable=nome)
    nome_entry.grid(column=4,row=2)
    nome_entry.focus()

    comandoOK = partial(ok_clicked,nome)

    OK_button = ttk.Button(resultado, text="Pesquisar", command=comandoOK)
    OK_button.grid(column=5,row=2)

#FUNÇÃO CHAMADA POR "resultados()". FAZ A LEITURA DO ARQUIVO TXT PREVIAMENTE SALVO NO PC.
#ELE FAZ A BUSCA LINHA POR LINHA E SE ENCONTRAR ALGUM REGISTRO PARA O USUÁRIO PESQUISADO,
#RETORNA OS RESULTADOS E MONTA OS RESPECTIVOS GRÁFICOS
def lerResultados(nome):
    f = open(f'{savePath}resultados.txt', 'r')
    linha = f.readline()
    listaResTeste1 = list()
    listaResTeste2 = list()
    dadosTeste1 = list()
    dadosTeste2 = list()
    nomeUsuario = nome

    while linha != "":#FAZ A LEITURA DO ARQUIVO "resultados.txt"
        registro = linha.split(",")

        if registro[0] == nome:
            if registro[1] == "1" :
                data = registro[3].split((" "))
                dadosTeste1.append(data[0])
                listaResTeste1.append((int(registro[2])))
            else:
                data = registro[3].split((" "))
                dadosTeste2.append(data[0])
                listaResTeste2.append(int((registro[2])))
            print(linha)
        linha = f.readline()


    #CRIAÇÃO DAS TUPLAS REPRESENTANDO OS RESULTADOS ENCONTRADOS
    data1 = {'Datas T1': dadosTeste1,'Nº Acertos': listaResTeste1}
    data2 = {'Datas T2': dadosTeste2, 'Nº Acertos': listaResTeste2}

    #CRIA DATAFRAMES (UTILIZADOS PELA BIBLIOTECA DE PLOTAGEM DE GRÁFICOS)
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    print(df1)
    print(df2)

    #CRIA UMA NOVA JANELA ONDE SERÃO MOSTRADOS OS GRÁFICOS
    resultado = tk.Toplevel()
    resultado.title('resultados')
    window_width = 1000
    window_height = 600
    resultado.grid()
    resultado.columnconfigure(0, weight=0)
    resultado.columnconfigure(1, weight=0)
    resultado.columnconfigure(2, weight=0)
    resultado.columnconfigure(3, weight=0)
    # get the screen dimension
    screen_width = resultado.winfo_screenwidth()
    screen_height = resultado.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    resultado.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    #CRIAÇÃO DA VISUALIZAÇÃO DO GRÁFICO DO TESTE 1
    figure1 = plt.Figure(figsize=(6, 1), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, resultado)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df1 = df1[['Datas T1', 'Nº Acertos']]#.groupby('country').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title(f'{nomeUsuario} - Resultados T1')

    # CRIAÇÃO DA VISUALIZAÇÃO DO GRÁFICO DO TESTE 2
    figure2 = plt.Figure(figsize=(6, 1), dpi=100)
    ax2 = figure2.add_subplot(111)
    bar2 = FigureCanvasTkAgg(figure2, resultado)
    bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Datas T2', 'Nº Acertos']]  # .groupby('country').sum()
    df2.plot(kind='bar', legend=True, ax=ax2)
    ax2.set_title(f'{nomeUsuario} - Resultados T2')




#CRIANDO A PRIMEIRA TELA DA APLICAÇÃO
root = tk.Tk()
root.title('Treinamento RFT')

#Dimensionamento e posicionamento da janela da interface gráfica
window_width = 1300
window_height = 700
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=0)
root.columnconfigure(3, weight=0)
root.columnconfigure(4, weight=0)
root.columnconfigure(5, weight=0)
root.rowconfigure(0,weight = 0)
root.rowconfigure(1 ,weight= 0)
root.rowconfigure(2 ,weight= 1)
root.rowconfigure(3 ,weight= 1)
root.rowconfigure(4 ,weight= 1)
root.rowconfigure(5 ,weight= 1)
#root.columnconfigure(7,weight = 1)
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.grid()

#CRIANDO OS ELEMENTOS DO MENU PRINCIPAL DA APLICAÇÃO
b1 = ttk.Button(root, text="Treinamento 1", command=treino1)
b1.grid(column=0, row=0)
b2 = ttk.Button(root, text="Treinamento 2", command=treino2)
b2.grid(column=1, row=0)
b3 = ttk.Button(root, text="Teste 1", command=teste1).grid(column=2, row=0)
b4 = ttk.Button(root, text="Teste 2", command=teste2).grid(column=3, row=0)
b5 = ttk.Button(root, text="Resultados", command=resultados).grid(column=4, row=0)
bSair = ttk.Button(root, text="Sair", command=root.destroy).grid(column=8, row=0)

############ CRIANDO AS VARIÁVEIS CONTENDO O CAMINHO PARA CADA IMAGEM A SER USADA NOS TESTES E TREINAMENTOS
imgb1 = tk.PhotoImage(file=f'{imageFolder}b1.png')
imgb2 = tk.PhotoImage(file=f'{imageFolder}b2.png')
imgb3 = tk.PhotoImage(file=f'{imageFolder}b3.png')
imgb4 = tk.PhotoImage(file=f'{imageFolder}b4.png')
imgb5 = tk.PhotoImage(file=f'{imageFolder}b5.png')
imgbr1 = tk.PhotoImage(file=f'{imageFolder}br1.png')
imgbr2 = tk.PhotoImage(file=f'{imageFolder}br2.png')
imgbr3 = tk.PhotoImage(file=f'{imageFolder}br3.png')
imgc1 = tk.PhotoImage(file=f'{imageFolder}c1.png')
imgc2 = tk.PhotoImage(file=f'{imageFolder}c2.png')
imgc3 = tk.PhotoImage(file=f'{imageFolder}c3.png')
imgc4 = tk.PhotoImage(file=f'{imageFolder}c4.png')
imgc5 = tk.PhotoImage(file=f'{imageFolder}c5.png')
imgcr1 = tk.PhotoImage(file=f'{imageFolder}cr1.png')
imgcr2 = tk.PhotoImage(file=f'{imageFolder}cr2.png')
imgcr3 = tk.PhotoImage(file=f'{imageFolder}cr3.png')
imgd1 = tk.PhotoImage(file=f'{imageFolder}d1.png')
imgd2 = tk.PhotoImage(file=f'{imageFolder}d2.png')
imgd3 = tk.PhotoImage(file=f'{imageFolder}d3.png')
imgd4 = tk.PhotoImage(file=f'{imageFolder}d4.png')
imgd5 = tk.PhotoImage(file=f'{imageFolder}d5.png')
imgdr1 = tk.PhotoImage(file=f'{imageFolder}dr1.png')
imgdr2 = tk.PhotoImage(file=f'{imageFolder}dr2.png')
imgdr3 = tk.PhotoImage(file=f'{imageFolder}dr3.png')
imgg6 = tk.PhotoImage(file=f'{imageFolder}g6.png')
imgg7 = tk.PhotoImage(file=f'{imageFolder}g7.png')
imgg8 = tk.PhotoImage(file=f'{imageFolder}g8.png')
imggt1 = tk.PhotoImage(file=f'{imageFolder}gt1.png')
imggt2 = tk.PhotoImage(file=f'{imageFolder}gt2.png')
imgd6 = tk.PhotoImage(file=f'{imageFolder}d6.png')
imgd7 = tk.PhotoImage(file=f'{imageFolder}d7.png')
imgd8 = tk.PhotoImage(file=f'{imageFolder}d8.png')
imgdt1 = tk.PhotoImage(file=f'{imageFolder}dt1.png')
imgdt2 = tk.PhotoImage(file=f'{imageFolder}dt2.png')

 
###ORGANIZAÇÃO DAS IMAGENS EM LISTAS USADAS NOS TESTES/TREINOS
listaTreino1 = (imgbr1,imgbr2,imgbr3,imgcr1,imgcr2,imgcr3,imgdr1,imgdr2,imgdr3)
listaTreino2 = (imgdt1,imgdt2,imggt1,imggt2)

##  AS 3 ÚLTIMAS POSIÇÕES DA LISTA REPRESENTAM RESPECTIVAMENTE A QUANTIDADE DE QUESTÕES NO TESTE,
#   TOTAL DE ACERTOS NO TESTE E NOME DO USUÁRIO QUE ESTÁ REALIZANDO OS TESTES
listaTeste1 = [imgb1,imgb2,imgb3,imgb4,imgb5,imgc1,imgc2,imgc3,imgc4,imgc5,imgd1,imgd2,imgd3,imgd4,imgd5,0,0,""]
listaTeste2 = [imgd6,imgd7,imgd8,imgg6,imgg7,imgg8,0,0,""]

#início da aplicação
root.mainloop()