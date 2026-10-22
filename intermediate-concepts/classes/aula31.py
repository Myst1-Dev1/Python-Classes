# map - para mapear dados

'''
A função map serve para aplicar uma mesma função a cada item de um iterável 
(como uma lista, tupla, etc.), gerando novos dados transformados.

Em Ciência de Dados, usamos muito esse conceito para limpar ou transformar colunas de dados. 
Veja este exemplo onde temos uma lista de preços que foram raspados da internet (web scraping) 
e vieram como strings "sujas". Precisamos converter isso para números reais (float).
'''

# Dados brutos em formato de texto (string)
precos_extracao = ['R$ 15.50', 'R$ 20.00', 'R$ 5.99', 'R$ 100.00']

# 1. Criamos a função que faz a transformação de UM único item
def limpar_preco(valor_string):
    # Substitui 'R$ ' por nada e converte para decimal
    valor_limpo = valor_string.replace('R$ ', '')
    return float(valor_limpo)

# 2. Usamos o map(função, iterável) para aplicar a limpeza em toda a lista
precos_mapeados = map(limpar_preco, precos_extracao)

# O map não retorna uma lista pronta, ele retorna um "iterador" (map object)
# Para ver os dados, precisamos converter para lista
precos_prontos = list(precos_mapeados)

print("Dados originais:", precos_extracao)
print("Dados limpos:   ", precos_prontos)

ips = ['192.168.0.1', '10.0.0.5', '127.0.0.1']

# Mapeando com lambda: adiciona ':80' ao final de cada IP
ips_com_porta = list(map(lambda ip: ip + ':80', ips))

print(ips_com_porta)
# Saída: ['192.168.0.1:80', '10.0.0.5:80', '127.0.0.1:80']

'''
Por que usar map e não um for normal?
Além de deixar o código mais limpo e declarativo (você diz o que quer fazer, não como), 
o map não carrega todos os dados na memória de uma vez. Ele gera os valores sob demanda 
(lazy evaluation), o que é excelente para Ciência de Dados quando se 
trabalha com arquivos gigantescos.
'''