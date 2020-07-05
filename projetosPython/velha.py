from random import randint 
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0 
h = 0 
i = 0 
posibilidades = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
jogada = -1

for i in range(1, 10): # ele vai repetir 9 vezes. O (i) vai receber de 1 até 9
	
	jogada += 1

	if  jogada % 2 == 0:
		vez = 'X'
	elif jogada % 2 != 0:
		vez = 'O'
	else:
		print('O correu um erro. Esta mensagem é referente a linha 17')

	if jogada % 2 == 0:
		while True:
			valor = input('Digite a casa a ser jogada : ')
			if not valor in posibilidades: # se o valor não estiver em posibilidades True 
				print('Digite uma casa valida : ')
			elif valor == 'a' and a != 0:
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
			else:
				if valor == 'a': a = vez 
				elif valor == 'b': b = vez
				elif valor == 'c': c = vez
				elif valor == 'd': d = vez
				elif valor == 'e': e = vez
				elif valor == 'f': f = vez
				elif valor == 'g': g = vez
				elif valor == 'h': h = vez
				elif valor == 'i': i = vez
				break
				else:
					print('Algum erro ocorreu')
					break

	elif jogada % 2 != 0:
		aleatorio = randint(1, 9)
		if aleatorio == 1:
			valor = 'a'
		elif aleatorio == 2:
			valor = 'b'
		elif aleatorio == 3:
			valor = 'c'	
		elif aleatorio == 4:
			valor = 'd'
		elif aleatorio == 5:
			valor = 'e'
		elif aleatorio == 6:
			valor = 'f'
		elif aleatorio == 7:
			valor = 'g'
		elif aleatorio == 8:
			valor = 'h'
		elif aleatorio == 9:
			valor = 'i'
		else:
			print('Algum erro ocorreu !')	

	
	if valor == 'a':
		a = vez
	elif valor == 'b':
		b = vez	
	elif valor == 'c':
		c = vez
	elif valor == 'd':
		d = vez
	elif valor == 'e':
		e = vez
	elif valor == 'f':
		f = vez
	elif valor == 'g':
		g = vez
	elif valor == 'h':
		h = vez
	elif valor == 'i':
		i = vez


