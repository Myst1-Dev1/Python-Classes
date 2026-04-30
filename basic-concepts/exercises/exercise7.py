# Calculadora com while

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, *, /): ")

while operacao not in ['+', '-', '*', '/']:
    print("Operação inválida. Tente novamente.")
    operacao = input("Digite a operação (+, -, *, /): ")

if operacao == '+':
    resultado = numero_1 + numero_2
elif operacao == '-':
    resultado = numero_1 - numero_2
elif operacao == '*':
    resultado = numero_1 * numero_2
else:
    resultado = numero_1 / numero_2

print(f"O resultado da operação {numero_1} {operacao} {numero_2} é: {resultado}")