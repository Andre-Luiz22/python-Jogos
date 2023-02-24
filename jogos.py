import adivinhacao
import forca

def escolher_jogo():
    print("************************")
    print("***Escolha o seu jogo***")
    print("************************")

    print("(1)Forca  (2)Adivinhação")
    jogo = int(input("Escolha 1 jogo\n"))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    else:
        print("Jogando adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolher_jogo()
