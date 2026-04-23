# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as expressões precisam ser verdadeiras para retornar True
# se qualquer valor for considerado falso, a expressão inteira será avaliada como falsa
# Valores considerados falsy: 0 0.0 '' false
# Também existe o tipo none que é usado para representar um não valor


# entrar = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrar == 'E' or entrar == 'e') and senha_digitada == senha_permitida:
#     print('Entrando...')
# else:
#     print('Saindo...')

# Avaliação de curto circuito

# print(0 or False or 0 or 'abc' or True)
# senha = input('Senha: ') or 'Sem senha'
# print(senha)


# Operador lógico not
# Usado para inverter expressões
# not True =  False
# not False = True

# senha = input('Senha: ')

# if not senha:
#     print('Você não digitou nada')

# Operadores in e not in
#Strings são iteráveis
#0 1 2 3 4 5
#o t á v i o
#-6 -5 -4 -3 -2 -1

nome = 'Otávio'
# print(nome[2])
# print(nome[-4])

# print('á' in nome)
# print('z' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')