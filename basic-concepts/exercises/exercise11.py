'''
Calculo do segundo digito do CPF
CPF: 746.824.890-70
colete a soma dos 9 primeiros digitos do cpf,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma contagem regressiva começando de 11

Ex: 746.824.890-70(746824890)
    11 10 9 8 7 6 5 4 3 2
*   7  4 6 8 2 4 8 9 0 7 -> PRIMEIRO DIGITO
    77 40 54 64 14 24 40 36 0 14

Somar todos os resultados
77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    o resultado é 0
contrário disso:
    o resultado é o valor da conta
o segundo digito do CPF é 0
'''

cpf = '746.824.890-70' \
    .replace('.', '') \
    .replace('-', '')
nove_digitos = cpf[:9]
soma = 0

contador = 10

for numero in nove_digitos:
    soma += int(numero) * contador
    contador -= 1

print('Soma:', soma)

resultado = soma * 10

print('Resultado x10:', resultado)

digito = resultado % 11

print('Resto da divisão:', digito)

digito = digito if digito <= 9 else 0

print('Primeiro dígito:', digito)

dez_digitos = nove_digitos + str(digito)
contador_2 = 11
soma_2 = 0

for digito in dez_digitos:
    soma_2 += int(digito) * contador_2
    contador_2 -= 1
    
print('Soma dos 10 dígitos:', soma_2)
resultado_2 = soma_2 * 10
print('Resultado x10:', resultado_2)
digito_2 = resultado_2 % 11
print('Resto da divisão:', digito_2)
digito_2 = digito_2 if digito_2 <= 9 else 0

print('O Segundo dígito do CPF é:', digito_2)