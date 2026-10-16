# Combinations, Permutations e Product (itertools)
# Combinação - ordem nao importa - iteravel + tamanho do grupo
# Permutaçao - ordem importa
# Produto - Ordem importa e repete valores unicos

from itertools import combinations, permutations, product

pessoas = ['Ana', 'Bia', 'Caio']

# ==============================================================================
# 1. COMBINATION (Combinação)
# A ordem NÃO importa. O grupo ('Ana', 'Bia') é igual a ('Bia', 'Ana').
# Não há repetição do mesmo item com ele mesmo.
# ==============================================================================
print("--- COMBINATIONS (Grupos de 2) ---")
combinacoes = combinations(pessoas, 2)

for c in combinacoes:
    print(c)
# Saída:
# ('Ana', 'Bia')
# ('Ana', 'Caio')
# ('Bia', 'Caio')
# Repare que 'Bia' e 'Ana' não aparece, pois o grupo já foi formado.


# ==============================================================================
# 2. PERMUTATION (Permutação)
# A ordem IMPORTA. ('Ana', 'Bia') é DIFERENTE de ('Bia', 'Ana').
# Útil para senhas, pódios de corrida (1º e 2º lugar), etc.
# Também não repete a mesma pessoa duas vezes no mesmo grupo.
# ==============================================================================
print("\n--- PERMUTATIONS (Pódio de 2 lugares) ---")
permutacoes = permutations(pessoas, 2)

for p in permutacoes:
    print(p)
# Saída:
# ('Ana', 'Bia')
# ('Ana', 'Caio')
# ('Bia', 'Ana')  <-- Aqui a ordem inverteu, conta como um novo resultado
# ('Bia', 'Caio')
# ('Caio', 'Ana')
# ('Caio', 'Bia')


# ==============================================================================
# 3. PRODUCT (Produto Cartesiano)
# A ordem importa E os valores podem se repetir (Ana com Ana).
# Faz todas as combinações possíveis, como um cadeado numérico.
# ==============================================================================
opcoes_binarias = ['0', '1']

print("\n--- PRODUCT (Todas as possibilidades com repetição) ---")
# repeat=2 significa que queremos grupos de 2 elementos
produto = product(opcoes_binarias, repeat=2) 

for pr in produto:
    print(pr)
# Saída:
# ('0', '0') <-- Elementos podem se repetir
# ('0', '1')
# ('1', '0') <-- Ordem importa
# ('1', '1')