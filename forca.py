def jogar_forca():
    print("--------------------------")
    print("bem vindo ao jogo")
    print("--------------------------")    

    lista = ["--------------------------"]

    palavra_secreta = "peocessador"
    letras_acertadas = ["_","_","_","_","_","_","_","_",]
    perdeu = False
    acertou = False
    erros = 0


    if(not perdeu and not acertou):
        chute = input("escreveu uma letra:")
        chute = chute.strip()

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