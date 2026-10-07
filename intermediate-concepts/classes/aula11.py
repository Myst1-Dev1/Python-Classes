# Dictionary comprehension e Set comprehension

produto = {
    'nome':'caneta azul',
    'preco':24,
    'categoria': 'Escritorio'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

print(dc)

s1 = {i ** 2 for i in range(10)}

print(s1)