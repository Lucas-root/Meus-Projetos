# olá me chamo Lucas sou iniciante em programação 
# e estou tentando criar um jogo da velha de terminal em python3
# me desculpe pela bagunça do código e sintase a vontade
# para propor modificações

# casas disponiveis
# se uma casa não está disponivel ela recebe x ou o (ó)
#está variavel serve para mais tarde atribuirmos valores
#e imprimilos

casa1 = '0'
casa2 = '0'
casa3 = '0'
casa4 = '0'
casa5 = '0'
casa6 = '0'
casa7 = '0'
casa8 = '0'
casa9 = '0'

# correspondencias no momento sem uso 
# (mudei a forma com que estava pensando escrever este codigo)
corresponde = {1:1, 2:1, 3:1,
               4:2, 5:2, 6:2,
               7:3, 8:3, 9:3}

'''
def tabuleiro(casa, valor):
    if casa = 1:
        tabuleiro =   
tabuleiro = """
 {} | {} | {}
 {} | {} | {}
 {} | {} | {}
""".format(1, 2, 3, 4, 5, 6, 7, 8, 9)
'''

# colhe como dados de entrada a casa que o joador quer jogar

jogada = int(input('Digite a casa que você que jogar : '))

#  em um intervalo de 1 ate 9 ele verifica se a jogada do jogador 
# é igual ao i 
for i in range(1, 10): 
    if jogada == i:
        atual = " {} | {} | {} \n {} | {} | {} \n {} | {} | {} ".format(casa1, casa2, casa3, casa4, casa5, casa6, casa7, casa8, casa9)
        print(atual)
        break
#!!! tenho que colher os dados da casa e valor
# depois atribuir os dado a sua respectiva variavel casa (que está definida no começo)
# e depois imprimir estes dados na tela 
