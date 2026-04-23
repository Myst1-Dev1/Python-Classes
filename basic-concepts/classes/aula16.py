"""
Interpolaçao básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

# nome = 'luiz'
# preco = 1000.958976
# variavel = '%s, o preço é R$%.2f' % (nome, preco)
# print(variavel)
# print('O hexadecimal de %d é %08X' % (1500, 1500))


"""
Formataçao básica de strings
s - string
d - int
f - float
.<número de digitos>f x ou X Hexadecimal (Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex: 0>100,.1f
Conversion flags - !r !s !a
"""

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')