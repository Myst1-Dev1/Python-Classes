# Função lambda em python
# A função lambda é uma função como qualquer outra em python
# porém são funções anónimas que contem apenas uma linha
# ou seja tudo deve ser contido dentro de uma única expressão

lista = [
   {'nome': 'peter', 'sobrenome': 'parker'},
   {'nome': 'myst', 'sobrenome': 'vas'},
   {'nome': 'laura', 'sobrenome': 'schneider'},
   {'nome': 'clark', 'sobrenome': 'pente'},
]


# def ordena(item):
#     return item['nome']

lista.sort(key=lambda x: x['nome'])

for item in lista:
    print(item)