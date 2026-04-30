"""
Iterando strings com while
"""

nome = 'Myst Vas'
tamanho_nome = len(nome)

nova_string = ''

i = 0

while i < tamanho_nome:
    nova_string += nome[i]
    
    if i < tamanho_nome - 1:
        nova_string += '*'
    
    i += 1

print(nova_string)