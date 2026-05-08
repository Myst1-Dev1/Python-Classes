'''
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex: 746.824.890-70(746824890)
    10 9 8 7 6 5 4 3 2
    7 4 6 8 2 4 8 9 0
    70 36 48 56 12 20 32 27 0

Somar todos os resultados :
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 1
Se o resultado anterior for maior que 9:
    o resultado é 0
contrário disso:
    o resultado é o valor da conta
o primeiro digito do CPF é 7
'''

# cpf = '74682489070'
# nove_digitos = cpf[:9]
# # Variável que vai armazenar a soma total
# soma = 0

# # Contador regressivo começando em 10
# contador = 10

# # Percorre cada número do CPF
# for numero in nove_digitos:
#     soma += int(numero) * contador
#     contador -= 1

# print('Soma:', soma)

# # Multiplica por 10
# resultado = soma * 10

# print('Resultado x10:', resultado)

# # Pega o resto da divisão por 11
# digito = resultado % 11

# print('Resto da divisão:', digito)

# # Se for maior que 9, vira 0
# digito = digito if digito <= 9 else 0

# print('Primeiro dígito:', digito)