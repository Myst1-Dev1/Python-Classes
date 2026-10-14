# Yield from

def consultar_arquivos():
    yield from ["relatorio.pdf", "planilha.csv"]
    
def consultar_banco_dados():
    yield from ["cliente_id_1", "cliente_id_2"]

def extrair_todos_os_dados():
    # Une os resultados de duas funções geradoras diferentes
    yield "--- Iniciando extração ---"
    
    yield from consultar_arquivos()
    yield from consultar_banco_dados()
    
    yield "--- Fim da extração ---"

for dado in extrair_todos_os_dados():
    print(dado)