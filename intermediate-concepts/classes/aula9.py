# Empacotamento e desempacotamento de dicionarios

a , b = 1 ,2
a, b = b, a

pessoa = {
    'nome': 'peter',
    'sobrenome': 'parker'
}

dados_pessoas = {
    'idade': 24,
    'altura': 1.70
}

pessoa_completa = {**pessoa, **dados_pessoas}

print(pessoa_completa)

# args e kwargs
# args já vimos
# kwars - keywords arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(name = 'joao', idade = 24)

'''

'''