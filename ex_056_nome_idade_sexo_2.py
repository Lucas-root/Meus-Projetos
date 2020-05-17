# Reescrita do programa 1 

soma_idades = 0
idades_vinte = 0
t_h = 0
t_f = 0

for c in range(0, 4): # Vai repetir 4 vazes 

    nome = str(input('\nDigite o nome desta pessoa : '))
    idade = int(input('Digite a idade desta pessoa : '))
    sexo = str(input('Digite o sexo desta pessoa : '))
    
    soma_idades += idade

    if sexo == 'masculino' or sexo == 'm':
        if t_h == 0 and sexo == 'masculino' or t_h == 0 and sexo == 'm':
            nome_masculino = nome 
            idade_homem = idade 
            t_h = 1
        elif idade > idade_homem:
            nome_masculino = nome
            idade_homem = idade

    elif sexo == 'feminino' or sexo == 'f':
        if t_f == 0 and sexo == 'feminino' or t_f == 0 and sexo == 'f':
            nomes_femininos = ['nome']
            t_f = 1
            if idade < 20:
                idades_vinte += 1

        elif idade < 20:
            idades_vinte += 1
            nomes_femininos.append(nome)

media_idades = soma_idades / 4

print('\nA média de idade do grupo é de {:.0f} anos'.format(media_idades))
if idades_vinte > 1:
    print('{} mulheres possuem menos do que vinte anos de idade'.format(idades_vinte))
elif idades_vinte == 1:
    print('A penas uma mulher possui menos do que vinte anos de idade')
else:
    print('Nenhuma mulher possui menos do que vinte anos de idade')
print('E {} que contem {} anos de idade é o homem mais velho deste grupo.'.format(nome_masculino.title(), idade_homem))

print('\nFim do código\n')

