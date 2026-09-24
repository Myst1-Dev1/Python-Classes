import copy

# Dicionários em Python(tipoe dict)

# person = {
#     'name': 'John',
#     'surname': 'Doe',
#     'age': 24,
#     'address': [
#         {'street': 'street silver', 'number': 64}
#     ]
# }

# tasks = {}

# tasks['1'] = {
#     'name' : 'Limpar a gaveta',
#     'type': 'Domestico'
# }

# tasks['2'] = {
#     'name' : 'Limpar o teclado',
#     'type': 'tecnologico'
# }

# if tasks.get('1') is None:
#     print('A tarefa não existe')
# else:
#     print(f"A tarefa {tasks['1']['name']} existe")

# print(tasks)


#Metodos uteis dos dicionários em python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com as chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma copia rasa (shallow copy)
# get - obtem uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o ultimo item correspondente
# update - atualiza um dicionario com o outro


pokemons1 = {
    '0447': {'name': 'Riolu', 'type': 'Fighting'},
    '0172': {'name': 'Pichu', 'type': 'Electric'},
    '0007': {'name': 'Squirtle', 'type': 'Water'}
}
# print(list(pokemons1.values()))
# chaves = pokemon12.keys()
# print(chaves)
# print(list(pokemons1.keys()))

#Copia rasa

pokemons2 = {
    '0007': {'name': 'Squirtle', 'type': 'Water'}
}

# Criando uma cópia real usando .copy()
copia_segura = pokemons2.copy()

# Se adicionarmos ou trocarmos uma chave no nível principal, o original não sofre alterações:
copia_segura['025'] = {'name': 'Pikachu', 'type': 'Electric'}

print('025' in pokemons2)       # Saída: False (O original continua intacto!)
print('025' in copia_segura)   # Saída: True

#deepcopy

import copy

pokemons3 = {'0007': {'name': 'Squirtle', 'type': 'Water'}}
copia_profunda = copy.deepcopy(pokemons3)

# Agora sim, mexer em qualquer nível interno não afeta o original
copia_profunda['0007']['name'] = 'Blastoise'
print(pokemons3['0007']['name'])     # Saída: Squirtle (Seguro!)
print(copia_profunda['0007']['name']) # Saída: Blastoise