# Modularização em python

import aula21_operacoes
# from aula21_operacoes import somar, subtrair

def executar_calculadora():
    print("--- Calculadora Modularizada ---")
    
    num1 = 10
    num2 = 5
    
    # Usando as funções através do nome do módulo
    soma = aula21_operacoes.somar(num1, num2)
    subtracao = aula21_operacoes.subtrair(num1, num2)
    multiplicacao = aula21_operacoes.multiplicar(num1, num2)
    divisao = aula21_operacoes.dividir(num1, num2)
    
    print(f"Soma: {num1} + {num2} = {soma}")
    print(f"Subtração: {num1} - {num2} = {subtracao}")
    print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
    print(f"Divisão: {num1} / {num2} = {divisao}")

# Executa a função principal
if __name__ == "__main__":
    executar_calculadora()