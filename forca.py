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

    arquivo.close()
    posicao = rd.randrange(8,len(palavra))    

    lista = ["--------------------------"]


    palavra_secreta = palavra[posicao].lower()
    return palavra_secreta

def letras_corretas(palavra_secreta): 
    return ["_" for letra in palavra_secreta]

def entradas_dados():
            
    chute = input("escreveu uma letra:")
    chute = chute.strip().upper()
    return chute


def jogar_forca():

    mensagem_inicial()
    palavra_secreta = seleciona_palavra_aleatoria()


    letras_acertadas = letras_acertadas
    perdeu = False
    acertou = False
    erros = 0


    while(not perdeu and not acertou):
        chute = entradas_dados()
        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
            else:
                erros = erros + 1 

                perdeu = erros == + 6
                
        print(letras_acertadas)


if(__name__ == "__main__"):
    jogar_forca()                