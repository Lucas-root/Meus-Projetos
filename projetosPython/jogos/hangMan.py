# Este é um jogo da forca simples que no momento apenas possui uma palavra
# mas no futuro adicionarei a funcionalidade para ele escolher uma palavra
# em uma lista de palavras



alfabeto = 'abcdefghijklmnopqrstuvwxyz'
disponiveis = alfabeto
palavra = 'homem'
letras_disponiveis = palavra
tentativas = 8
foram = []

# esta variavel armazena no formato {0:['letra_da_pavalra':'_']}
# a estrutura da forca sendo a key do dict um numero que vai de 0 até o 
# tamanho da palavra no valor a primeira letra é a letra que ele faz referencia
# e a segunda str começa com um '_' mas quando o úsuario acerta a letra ele muda
# para a letra
estrutura = {}
conta = 0

# cria a estrutura da forma que será ultilizada
for letra in palavra:
	estrutura[conta] = [letra, '_']
	conta += 1

def imprime():
	'''
	imprime corretamente a variavel estrura
	'''
	string = ''
	for item in estrutura:
		string += estrutura[item][1]
	return string
		
while True:
	
	if tentativas == 0:
		print('\nQue pena! suas tentativas acabaram')
		print('A parlavra era : {}\n'.format(palavra))
		break
	elif letras_disponiveis == '':
		print('\nParabéns! você finalizou o jogo!\n')
		break
	print('\n'+'-='*20)
	print('Tentativas :',tentativas)
	print('Tente acertar a palavra :',imprime())
	print('\n'+'-='*20)

	letra = input('Digite uma letra : ')

	if not letra in alfabeto:
		print('Está letra já foi! tente outra')
		continue
	elif not letra in palavra:
		print('\nEstá palavra não contem está letra')
		tentativas -= 1
	elif letra in foram:
		print('Esta letra já foi! Tente outra')
	
	# se letra estiver em letras disponiveis ele remove a letra da variavel
	# letras disponiveis, remove 1 de tentativas, adiciona a letra que o úsuario
	# acabou de digitar a lista foram, e altera o '_' do estrutura[item][1] para 
	# a letra que o usuario digitou assim na hora que for ser impresso a estrutura
	# com a função imprime a letra que o úsuario digitou não será mais um traço
	elif letra in letras_disponiveis:
		letras_disponiveis = letras_disponiveis.replace(letra, '')
		foram.append(letra)
		disponiveis = disponiveis.replace(letra, '')
		for item in estrutura:
			if estrutura[item][0] == letra:
				estrutura[item][1] = letra

				
				
		

	
	
