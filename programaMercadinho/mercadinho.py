produtos = {
			'bolacha':3.90, 
			'pão':5.00
			}

comandos = {
			'adicionar':'Permite adicionar itens a lista de produtos',
			'sair':'Permite encerrar a aplicação.',
			'estoque':'imprime os produtos na lista de produtos',
			'remover':'Permite a remoção de um item na lista de produtos'
			}

while True:

	comando = input('\nDigite algum comando ou Digite "help" para ver a lista completa : ')

	if comando == 'help': (print(comandos))

	elif comando == 'sair': break
	
	elif comando == 'estoque': print(produtos)

	elif comando == 'adicionar':
		item = input('Digite o nome do item a ser adicionado : ')
		preco = input('Digite o preço do item a ser adicionado : ')
		produtos[item] = preco
		print(produtos)

	elif comando == 'remover':
		while True:
			deletar = input('Digite o nome do item a ser deletado : ')
			verifica = deletar in produtos
			if deletar == 'sair': break
			elif verifica: # True se o item passado para deletar estiver na lista de produtos
				del produtos[deletar]
				print('\nitem removido {}'.format(deletar))
				print('Estado atual da lista de produtos : ')
				print(produtos)
				break
			else:
				print('\nEste item não está na lista de produtos')
				print('tente novamente ou digite "sair" para retornar ao inicio\n')

	else:
		print('\nPor favor, digite um comando valido')

print('\nFim do código')
