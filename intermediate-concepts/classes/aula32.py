# filter - é um filtro funcional

'''
A função filter faz exatamente o que o nome diz: filtra os dados de um iterável.

Para usá-la, você passa uma função que deve obrigatoriamente retornar True ou False. O 
filter vai testar cada item do iterável nessa função: se retornar True, o item entra no resultado 
final; se retornar False, o item é descartado.

Aqui estão dois exemplos práticos voltados para as suas áreas de interesse.
'''

# Exemplo 1: Cibersegurança (Filtrando logs de invasão)
# Imagine que você tem uma lista de dicionários representando logs do sistema 
# e precisa isolar apenas as tentativas de login que falharam.

# Nossa base de logs
logs = [
    {'usuario': 'admin', 'acao': 'login_falhou', 'ip': '203.0.113.5'},
    {'usuario': 'joao',  'acao': 'login_sucesso', 'ip': '192.168.1.25'},
    {'usuario': 'root',  'acao': 'login_falhou', 'ip': '198.51.100.22'},
    {'usuario': 'maria', 'acao': 'logout',        'ip': '192.168.1.30'},
]

# 1. Função que retorna True ou False
def filtro_falhas(log):
    return log['acao'] == 'login_falhou'

# 2. Aplicando o filter(função, iterável)
logs_suspeitos = filter(filtro_falhas, logs)

# Convertendo o iterador para lista para visualizar
lista_suspeitos = list(logs_suspeitos)

for alerta in lista_suspeitos:
    print(f"ALERTA: Falha de login do usuário '{alerta['usuario']}' no IP {alerta['ip']}")

# Exemplo 2: Ciência de Dados usando lambda (Detecção de anomalias)
# Assim como no map, é muito comum usar funções anônimas (lambda) com o filter para códigos curtos.
# Vamos supor que você está analisando um conjunto de transações bancárias e quer filtrar 
# apenas valores "anômalos" (muito altos, digamos, acima de R$ 10.000) para investigação.

transacoes = [150.0, 3000.50, 20.0, 15000.0, 8.50, 55000.0, 450.0]

# Filtra mantendo apenas os valores onde a condição (t > 10000) for True
transacoes_suspeitas = list(filter(lambda t: t > 10000, transacoes))

print("Transações para investigar:", transacoes_suspeitas)
# Saída: Transações para investigar: [15000.0, 55000.0]

'''
A grande vantagem do filter:
Assim como o map e o groupby, o filter retorna um iterador. Ele não cria uma nova lista gigante 
na memória do seu computador imediatamente, ele vai te entregando os valores filtrados um por 
um conforme você pede. Isso é excelente para lidar com gigabytes de dados de rede ou tabelas 
massivas de dados.
'''