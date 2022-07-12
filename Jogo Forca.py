import random
import time


# Passos iniciais do jogo:
print("\nBem vindo ao jogo da Forca por Tarik\n")
nome = input("Qual é o seu nome: ")
print("Ola " + nome + "! boa sorte!")
time.sleep(2)
print("O jogo começará em Breve...\n Vamos jogar um pouco!")
time.sleep(3)

def princip():
    '''
    Essa é a função principal, com as variáveis etc...
    '''
    global contagem
    global mostrar
    global palavra
    global palav_advinhada
    global tamanho
    global jogar
    palav_advinhada = ["Janeiro","fronteira","imagem","filme","promessa","rua","carro","boneca","ritmo","vitoria","planta"]
    palavra = random.choice(palav_advinhada)
    tamanho = len(palavra)
    contagem = 0
    mostrar = '_' * tamanho
    palav_advinhada = []
    jogar = ""


def jogo_loop():
    '''
   Laço para executar o jogo novamente após o fim do jogo:
    '''
    global jogar
    jogar = input("Você quer jogar novamente? s = sim, n = não \n")
    while jogar not in ["s", "n","S","N"]:
        jogar = input("Você quer jogar novamente? s = sim, n = não \n")
    if jogar == 's' or jogar =='S':
        princip()
    elif jogar == "n" or jogar =='N':
        print("Obrigado por jogar! Espero que tenha aproveitado!!")
        exit()

# Iniciando as condições de jogo:
def forca():
    '''
   Laço para iniciar as condições do jogo:
    '''
    global contagem
    global mostrar
    global palavra
    global palav_advinhada
    global jogar
    limite = 5
    chute = input("Esta é a palavra: " + mostrar + " O que você irá chutar? \n")
    chute = chute.strip()
    if len(chute.strip()) == 0 or len(chute.strip()) >= 2 or chute <= "9":
        print("que tal tentar uma palavra\n")
        forca()
    elif chute in palavra:
        palav_advinhada.extend([chute])
        index = palavra.find(chute)
        palavra = palavra[:index] + "_" + palavra[index + 1:]
        mostrar = mostrar[:index] + chute + mostrar[index + 1:]
        print(mostrar + "\n")
    elif chute in palav_advinhada:
        print("Tente outra letra.\n")
    else:
        contagem += 1
        if contagem == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Você adivinhou errado! " + str(limite - contagem) + " tentativas restantes\n")
        elif contagem == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Você adivinhou errado! " + str(limite - contagem) + " tentativas restantes\n")
        elif contagem == 3:
            time.sleep(1)
            print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Você adivinhou errado! " + str(limite - contagem) + " tentativas restantes\n")
        elif contagem == 4:
            time.sleep(1)
            print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     o \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Você adivinhou errado! " + str(limite - contagem) + " tentativas restantes\n")
        elif contagem == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Você adivinhou errado! Forca nele!!!\n")
            print("A palvra correta era:",palav_advinhada,palavra)
            jogo_loop()
    if palavra == '_' * tamanho:
        print("Parabéns, você acertou corretamente!!!")
        jogo_loop()
    elif contagem != limite:
        forca()
princip()
forca()