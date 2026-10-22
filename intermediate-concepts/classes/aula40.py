# Salvando dados python em json com módulo json

'''
1. Salvando dados em arquivo: json.dump()
Vamos pegar o que você aprendeu na aula passada sobre o with open (com encoding='utf-8') e 
aplicar aqui.

Imagine que você coletou dados de servidores (Cibersegurança) ou o perfil de clientes 
(Ciência de Dados) e quer salvar isso no disco.
'''

import json

# Nossos dados em Python (uma lista de dicionários)
dados_sistema = [
    {"servidor": "Web", "ip": "192.168.0.1", "status_ativo": True, "alertas": 0},
    {"servidor": "Banco", "ip": "10.0.0.5", "status_ativo": False, "alertas": 3, "obs": "Atenção"}
]

caminho_arquivo = 'relatorio_servidores.json'

# Usamos o 'w' para escrever e o utf-8 (padrão de ouro!)
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    # json.dump(dados, arquivo_destino)
    json.dump(
        dados_sistema, 
        arquivo,
        ensure_ascii=False, # Impede que acentos virem códigos estranhos (ex: \u00e7 para 'ç')
        indent=4            # Formata o texto com 4 espaços para ficar bonito e legível para humanos
    )

print("Dados salvos em JSON com sucesso!")

'''
ensure_ascii=False: O JSON foi criado por americanos. Por padrão, ele tenta converter caracteres como 
ç ou ã em códigos unicode. Colocar False diz para o JSON: "Deixe meus acentos em paz!".

indent=4 ou indent=2: Se você não colocar isso, o JSON será salvo em uma única linha infinita. 
O indent quebra as linhas e coloca espaços, deixando estruturado como você vê no código Python.
'''

'''
2. Lendo dados do arquivo: json.load()
Agora, outro script seu precisa ler esse arquivo e transformar 
de volta em listas/dicionários do Python para fazer cálculos.
'''

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    # json.load(arquivo_origem)
    dados_carregados = json.load(arquivo)

# Agora 'dados_carregados' voltou a ser uma lista de dicionários Python!
print(type(dados_carregados)) # <class 'list'>

# Iterando sobre os dados
for maquina in dados_carregados:
    print(f"Servidor: {maquina['servidor']} - Alertas: {maquina['alertas']}")


'''
3. A "Pegadinha" Clássica: dump vs dumps (e load vs loads)
Esse é um erro muito comum no início. Note que existe um "s" no final de algumas funções. 
Esse "S" significa String.

json.dump() e json.load() (SEM o S): Usados para ler/escrever diretamente em arquivos 
(precisam do with open).

json.dumps() e json.loads() (COM o S): Usados para converter dados em strings na 
memória (texto), sem salvar no HD.
'''

'''
Quando usar os com "S" (dumps/loads)?
Em Cibersegurança, se você estiver interceptando uma requisição web na memória, ou 
em Ciência de Dados, se estiver baixando uma página da internet diretamente para uma variável, 
você não precisa salvar no HD primeiro.
'''

dicionario_python = {"alvo": "site.com", "porta": 80}

# Converte o dicionário para uma STRING no formato JSON
texto_json = json.dumps(dicionario_python) 
print(type(texto_json)) # <class 'str'>

# Converte a string JSON de volta para dicionário Python
dicionario_de_volta = json.loads(texto_json)
print(type(dicionario_de_volta)) # <class 'dict'>

'''
Resumo das conversões Python <-> JSON:

dict vira Object (chaves e valores).

list vira Array.

True / False viram true / false (minúsculo no JSON).

None vira null no JSON.
'''