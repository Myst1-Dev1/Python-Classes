# try except. else e finally

def dividir(a, b):
    try:
        # Tenta realizar a operação de risco
        resultado = a / b
    except ZeroDivisionError as error:
        # Executado se houver divisão por zero
        print(f"Erro: {error}!")
    else:
        # Executado se o 'try' rodar 100% sem erros
        print(f"Sucesso! O resultado é {resultado}")
    finally:
        # Executado sempre, aconteça o que acontecer
        print("Bloco finally: Limpeza ou finalização executada.\n")

# Testando a função:
print("--- Teste 1: Divisão válida ---")
dividir(10, 2)

print("--- Teste 2: Divisão por zero (Erro) ---")
dividir(10, 0)