# Sets em python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

# Criando um set em python

# s1 = set() #Set vazio
# s1 = { 'Myst', 1, 2, 3 } #Set com dados

# Sets são eficientes para remover valores duplicados de iteráveis
# Seus valores sempre serão únicos
# - não aceitam valores mutáveis
# - eles não tem indexes
# - eles não garantem ordem
# - eles são iteráveis (for in,  not in)

# Metodos uteis
# add, update, clear, discard

# Operadores uteis
# união | união (union) - Une
# intersecção & intersection - Items presentes em ambos
# diferença - Item presentes apenas no set da esquerda
# diferença simetrica ^ - Items que não estão em ambos

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}

# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s1 - s2
# s3 = s1 ^ s2

# print(s3)


#Exemplo de uso dos sets

letras = set()
attemptives = 3

print('Descubra o animal misterioso')
print('DICA: um animal doméstico')

while True :
    letra = input('digite o nome de um animal: ')
    letras.add(letra.lower())

    if 'gato' in letras:
        print('Parabéns, você encontrou o animal')
        break
    else:
        attemptives -= 1
        print(f'Errou! Você ainda tem {attemptives} tentativa(s).')

    if len(letras) == 3:
        print('Suas tentativas acabaram')
        break
print(letras)