alfabeto = 'abcdefghijklmnopqrstuvwxyz' # o alfabeto completo serve para a função gerador() ultilizala

#recebe a palavra e a formata (retira os possiveis espaços nos lados e joga ela para lower)
palavra = input('Digite uma palavra para ver qual \né a sua maior precedencia  alfabetica : ')
palavra = palavra.lower()
palavra = palavra.strip()

def gerador(alterar):
	tamanho = len(alterar)

	ultimo = len(alterar)-1

	possiveis = []
	letra = 0
	inicial = 2 
	loop = 0

	while loop <= ultimo:
		
		loop += 1
		for i in range(tamanho):
			if i == 0:
				controle = inicial
				possiveis.append(alterar[letra])
			if controle <= tamanho:
				possiveis.append(alterar[letra:controle])
				controle += 1
		inicial += 1
		letra += 1
	return possiveis	

alpha_possi = gerador(alfabeto)
palavra_possi = gerador(palavra)

len_palavra = len(palavra_possi)
conta = 0

maior = 0
qual = '' 

for i in range(len_palavra):
	if palavra_possi[i] in alpha_possi:
		if len(palavra_possi[i]) > maior:
			maior = len(palavra_possi[i])	
			qual = palavra_possi[i]

print('A maior precedencia alfabetica desta palavra é {}'.format(qual))


			
