# Desafio 2: Limpeza e Agrupamento de Dados (Foco em Map, Groupby e Reduce/Soma)

from itertools import groupby

trafego_sensores = [
    {'setor': '  FINANCEIRO  ', 'pacotes': 1500},
    {'setor': 'TI ', 'pacotes': 8000},
    {'setor': 'financeiro', 'pacotes': 350},
    {'setor': '  TI', 'pacotes': 1200},
    {'setor': 'RH', 'pacotes': 200}
]

# --- PASSO 1: MAP (Limpeza) ---
def limpar_dados(dicionario):
    # Pega o nome do setor, remove os espaços nas pontas e joga para maiúsculo
    setor_limpo = dicionario['setor'].strip().upper()
    
    # Retorna um novo dicionário com o nome limpo e mantendo os pacotes intactos
    return {'setor': setor_limpo, 'pacotes': dicionario['pacotes']}

trafegos_limpos = list(map(limpar_dados, trafego_sensores))

# --- PASSO 2: GROUPBY (Agrupamento) ---
# Regra de ouro: precisamos ordenar a lista pela mesma chave que vamos agrupar
def chave_setor(dicionario):
    return dicionario['setor']

# Ordena a lista limpa (modifica a lista original in-place)
trafegos_limpos.sort(key=chave_setor)

# Agrupa os dados
grupos_de_trafego = groupby(trafegos_limpos, key=chave_setor)

# --- PASSO 3: REDUCE / SOMA ---
print("--- Relatório de Tráfego por Setor ---")

for setor, grupo in grupos_de_trafego:
    # O 'grupo' tem todos os dicionários daquele setor. 
    # Usamos uma list comprehension para extrair só os números de pacotes e somar.
    total_pacotes = sum(item['pacotes'] for item in grupo)
    
    print(f"Setor {setor}: {total_pacotes} pacotes")