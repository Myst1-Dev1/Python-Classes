'''
Crie uma função que multiplica todos os argumentos não nomeados recebidos
retorne o total para uma variável e mostre o valor da variavel.
'''

def multiply(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado = multiply(2,3,4)
print(resultado)





'''
Crie uma função fala se um número é par ou impar
Retorne se o número é par ou impar
'''

def oddOrEven(x):
    if(x % 2 == 0):
        return 'O número é par'
    else:
        return 'O número é impar'

print(oddOrEven(2))