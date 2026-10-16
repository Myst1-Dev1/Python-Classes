# Crie uma funçao zipper (como o zipper de roupas)
# o trabalho dessa funçao sera unir duas listas na ordem
# Use todos os valores da menor lista
# Ex: ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG' 'RJ']
# Resultado: [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest

def zipper(lista1, lista2):
    return [(lista1[i], lista2[i]) for i in range(min(len(lista1), len(lista2)))]

# Testando com os seus dados
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

resultado_esperado = zipper(cidades, estados)
print(resultado_esperado)

print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados, fillvalue='SEM CIDADE')))