# Desafio 1: O Analista de Segurança (Foco em Arquivos, Filter e JSON)

'''
Você interceptou um log de acessos a um servidor, mas ele está em texto puro e cheio de acessos 
normais. Sua missão é extrair apenas as falhas de segurança 
e salvar um relatório estruturado.

Requisitos:

Crie um arquivo chamado server_logs.txt pelo próprio Python 
(usando with open e modo 'w') contendo as seguintes linhas:

Plaintext
10:00 - IP: 192.168.0.1 - STATUS: SUCESSO
10:15 - IP: 10.0.0.5 - STATUS: FALHA_AUTENTICACAO
10:30 - IP: 127.0.0.1 - STATUS: SUCESSO
11:00 - IP: 198.51.100.22 - STATUS: FALHA_AUTENTICACAO
Leia este arquivo texto.

Use a função filter() (ou list comprehension) para separar apenas as linhas 
que contêm a palavra "FALHA".

Transforme essas linhas filtradas em uma lista de dicionários Python 
(ex: [{'horario': '10:15', 'ip': '10.0.0.5', 'erro': 'FALHA_AUTENTICACAO'}]).

Salve essa lista de dicionários em um arquivo chamado alertas_criticos.json usando o módulo json.
'''

import json

caminho_txt = 'server_logs.txt'
caminho_json = 'alertas_criticos.json'

# PASSO 1: Criar o arquivo de texto bruto (simulando um log real)
texto_log = """10:00 - IP: 192.168.0.1 - STATUS: SUCESSO
10:15 - IP: 10.0.0.5 - STATUS: FALHA_AUTENTICACAO
10:30 - IP: 127.0.0.1 - STATUS: SUCESSO
11:00 - IP: 198.51.100.22 - STATUS: FALHA_AUTENTICACAO"""

with open(caminho_txt, 'w', encoding='utf-8') as arquivo:
    arquivo.write(texto_log)

# PASSO 2: Ler o arquivo texto
with open(caminho_txt, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

# PASSO 3: Usar filter para separar as falhas
# A lambda retorna True se a palavra "FALHA" existir dentro da string daquela linha
linhas_com_falha = list(filter(lambda linha: "FALHA" in linha, linhas))

# PASSO 4: Transformar texto bruto em dicionários
alertas = []
for linha in linhas_com_falha:
    # O método split(" - ") quebra a string onde houver esse separador.
    # Exemplo do que ele gera: ['10:15', 'IP: 10.0.0.5', 'STATUS: FALHA_AUTENTICACAO\n']
    partes = linha.strip().split(" - ")
    
    # Limpando os rótulos de texto para ficar apenas com o dado
    horario = partes[0]
    ip = partes[1].replace("IP: ", "")
    erro = partes[2].replace("STATUS: ", "")
    
    # Criando o dicionário e adicionando à lista
    alertas.append({
        'horario': horario,
        'ip': ip,
        'erro': erro
    })

# PASSO 5: Salvar em JSON
with open(caminho_json, 'w', encoding='utf-8') as arquivo_json:
    json.dump(alertas, arquivo_json, ensure_ascii=False, indent=4)

print("Relatório de incidentes gerado com sucesso.")
