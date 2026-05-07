'''
Introdução ao desempacotamento + tuples (tuplas)
'''

# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
# print(nome2)

# _,_, nome2, *resto = ['Maria', 'Helena', 'Luiz', 'João', 'Eduardo']
# print(nome2)

'''
Tipo Tupla -> uma lista imutável, ou seja, não pode ser alterada.
As tuplas são representadas por parênteses () e os elementos são separados por vírgulas.
'''

# nomes = ('Maria', 'Helena', 'Luiz')
# print(nomes[1])

'''
Enumerate -> enumera iteráveis(indices)
'''

lista = ['Maria', 'Helena', 'Luiz']
for indice, nome in enumerate(lista):
    print(indice, nome)