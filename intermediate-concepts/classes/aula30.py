# groupby - agrupando valores (itertools)

'''
A regra de ouro do groupby do módulo itertools é: os dados precisam estar ordenados pela mesma 
chave de agrupamento antes de usar a função. O groupby apenas agrupa itens consecutivos que são iguais.

Para conectar com seus interesses, fiz um exemplo focado em Cibersegurança/Análise de Dados. 
Vamos imaginar que você tem uma lista de logs de IPs e quer agrupá-los pelo status de 
acesso (bloqueado, permitido ou em análise).

'''

from itertools import groupby

# Nossa base de dados fictícia (lista de dicionários)
logs_de_rede = [
    {'ip': '192.168.0.1', 'status': 'bloqueado'},
    {'ip': '192.168.0.2', 'status': 'permitido'},
    {'ip': '192.168.0.3', 'status': 'bloqueado'},
    {'ip': '10.0.0.1', 'status': 'permitido'},
    {'ip': '10.0.0.2', 'status': 'em_analise'},
]

# 1. Função que ensina o Python por qual chave queremos ordenar/agrupar
def chave_de_agrupamento(log):
    return log['status']

# 2. OBRIGATÓRIO: Ordenar a lista usando a mesma chave
logs_de_rede.sort(key=chave_de_agrupamento)

# 3. Agrupar os dados
grupos_de_logs = groupby(logs_de_rede, key=chave_de_agrupamento)

# 4. Iterar sobre os grupos
for status, grupo in grupos_de_logs:
    print(f"\n--- IPs com status: {status.upper()} ---")
    
    # O 'grupo' é um iterador, precisamos fazer um for para ver os itens dentro dele
    for log in grupo:
        print(f"  > {log['ip']}")