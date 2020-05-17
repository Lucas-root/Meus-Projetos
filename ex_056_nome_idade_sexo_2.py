# Programa para ler o nome, idade, sexo de quatro pessoas e imprimir : a idade do grupo, quem é o homem mais velho e 
# quantas mulheres possuem menos do que 20 anos

# programa ainda em melhoria

soma_idades = 0 # cria a variavel que ira somar a idade de todas as pessoas para depois tirar a sua média
idades_vinte = 0 # cria a variavel que irá guardar quantas mulheres possuem menos do que vinte anos de idade 
t_h = 0 # as variaveis t_h e t_f com o valor 0 sinalizam que ainda nenhum homem/mulher preecheram este formulario quando
t_f = 0 # um h/m preencer a variavel referente tomara o valor de 1 

for c in range(0, 4): # Vai perguntar nome, idade e sexo 4 vezes

    nome = str(input('\nDigite o nome desta pessoa : ')) #  estas variaveis guardam temporariamente estes dados
    idade = int(input('Digite a idade desta pessoa : ')) # para enviar a outras variaveis os dados relevantes
    sexo = str(input('Digite o sexo desta pessoa : '))
    
    soma_idades += idade # Soma todas as idades que forem digitadas Para depois tirar a média delas

    if sexo == 'masculino' or sexo == 'm': # verifica se o sexo digitado foi o masculino
        if t_h == 0 and sexo == 'masculino' or t_h == 0 and sexo == 'm': #Verifica se é a primeira execussão para o sexo m 
            nome_masculino = nome # se for a primeira execussão ele guarda os valores digitados nestas duas variaveis 
            idade_homem = idade # estas duas variaveis estão guardando o nome e a idade do do primeiro homem 
            t_h = 1 # está variavel sinaliza que as variaveis acima já possuem algum valor
        elif idade > idade_homem: # verifica se a idade digitada é maior do que a idade da variavel idade_homem
            nome_masculino = nome # guarda o nome do homem que possui a idade mais alta
            idade_homem = idade # se este elif for true ele rescreve a idade em idade_homem 

    elif sexo == 'feminino' or sexo == 'f': # verifica se o sexo digitado foi o feminino 
        if t_f == 0 and sexo == 'feminino' or t_f == 0 and sexo == 'f': # T se for o primeiro preenchimento de uma mulher
            nomes_femininos = ['nome'] # guarda os nomes das mulheres (no momento está sem uso)
            t_f = 1 # Altera para 1 para sinalizar que já foi preenchido 
            if idade < 20: # se a idade da mulher em questão for menor que 20 
                idades_vinte += 1 # guarda nesta variavel quantas mulheres possuem < do que 20 anos

        elif idade < 20: # caso não seje o primeiro preenchimento de uma mulher e ela tiver < que 20 anos
            idades_vinte += 1 # Adiciona 1 a variavel que armazena quantas mulheres possuem < que vinte anos 
            nomes_femininos.append(nome) # adiciona o nome a lista de nomes de mulheres (no momento sem uso)

media_idades = soma_idades / 4 # armazena a media de idades do grupo

# e finalmente imprime as mensagens
print('\nA média de idade do grupo é de {:.0f} anos'.format(media_idades))
if idades_vinte > 1:
    print('{} mulheres possuem menos do que vinte anos de idade'.format(idades_vinte))
elif idades_vinte == 1:
    print('A penas uma mulher possui menos do que vinte anos de idade')
else:
    print('Nenhuma mulher possui menos do que vinte anos de idade')
print('E {} que contem {} anos de idade é o homem mais velho deste grupo.'.format(nome_masculino.title(), idade_homem))

print('\nFim do código') # só sinaliza que o programa terminou

