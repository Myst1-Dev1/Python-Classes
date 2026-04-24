📘 Estudos em Python (Básico)

Este repositório contém anotações e exemplos dos meus estudos iniciais em Python.

🧠 Conceitos Iniciais

# 📝 Comentários

Comentário de uma linha é feito com #

''' Comentário de múltiplas linhas '''
""" Comentário de múltiplas linhas """

---

# 🖨️ Função print

print("Olá, mundo!")

print(12, 35, sep="-")  
Saída: 12-35

print(12, 35, 1011, sep='-', end='##\n')  
Saída: 12-35-1011##
sep: define o separador entre os valores
end: define o final da linha (padrão é \n)

---

# 🔤 Strings

str → representa textos
Podem ser usadas com aspas simples ' ' ou duplas " "
Aspas simples
print('Olá, Mundo!')
print(1, 'olá, "mundo"')

Aspas duplas
print("Olá, Mundo")
print(1, "olá, 'mundo'")

Escape
print("Olá, Mundo! \"Bem-vindo ao curso de Python!\"")

Raw string (ignora escapes)
print(r"Olá, Mundo! \"Bem-vindo ao curso de Python!\"")

---

# 🔢 Tipos Numéricos

Inteiros (int)

print(11)
print(-11)
print(0)

Ponto flutuante (float)

print(3.14)
print(-3.14)
print(0.0)

Verificando tipos

print(type('Myst'))  # <class 'str'>
print(type(1.1))     # <class 'float'>
print(type(1))       # <class 'int'>🔢 Tipos Numéricos

---

# ✅ Booleanos (bool)

Representam verdadeiro ou falso:

print(10 == 10)  # True
print(10 == 11)  # False

print(type(True))           # bool
print(type(10 == 10))       # bool

---

# 🔄 Conversão de Tipos (Type Casting)

print(int('1'), type(int('1')))
print(int('1') + 1)

print(float(1) + 1)
print(float('1.5'), type(float('1.5')))

print(bool(''))     # False
print(str(11) + 'b')

---

# 📦 Variáveis

Armazenam valores na memória
Convenção PEP8: usar letras minúsculas e _

nome_completo = "Myst Vas"
soma = 2 + 2
int_um = int("1")
idade = 24
maior_de_idade = idade >= 18

print(nome_completo)
print(soma)
print(int_um, type(int_um))
print(idade)
print(maior_de_idade)

print("Nome completo: " + nome_completo +
      ", Idade: " + str(idade) +
      ", É maior de idade: " + str(maior_de_idade))

---

# ➕ Operadores Aritméticos

adicao = 10 + 10
subtracao = 10 - 10
multiplicacao = 10 * 10
divisao = 10 / 2.2
divisao_inteira = 10 // 2.2
exponenciacao = 2 ** 10
modulo = 55 % 2

print(adicao)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisao_inteira)
print(exponenciacao)
print(modulo)

---

# 🔗 Concatenação e Repetição

concatenacao = 'A' + 'B' + 'C'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_myst = 3 * 'Myst'

print(a_dez_vezes)
print(tres_vezes_myst)

---

# 📊 Precedência de Operadores

Ordem de execução:

( )
**
* / // %
+ -
conta_1 = 1 + 1 ** 5 + 5
conta_2 = (1 + 1) ** (5 + 5)

print(conta_1)
print(conta_2)

---

# 🧵 f-Strings (Formatação Moderna)

nome = 'João'
altura = 1.70

texto = f'{nome} tem altura de {altura:.2f}'
print(texto)

f permite inserir variáveis diretamente na string
:.2f formata números com 2 casas decimais

---

# Função input para coletar dados de usuário

nome = input('Qual o seu nome? ')

print(f'O seu nome é {nome=}')

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

print(f'A soma de {numero_1} + {numero_2} é igual a {numero_1 + numero_2}')

---

# if / elif / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Opção inválida')

---

# Operadores de comparação(relacionais)

OP          Significado         Exemplo (true)
>           Maior               2 > 1
>=          Maior ou igual      2 >= 2
<           Menor               1 < 2
<=          Menor ou igual      2 <= 2
==          Igual                'a' == 'a'
!=          Diferente             'a' != 'b'

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(diferente)

---

# Operadores lógicos

- and (e) or (ou) not (não)
- and - todas as expressões precisam ser verdadeiras para retornar True
- se qualquer valor for considerado falso, a expressão inteira será avaliada como falsa
- Valores considerados falsy: 0 0.0 '' false
- Também existe o tipo none que é usado para representar um não valor

entrar = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrar == 'E' and senha_digitada == senha_permitida:
    print('Entrando...')
else:
    print('Saindo...')

---

# Avaliação de curto circuito

print(0 or False or 0 or 'abc' or True)
senha = input('Senha: ') or 'Sem senha'
print(senha)

---

# Operador lógico not

Usado para inverter expressões
not True =  False
not False = True

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')

---

# Operadores in e not in

Strings são iteráveis
0 1 2 3 4 5
o t á v i o
-6 -5 -4 -3 -2 -1

nome = 'Otávio'
print(nome[2])
print(nome[-4])

print('á' in nome)
print('z' in nome)
print(10 * '-')
print('vio' not in nome)
print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')

---

# Interpolaçao básica de strings

nome = 'luiz'
preco = 1000.958976
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

---

# Formatação básica de strings

s - string
d - int
f - float
.<número de digitos>f x ou X Hexadecimal (Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex: 0>100,.1f
Conversion flags - !r !s !a

---

# Fatiamento de strings

012345678
OLá mundo
-987654321
Fatiamento [i:f:p] [i:]
Obs.: a função len retorna a qtd de caracteres da string

variavel = 'Olá mundo'
print(len(variavel))

---

# Introdução ao try/except

try -> tentou executar o código
except -> ocorreu algum erro ao executar o código

numero_string = input('Vou dobrar o número que você digitar: ')

try:
    numero_int = int(numero_string)
    print(f'O dobro de {numero_int} é {numero_int * 2}')
except:
    print('Isso não é um número inteiro válido.')

---

# CONSTANTE = 'Variaveis' que não vão mudar
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)

velocidade = 61
local_carro = 99


RADAR_1  = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_multado_radar_1 and vel_carro_pass_radar_1:    
    print('Carro multado em radar 1')

---

# Flag (bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade


---