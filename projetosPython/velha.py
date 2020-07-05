# sinta-se a vontade para propor melhorias e modificações. Este código não está pronto portando não é a versão final
# ele pode possuir bugs e não possui a melhor performance para um programa com este resultado

# autor <lucasedux0@gmail.com>

from random import choice
from time import sleep

# estas são as casas
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0 
h = 0 
i = 0 

posibilidades = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] # para verificar se a entrada do jogador é uma entrada valida
jogada = 0 # sempre que for par sera a vez do jogador e sempre que for impar do computador
disponiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] 
# sempre que alguem ultiliza umas destas casas a sua letra correspondente é apagada com o metodo .remove

for numero in range(1, 10): # ele vai repetir 9 vezes. O (numero) vai receber de 1 até 9
	
	
	# Obs a variavel (vez) diz se a casa vai receber 'X' ou 'C' e ela é comparatilhada mudando o seu valor conforme
	# a vez se for jogada for par é a vez do jogador e ela passa a valher 'X' se for impar é a vez da cpu e ela valhe 'C'
	if  jogada % 2 == 0: # se jogada for par vez recebe 'X' isto é o jogador é o 'x' e a cpu 'C'
		vez = 'X'
	elif jogada % 2 != 0: # se jogada não for par é a vez da cpu é a variavel vez recebe C
		vez = 'C'
	else:
		print('O correu um erro. Esta mensagem é referente a linha 27')

	if jogada % 2 == 0: # se jogada for para é a vez do jogador
		while True:
			valor = input('\nDigite a casa a ser jogada : ')
			if not valor in posibilidades: # se o valor não estiver em posibilidades True 
				print('Digite uma casa valida : ')
			elif valor == 'a' and a != 0: # estas variaveis verificam se a variavel escolhida já está preenchida
				print('Esta casa já contem um valor, tente em outra')
				continue
			elif valor == 'b' and b != 0:
				print('Esta casa já contem um valor tente em outra')
				continue
			elif valor == 'c' and c != 0:
				print('Esta casa já possui um valor tente em outra')
				continue
			elif valor == 'd' and d != 0:
				print('Esta casa já possui um valor tente em outra')
				continue
			elif valor == 'e' and e != 0:
				print('Esta casa já possui um valor tente em outra')
				continue
			elif valor == 'f' and f != 0:
				print('Esta casa já possui um valor tente em outra')
				continue
			elif valor == 'g' and g != 0:
				print('Esta casa já possui um valor tente em outra')
				continue
			elif valor == 'h' and h != 0:
				print('Esta casa já possui um valor tente em outra')
				continue
			elif valor == 'i' and i != 0:
				print('Esta casa já possui um valor tente em outra')
				continue
			else: # verificam o que o jogador digitou e atribuem este valor a sua casa correspondente
				if valor == 'a': a = vez 
				elif valor == 'b': b = vez
				elif valor == 'c': c = vez
				elif valor == 'd': d = vez
				elif valor == 'e': e = vez
				elif valor == 'f': f = vez
				elif valor == 'g': g = vez
				elif valor == 'h': h = vez
				elif valor == 'i': i = vez
				else:
					print('Algum erro ocorreu')
				disponiveis.remove(valor)
				print('Processando...')
				sleep(0.3)
				break
				
	elif jogada % 2 != 0: # esta é a vez do computador ele escolhe uma letra nas disponiveis 
		valor = choice(disponiveis)
		disponiveis.remove(valor)
	
		if valor == 'a': # verificam a escolha da cpu e atrnuem a sua casa correspondente
			a = vez
			atual = 'a' # serve para depois imprimir a escolha da cpu
		elif valor == 'b':
			b = vez	
			atual = 'b'
		elif valor == 'c':
			c = vez
			atual = 'c'
		elif valor == 'd':
			d = vez
			atual = 'd'
		elif valor == 'e':
			e = vez
			atual = 'e'
		elif valor == 'f':
			f = vez
			atual = 'f'
		elif valor == 'g':
			g = vez
			atual = 'g'
		elif valor == 'h':
			h = vez
			atual = 'h'
		elif valor == 'i':
			i = vez
			atual = 'i'

		print('\nminha vez...\n')
		sleep(0.5)
		print('joguei na casa {}\n'.format(atual))
		sleep(0.5)
	
	# por fim imprime as variaveis com seus respectivos valores organizados na velha
	print(''' 
	{} | {} | {}
      -------------
	{} | {} | {}
      -------------
	{} | {} | {}
	'''.format(a, b, c, d, e, f, g, h, i))
	
	if jogada >= 3: # apartir de 3 valores na velha ele começa a verificar 
	
		if a == vez and b == vez and c == vez: # verificam se qualquer uma das 8 alternativas foi..-
			if vez == 'X':	#-... atendida se qualquer condição for True ele verifica a variavel vez ...-
				print('GANHOU! parabéns você ganhou') #...- e imprime quem ganhou
			elif vez == 'C':
				print('Ganhei! hehehe eu Ganhei!')
			break
			
		elif d == vez and e == vez and f == vez:
			if vez == 'X':
				print('GANHOU! parabéns você ganhou')
			elif vez == 'C':
				print('Ganhei! hehehe eu Ganhei!')
			break
			
		elif g == vez and h == vez and i == vez:
			if vez == 'X':
				print('GANHOU! parabéns você ganhou')
			elif vez == 'C':
				print('Ganhei! hehehe eu Ganhei!')
			break
			
		elif a == vez and d == vez and g == vez:
			if vez == 'X':
				print('GANHOU! parabéns você ganhou')
			elif vez == 'C':
				print('Ganhei! hehehe eu Ganhei!')
			break
	
		elif b == vez and e == vez and h == vez:
			if vez == 'X':
				print('GANHOU! parabéns você ganhou')
			elif vez == 'C':
				print('Ganhei! hehehe eu Ganhei!')
			break
	
		elif c == vez and f == vez and i == vez:
			if vez == 'X':
				print('GANHOU! parabéns você ganhou')
			elif vez == 'C':
				print('Ganhei! hehehe eu Ganhei!')
			break
		
		elif a == vez and e == vez and i == vez:
			if vez == 'X':
				print('GANHOU! parabéns você ganhou')
			elif vez == 'C':
				print('Ganhei! hehehe eu Ganhei!')
			break
	
		elif c == vez and e == vez and g == vez:
			if vez == 'X':
				print('GANHOU! parabéns você ganhou')
			elif vez == 'C':
				print('Ganhei! hehehe eu Ganhei!')
			break
		else:
			print('\nPor enquanto ninguem ganhou!\n')
			print('Tecle enter para continuar')
			input()
		
	jogada += 1

print('\nFim do Código\n')




