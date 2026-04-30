# Repetições While (enquanto) executa uma ação enquanto um condição for verdadeira

# condicao = True

# while condicao:
#     nome = input('Digite seu nome: ')
#     print(f'Olá {nome}!')

#     if nome == 'sair':
#         break # Interrompe o loop

# contador = 0

# while contador <= 5:
#     print(f'Contagem: {contador}')
#     contador += 1

# print('Fim do programa')

# Operadores de atribuição + += -= *= /= //= %=

# contador = 0

# while contador <= 100:
#     contador += 1

#     if contador == 6:
#         continue # Pula a iteração atual e continua para a próxima

#     print(f'Contagem: {contador}')

#     if contador == 40:
#         break # Interrompe o loop

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    print(linha)

    while coluna <= qtd_colunas:
        print(f'Linha {linha} - Coluna {coluna}')
        coluna += 1

    linha += 1

print('Acabou o loop')