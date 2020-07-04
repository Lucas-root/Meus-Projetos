produtos = {
			'bolacha':3.90, 
			'pão':5.00
			}

comandos = {
			'adicionar':'Permite adicionar itens a lista de produtos',
			'sair':'Permite voltar ao menu anterior ou encerra a aplicação.',
			'estoque':'imprime os produtos na lista de produtos',
			'remover':'Permite a remoção de um item na lista de produtos'
			}

while True:

	comando = input('\nDigite algum comando ou Digite "help" para ver a lista completa : ')

	if comando == 'help': (print(comandos)) # imprime o dicionario de comandos 

	elif comando == 'sair': break # enerra a aplicação
	
	elif comando == 'estoque': print(produtos)

	elif comando == 'adicionar': # permite adicionar um item a lista de produtos 
		item = input('Digite o nome do item a ser adicionado : ')
		preco = input('Digite o preço do item a ser adicionado : ')
		produtos[item] = preco
		print(produtos)

	elif comando == 'remover': # comanado remover que permite a remoção de um item da lista
		while True:
			deletar = input('Digite o nome do item a ser deletado : ')
			verifica = deletar in produtos # recebe True caso o item passado pelo usuario esteja na lista 

			if deletar == 'sair': break # comando para sair caso o usuario no lugar de um item passe 'sair'

			elif verifica: # True se o item passado para deletar estiver na lista de produtos
				continua = input('Você realmente deseja remover {} da lista ? (s/n)'.format(deletar))
				
				# esta é uma confirmação para evitar de remover um item não desejado
				if continua == 's' or continua == 'sim' or continua == 'S':
					del produtos[deletar]
					print('\nitem removido {}'.format(deletar))
					print('Estado atual da lista de produtos : ')
					print(produtos)
					break

				else: # caso o usuario digite algo diferente de s, sim ou S
					print('\nItem {} não removido'.format(deletar))
					print('Estado atual da lista de produtos : ')
					print(produtos)

			else:
				print('\nEste item não está na lista de produtos')
				print('tente novamente ou digite "sair" para retornar ao inicio\n')

	else:
		print('\nPor favor, digite um comando valido')

print('\nFim do código')
