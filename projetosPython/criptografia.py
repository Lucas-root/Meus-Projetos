
from sys import argv

palavra_passada = argv[1]

alfabeto = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
	'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
	'u', 'v', 'w', 'x', 'y', 'z'
			
]

def criptografa(palavra):
	'''
	criptografa uma palavra com a tecnica letra>>
	ex: l = m 
	'''
	criptografado = ''

	for letra in palavra:

		adicionar = ''
		index = alfabeto.index(letra)
		
		# caso index se refira a ultima letra adicionar recebe a
		if index == len(alfabeto)-1:
			adicionar = alfabeto[0]
		else:
			adicionar = alfabeto[index + 1]
		
		criptografado += adicionar
	
	return criptografado

print(f'\nA palavra "{palavra_passada}" criptografada fica: {criptografa(palavra_passada)}\n')
