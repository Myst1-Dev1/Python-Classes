"""
# Introdução ao try/except

try -> tentou executar o código
except -> ocorreu algum erro ao executar o código

"""

numero_string = input('Vou dobrar o número que você digitar: ')

try:
    numero_int = int(numero_string)
    print(f'O dobro de {numero_int} é {numero_int * 2}')
except:
    print('Isso não é um número inteiro válido.')