# Calculadora de IMC

# weight = input('Digite seu peso:')
# height = input('Digite sua altura:')

# degrees_of_obesity = [
#     {'imc_result': 18.5, "degree": "Magreza"},
#     {'imc_result': 24.9, "degree": "Normal"},
#     {'imc_result': 29.9, "degree": "Sobrepeso"},
#     {'imc_result': 34.9, "degree": "Obesidade grau I"},
#     {'imc_result': 39.9, "degree": "Obesidade grau II"},
#     {'imc_result': 40.0, "degree": "Obesidade grau III (Grave)"},
# ]

# def bmiCalculation(weight, height):
#     imc = round(float(weight) / (float(height) ** 2), 2)
#     print(f'\n(Debug) Seu IMC exato é: {imc}')

#     for degree in degrees_of_obesity:
#         if imc <= degree.get('imc_result'):
#             return degree.get('degree')
            
#     return "Obesidade grau III (Grave)"

# print(f'Resultado: {bmiCalculation(weight, height)}')


# Desafio: Sistema de Detecção de Fraudes (Antifraude)

'''
As Regras de Negócio (Requisitos):
Uma transação é considerada suspeita se atender a PELO MENOS UMA destas regras:

O valor for maior que 3000.00.

A hora estiver entre "00:00" e "05:59" (Dica: no Python, você pode comparar strings de horas no 
formato 24h diretamente usando < e >, por exemplo: '00:00' <= hora < '06:00').

Sua Missão Passo a Passo:

Crie uma função chamada detectar_fraude(transacao) que recebe um dicionário de transação e 
retorna True se for suspeita, ou False se for segura.

Use a função filter() para filtrar a lista original, mantendo apenas os dicionários de transações 
suspeitas.

Use a função map() em cima do resultado do filtro para extrair apenas o id dessas transações.

Transforme o resultado final em uma lista e imprima na tela.

Saída Esperada no Terminal:IDs bloqueados por suspeita de fraude: [102, 103, 105]
'''

# transacoes = [
#     {'id': 101, 'valor': 45.50, 'hora': '14:30', 'estado': 'SP'},
#     {'id': 102, 'valor': 15000.00, 'hora': '15:00', 'estado': 'RJ'}, # Suspeito (Valor alto)
#     {'id': 103, 'valor': 15.00, 'hora': '02:15', 'estado': 'SP'},    # Suspeito (Madrugada)
#     {'id': 104, 'valor': 250.00, 'hora': '18:45', 'estado': 'MG'},
#     {'id': 105, 'valor': 4500.00, 'hora': '03:30', 'estado': 'BA'},  # Suspeito (Valor alto E Madrugada)
# ]

# def detectar_fraude(transacao):
#     return transacao['valor'] > 3000.00 or '00:00' <= transacao['hora'] < '06:00'

# transacoes_filtradas = list(filter(detectar_fraude, transacoes))

# # print(f'Transações filtradas: {transacoes_filtradas}')

# ids = list(map(lambda t: t['id'], transacoes_filtradas))
# print(f'IDs bloqueados por suspeita de fraude: {ids}')

# A Auditoria de Permissões (Controle de Acesso)

'''
Sua Missão Passo a Passo:

O Filtro: Crie uma função (ou use lambda) para o filter(). Ela deve retornar True APENAS SE o 
cargo for igual a "Estagiario" E o nivel_acesso for maior que 2. Transforme o resultado em uma lista.

O Mapa: Crie uma função (ou use lambda) para o map(). Ela deve receber a lista de irregulares que 
você acabou de filtrar e extrair apenas o nome dessas pessoas. Transforme o resultado em uma lista.

A Exportação: Importe o módulo json. Use o with open para criar um arquivo chamado auditoria.json no 
modo de escrita ('w'). Salve a lista de nomes extraídos dentro deste arquivo.

O que deve acontecer no final:
Seu script não precisa printar nada na tela, mas ele deve gerar um arquivo auditoria.json na sua 
pasta contendo:

JSON
[
    "Carlos",
    "Fernanda"
]
'''

import json

funcionarios = [
    {'id': 1, 'nome': 'Ana', 'cargo': 'Analista', 'nivel_acesso': 3},
    {'id': 2, 'nome': 'Bruno', 'cargo': 'DevOps', 'nivel_acesso': 5},
    {'id': 3, 'nome': 'Carlos', 'cargo': 'Estagiario', 'nivel_acesso': 4}, # RISCO!
    {'id': 4, 'nome': 'Daniela', 'cargo': 'Gerente', 'nivel_acesso': 5},
    {'id': 5, 'nome': 'Eduardo', 'cargo': 'Estagiario', 'nivel_acesso': 1},
    {'id': 6, 'nome': 'Fernanda', 'cargo': 'Estagiario', 'nivel_acesso': 3}, # RISCO!
]

filtered_functionaries = list(filter(
    lambda f: f['cargo'] == 'Estagiario' and f['nivel_acesso'] > 2, funcionarios))

mapped_persons = list(map(lambda name: name['nome'], filtered_functionaries))

print(f'Resultados: {mapped_persons}')

with open('auditoria.json', 'w', encoding='utf-8') as arquivo:
    json.dump(mapped_persons, arquivo, ensure_ascii=False, indent=4)