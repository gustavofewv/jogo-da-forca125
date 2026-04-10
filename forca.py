import random as rd

def mensagem_inicial():
    print("--------------------------")
    print("bem vindo ao jogo")
    print("--------------------------")

def seleciona_palavra_aleatoria():
    arquivo = open("jogos/palavra.txt","r")
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.closed()
    posicao = rd.randrange(0,len(palavra))

    palavra_secreta = palavra[posicao].lower()
    return palavra_secreta

def letras_corretas(palavra_secreta):
    return ["_" for lrtra in palavra_secreta]

def entrada_dados():
    chute = input("escreveu uma letra:")
    chute = chute.strip().upper()
    return chute

def chute(palavra_secreta, chute,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
            return

def jogar_forca():

    mensagem_inicial()
    palavra_secreta = seleciona_palavra_aleatoria()

    letras_acertadas = letras_acertadas
    
    
    perdeu = False
    acertou = False
    erros = 0

    while(not perdeu and not acertou):
        chute = entrada_dados()
    
        if(chute in palavra_secreta):
             chute_coreto(palavra_secreta, chute,letras_acertadas)
        

        else:
            erros = erros + 1
            
        perdeu = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

if(__name__ == "__main__"):
    jogar_forca()