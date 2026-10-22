# reduce - faz a redução de um iterável em um valor

'''
A função reduce pega uma lista de dados (iterável) e a "esmaga" (reduz) até sobrar um único valor. 
Para isso, ela usa uma função que recebe sempre dois parâmetros: um acumulador e o item atual.

Diferente do map e do filter, o reduce não vem "solto" no Python. Você precisa importá-lo do módulo 
functools.

Aqui estão dois exemplos de como isso funciona na prática.
'''

# Exemplo 1: O Clássico (Somando valores)
# Para Ciência de Dados, imagine que você tem uma lista com o tamanho de vários arquivos em 
# Megabytes e quer saber o tamanho total.

from functools import reduce

tamanhos_arquivos_mb = [10, 50, 30, 20]

# O reduce funciona em passos:
# Passo 1: acumulador=0, item=10 -> resultado=10
# Passo 2: acumulador=10, item=50 -> resultado=60
# Passo 3: acumulador=60, item=30 -> resultado=90
# Passo 4: acumulador=90, item=20 -> resultado=110

total_mb = reduce(
    lambda acumulador, item: acumulador + item, # Função
    tamanhos_arquivos_mb,                       # Iterável
    0                                           # Valor inicial do acumulador (Boas práticas)
)

print(f"Tamanho total: {total_mb} MB")
# Saída: Tamanho total: 110 MB

#Exemplo 2: Cibersegurança (Encontrando o maior risco)
# O reduce não serve apenas para matemática básica. Você pode usá-lo para reduzir uma lista de 
# dicionários ao dicionário que contém a informação mais crítica.

# Vamos imaginar uma lista de servidores e seus níveis de vulnerabilidade. Queremos reduzir essa 
# lista para encontrar qual é o servidor mais perigoso no momento.

servidores = [
    {'nome': 'Web', 'score_risco': 4},
    {'nome': 'Banco_Dados', 'score_risco': 9},
    {'nome': 'Email', 'score_risco': 2},
    {'nome': 'Backup', 'score_risco': 7}
]

# Função que compara o acumulador com o item atual
def manter_maior_risco(acumulador, item_atual):
    # Se o risco do item atual for maior que o do acumulador, ele vira o novo acumulador
    if item_atual['score_risco'] > acumulador['score_risco']:
        return item_atual
    
    # Caso contrário, mantemos o acumulador como estava
    return acumulador

# Como não passamos um valor inicial (3º parâmetro), o reduce 
# usa o primeiro item da lista como acumulador inicial.
servidor_mais_critico = reduce(manter_maior_risco, servidores)

print(f"ATENÇÃO! Maior risco no servidor: {servidor_mais_critico['nome']}")
# Saída: ATENÇÃO! Maior risco no servidor: Banco_Dados

'''
O professor Luiz Otávio costuma bater muito na tecla do valor inicial (o terceiro parâmetro do reduce).
Se você está somando números, coloque 0. Se está multiplicando, coloque 1. Se estiver trabalhando 
com dicionários, às vezes é melhor passar um dicionário inicial vazio ou base para evitar erros caso 
a lista esteja vazia.
'''