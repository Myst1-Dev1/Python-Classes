import copy

produtos = [
    {'nome': 'produto 1', 'price': 100},
    {'nome': 'produto 2', 'price': 200},
    {'nome': 'produto 3', 'price': 300},
    {'nome': 'produto 4', 'price': 400},
    {'nome': 'produto 5', 'price': 500},
]

# 1. Aumente os preços dos produtos em 10% (gerando novos produtos por deep copy)
novos_produtos = copy.deepcopy(produtos)
for produto in novos_produtos:
    # Multiplicar por 1.10 adiciona 10% ao valor original
    produto['price'] = round(produto['price'] * 1.10, 2)

# 2. Ordene os produtos por nome decrescente (Z-A) usando deep copy
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda p: p['nome'], reverse=True)

# 3. Ordene os produtos por preço crescente (menor para maior) usando deep copy
produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda p: p['price'])

# --- EXIBINDO OS RESULTADOS ---
print("=== 1. LISTA ORIGINAL ===")
print(*produtos, sep='\n')

print("\n=== 2. NOVOS PRODUTOS (+10% no preço) ===")
print(*novos_produtos, sep='\n')

print("\n=== 3. ORDENADOS POR NOME DECRESCENTE (Z-A) ===")
print(*produtos_ordenados_por_nome, sep='\n')

print("\n=== 4. ORDENADOS POR PREÇO CRESCENTE ===")
print(*produtos_ordenados_por_preco, sep='\n')