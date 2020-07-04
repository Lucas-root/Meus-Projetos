produtos = {
			'bolacha':3.90, 
			'pão':5.00
			}

while True:

	comando = input('\nDigite algum comando ou Digite "help" para ver a lista completa : ')

	if comando == 'help':
		comandos = {
					'adicionar':'Permite adicionar itens a lista de produtos',
					'sair':'Permite encerrar a aplicação.'
				   }
		print(comandos)

	elif comando == 'sair':
		break

	elif comando == 'adicionar':
		item = input('Digite o nome do item a ser adicionado : ')
		preco = input('Digite o preço do item a ser adicionado : ')
		produtos[item] = preco
		print(produtos)

	else:
		print('\nPor favor, digite um comando valido')

print('\nFim do código')
