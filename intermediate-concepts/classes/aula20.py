# Modulos padrão do python (import, from, as e *)

import math

# Usa a função sqrt (raiz quadrada) do módulo math
resultado = math.sqrt(25)
print(f"Raiz quadrada de 25: {resultado}")

# Importa apenas a constante pi e a função factorial do módulo math
from math import pi, factorial

print(f"Valor de PI: {pi}")
print(f"Fatorial de 5: {factorial(5)}") # 5 * 4 * 3 * 2 * 1 = 120

# Importa o módulo datetime com o apelido 'dt'
import datetime as dt

hoje = dt.date.today()
print(f"Data de hoje: {hoje}")

# Importa TUDO do módulo random
from random import *

# Usa a função randint direto, sem escrever 'random.randint'
numero_sorteado = randint(1, 10)
print(f"Número aleatório de 1 a 10: {numero_sorteado}")

# Exemplo combinando os conceitos em um script real:
import math                      # Pega o módulo todo
from datetime import date as dt  # Pega uma função específica e renomeia

print(f"PI arredondado: {round(math.pi, 2)}")
print(f"Ano atual: {dt.today().year}")