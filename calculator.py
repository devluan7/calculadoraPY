from tkinter import *

#Função que vai pegar os botões que foram clicados e transformar em string
def adcValor(val):
    textoAtual = telaExibicao.get() #Estamos atribuindo o valor que estiver na telaExibição na variavel textoDigitado
    telaExibicao.delete(0, END)
    telaExibicao.insert(END, textoAtual + val)


#Função que vai calcular a expressao usando o eval()
def calculaResult():
    expressao = telaExibicao.get()
    try:
       resultado = eval(expressao)
       telaExibicao.delete(0, END)
       telaExibicao.insert(END, str(resultado))
    except Exception as erro:
        telaExibicao.delete(0, END)
        telaExibicao.insert(END, "Erro")


#Função para limpar a tela
def limparTela():
    telaExibicao.delete(0, END)



# Criando a interface Gráfica
janelaPrincipal = Tk()
janelaPrincipal.configure(bg="#223344")
janelaPrincipal.title("Calculadora")

# Tela de exibição
telaExibicao = Entry(janelaPrincipal, width=40, font =("Arial", 15), bg="black", fg="white")
telaExibicao.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

botoesNum = [
    {"text": "7", "name": "botao7"},
    {"text": "8", "name": "botao8"},
    {"text": "9", "name": "botao9"},
    {"text": "/", "name": "botaoDivisao"},
    {"text": "4", "name": "botao4"},
    {"text": "5", "name": "botao5"},
    {"text": "6", "name": "botao6"},
    {"text": "*", "name": "botaoMultiplicacao"},
    {"text": "1", "name": "botao1"},
    {"text": "2", "name": "botao2"},
    {"text": "3", "name": "botao3"},
    {"text": "-", "name": "botaoSubtracao"},
    {"text": "0", "name": "botao0"},
    {"text": ".", "name": "botaoPonto"},
    {"text": "C", "name": "botaoC"},
    {"text": "+", "name": "botaoSoma"},
    {"text": "=", "name": "botaoIgual"}


] #Dentro da lista, eu criei um dicionário para ficar mais facil de manipular um botao isolado depois

numeroLinha = 1
numeroColuna = 0



for digitos in botoesNum:
    texto = digitos["text"]
    nome = digitos["name"]


    botao = Button(janelaPrincipal, text=texto, width=7, height=3, bg="black", fg="white")
    botao.grid(row=numeroLinha, column=numeroColuna, padx=5, pady=5, sticky="NSEW")

    botao.configure(command=lambda val=texto: adcValor(val))
    #o command lambda é usado para criar uma função "anonima" que permite
    #passar diferentes argumentos para cada botao, ou seja
    #ela permite que a funcao adcValor(valor) se comporte diferente para cada botao
    #o val recebe o valor de texto (cada texto recebe o dos botoes, passados pelo for)

    if nome == "botaoC":
        botao.configure(command=limparTela)
    elif nome == "botaoIgual":
        botao.configure(command=calculaResult)
        botao.grid(columnspan=2)

    numeroColuna += 1
    if numeroColuna > 3:
        numeroColuna = 0
        numeroLinha += 1
        if numeroLinha > 4:
             numeroColuna = 1



janelaPrincipal.mainloop()