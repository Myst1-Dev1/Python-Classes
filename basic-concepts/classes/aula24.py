'''
Listas em python
tipo list -> Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis -> indice e fatiamento
Métodos uteis -> append, insert, pop, del, clear, extend, +
'''

# lista = ['pão', 'leite', 'frutas', 'carne', 'verduras']
# print('Lista: ' + str(lista))
# lista.append('ovos')  # Adiciona um item no final da lista'
# print('Lista após append: ' + str(lista))
# lista.insert(2, 'água')  # Adiciona um item no indice especificado
# print('Lista após insert: ' + str(lista))
# lista.pop(3)  # Remove o item do indice especificado
# print('Lista após pop: ' + str(lista))
# del lista[2]  # Remove o item do indice especificado
# print('Lista após del: ' + str(lista))
# lista.clear()  # Limpa a lista
# print('Lista após clear: ' + str(lista))

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b  # Concatena as listas
# print(lista_c)

# lista_a.extend(lista_b)  # Extende a lista_a com os itens da lista_b
# print(lista_a)

'''
for in com listas
'''

nomes = ['Laura', 'Veronica', 'Sara', 'Beatrice']
indices = range(len(nomes))

for indice in indices:
    print(indice, nomes[indice])