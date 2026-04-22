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

# 

---