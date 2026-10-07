# List comprehension em python
# List comprehension é uma forma rapida para criar listas a partir de iteráveis

'''
List Comprehension com Operador Ternário em Python
Uma das formas mais elegantes e pythônicas de criar listas dinâmicas 
combinando repetição e tomada de decisão em uma única linha de código.
'''

# lista = ['Par' if numero % 2 == 0 else 'impar' for numero in range(10)]

# print(lista)

'''
💡 Como funciona:
O Operador Ternário (if/else no meio): 'Par' if numero % 2 == 0 else 'Ímpar' define o valor que será 
adicionado com base na condição.

O Loop (for no final): for numero in range(10) percorre os elementos iteráveis, substituindo o 
tradicional bloco for com .append() por uma sintaxe limpa e de alta performance.
'''

# Mapeamento de dados em list comprehension

# produtos = [
#     {'nome': 'teclado', 'preco': 200},
#     {'nome': 'mouse', 'preco': 100},
#     {'nome': 'monitor', 'preco': 500},
# ]

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]

# print(*novos_produtos, sep='\n')

# Filtro

# frutas = [
#     {'nome': 'maça', 'kg': 200},
#     {'nome': 'banana', 'kg': 300},
#     {'nome': 'pera', 'kg': 400},
# ]

# frutas2 = [
#     {**fruta, 'kg': fruta['kg']} # Mapeamento
#     for fruta in frutas
#     if fruta['kg'] >= 300 # Filtro
# ]

# print(*frutas2, sep='\n')