# author : lucasedux0@gmail.com

comandos = {
	'help':'exibe todos os comandos disponiveis',
}

estoque = {
	'doces':{
		'bolachas':{
			'bel-vita':4.99,
		},
		'chocolates':{
			'barras':{
				'diamante-negro':{
					'50g':3.00,
					'100g':5.49,
				},
			},
		},
	},
	'bebidas':{
		'vinhos':{
			'vinho-branco':20.99,
		},
	},
	'laticinios':{
		'leites':{
			'terra-viva':3.49,
			'piracanjuba':4.50,
		},
		'queijos':{
			'brancos':{
				'seara':{
					'100g':5.00,
				},
			},
		},	
	},
}

print()

for item in estoque:
	print(item.upper())
	for subp in estoque[item]:
		print('\t',subp)
		for subf in estoque[item][subp]:
			print('\t'*2, subf)
		print()
	print()



















