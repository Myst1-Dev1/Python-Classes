# introducao ao for / in

# texto = 'python'
# novo_texto = ''

# for letra in texto:
#     novo_texto += f'*{letra}'
# print(novo_texto)

'''
For + Range
range -> range(start, stop, step)

'''

# numeros = range(0, 100, 5)

# for valor in numeros:
#     print(valor)

'''
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''

# texto = 'Myst'
# iterador = iter(texto)

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

'''
o que aprendemos no while também funciona no for(continue, break, else, etc)
'''

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso !')