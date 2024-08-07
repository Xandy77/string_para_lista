# variável
#nome = 'John Connor'

# separa a string em uma lista
#nome_completo = nome.split(' ')

# exibe a lista
#for parte_nome in nome_completo:
#    print(parte_nome, end= ' ')

# usuário informa o nome
nome = input('Informe o seu nome completo: ')

# separa as palavras do nome
nome_lista = nome.split(' ')

for i in range(len(nome_lista)):
    nome_lista[i] = nome_lista[i].capitalize()
   
# junta o nome em uma variável
nome_completo = ' '.join(nome_lista)

# exibe na lista
print(nome_completo)