import random
from listas import *


palavra_escondida = []
letras_corretas = []
letras_erradas = []
tentativas = 6
palavra_escolhida = ''
categoria = ''
dica = ''

def verificaLista(lista):
    if lista == '1':
        if len(estados) >= 1:
            return True
        else:
            return False
    elif lista == '2':
        if len(pessoas) >= 1:
            return True
        else:
            return False
    elif lista == '3':
        if len(filmes) >= 1:
            return True
        else:
            return False
    elif lista == '4':
        if len(frutas) >= 1:
            return True
        else:
            return False
    elif lista == '5':
        if len(animais) >= 1:
            return True
        else:
            return False

def listas(numLista):
    global dica
    global categoria
    if inicio == '1':
        opcoes = list(estados.keys())
        palavra = random.choice(opcoes)
        dica = estados.get(palavra)
        estados.pop(palavra)
        categoria = 'Estados'
        return palavra
    elif inicio == '2':
        opcoes = list(pessoas.keys())
        palavra = random.choice(opcoes)
        dica = pessoas.get(palavra)
        pessoas.pop(palavra)
        categoria = 'Pessoas'
        return palavra
    elif inicio == '3':
        opcoes = list(filmes.keys())
        palavra = random.choice(opcoes)
        dica = filmes.get(palavra)
        filmes.pop(palavra)
        categoria = 'Filmes'
        return palavra
    elif inicio == '4':
        opcoes = list(frutas.keys())
        palavra = random.choice(opcoes)
        dica = frutas.get(palavra)
        frutas.pop(palavra)
        categoria = 'Frutas'
        return palavra
    elif inicio == '5':
        opcoes = list(animais.keys())
        palavra = random.choice(opcoes)
        dica = animais.get(palavra)
        animais.pop(palavra)
        categoria = 'Animais'
        return palavra

def sorteio(tipoLista):
    global palavra_escolhida
    if verificaLista(tipoLista):
        palavra_escolhida = listas(tipoLista)
        for x in range(len(palavra_escolhida)):
            palavra_escondida.append("_")
    else:
        print('A categoria n??o possui item v??lidos, tente novamente!')

def buscaLetra(letra):
    if letra not in letras_erradas and letra not in letras_corretas:
        #verifica se a letra informada pelo jogador est?? na palavra sorteada
        if letra in palavra_escolhida:
            #add a letras corretas
            letras_corretas.append(letra)
            #procura a posi????o correta da letra e a adiciona nela.
            for x in range(len(palavra_escolhida)):
                if letra == palavra_escolhida[x]:
                    palavra_escondida[x] = letra
        else:
            #caso a letra informada esteja errada, ele retira uma das tentativas do jogador
            global tentativas
            tentativas -= 1
            letras_erradas.append(letra)
            desenho_boneco()
    else:
        print("\n")
        print("#" * 50)
        print("Essa letra j?? foi escolhida, tente uma nova letra!!")
        print("#" * 50)

def verificarJogo():
    if ''.join(palavra_escondida) == palavra_escolhida:
        print(f'PARAB??NS, VOC?? GANHOU !!!!!! ')
        print(f"Voc?? acertou a palavra: {palavra_escolhida}")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        return False
    elif tentativas < 1:
        print(f'A Palavra era {palavra_escolhida}')
        print(f'VOC?? PERDEU !!! MAIS SORTE NA PR??XIMA VEZ :)')
        return False
    else:
        return True

def desenho_boneco():
    global tentativas
    if (tentativas == 5):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 4):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if (tentativas == 3):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |            ")

    if (tentativas == 2):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (tentativas == 1):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /      ")

    if (tentativas == 0):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \    ")


def verificaLetra(letra):
    #Verifica se o que foi informado pelo jogador ?? uma letra ou n??o
    if (ord(letra) >= 65 and ord(letra) <= 90) or ((ord(letra) >= 97 and ord(letra) <= 122)):
        return True
    else:
        return False

jogar = True
while jogar:
    if palavra_escolhida == '':
        print(">" * 32, "UNIESP", "<" * 32, "\n                        Introdu????o a Programa????o\n")
        print("*   Grupo:\n*   Guilherme Jos?? - 2022111510046@iesp.edu.br\n*   Jorge de Melo - 2022111510039@iesp.edu.br")
        print("*   Marcelo Medeiros - 2022111510069@iesp.edu.br\n*   Marcos Pablo - 2022111510024@iesp.edu.br")
        print("*   Pollyara Virginia - 2022110220026@iesp.edu.br\n")
        print(">" * 32, "******", "<" * 32, "\n")
        print("Bem-vindo ao jogo da forca!")
        print("Voc?? possui 6 chances para tentar acertar a palavra misteriosa!")
        print("Escolha uma das categorias e divirta-se!!\n")
        print("1 - ESTADOS\n2 - PESSOAS\n3 - FILMES\n4 - FRUTAS\n5 - ANIMAIS\n0 - SAIR\n")
        inicio = input("Escolha uma categoria:")
        if inicio == '1' or inicio == '2' or inicio == '3' or inicio == '4' or inicio == '5':
            sorteio(inicio)
        elif inicio == '0':
            print("\nVoce saiu do jogo")
            print("Espero que tenha Gostado!")
            print("At?? Logo!!")
            jogar = False
        else:
            print("\n")
            print("#" * 50)
            print("A categoria que voc?? escolheu n??o existe!")
            print("Escolha uma categoria v??lida")
            print("#" * 50)
            print("\n")
    else:
        print("*" * 50)
        print(f'\nCategoria: {categoria}')
        print(f'Dica: {dica}')
        letra = input('Informe uma letra: ').lower()

        if len(letra) == 1:
            if verificaLetra(letra):
                buscaLetra(letra)
            else:
                print("\n")
                print("#" * 50)
                print("                  N??O ?? UMA LETRA!")
                print("#" * 50)
        else:
            print("\n")
            print("#" * 50)
            print("                INFORME APENAS 1 LETRA POR VEZ!!!!")
            print("#" * 50)
        print(f'\nCategoria: {categoria}')
        print(f'Dica: {dica}\n')
        print(f'Palavra: ', end="")
        print(' , '.join(palavra_escondida))
        print(f'Letras Certas: ', end="")
        print(' , '.join(letras_corretas))
        print(f'Letras Erradas: ', end="")
        print(' , '.join(letras_erradas))
        print(f'Tentivas restantes: {tentativas}\n')
        jogar = verificarJogo()
        if jogar == False:
            teste = input("Desejar jogar novamente? Digite: sim :").lower()
            if teste == 'sim':
                palavra_escondida = []
                letras_corretas = []
                letras_erradas = []
                tentativas = 6
                palavra_escolhida = ''
                categoria = ''
                dica = ''
                jogar = True
            else:
                print("\nVoc?? saiu do jogo!")
                print("Espero que tenha Gostado!")
                print("At?? Logo!!")