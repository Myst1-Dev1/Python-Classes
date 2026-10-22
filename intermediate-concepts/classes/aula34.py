# Funções recursivas e recursividade

'''
Uma função recursiva é, de forma bem simples, uma função que chama a si mesma dentro do próprio código.

A regra de ouro da recursividade (e o que o professor Luiz Otávio mais enfatiza) é: toda 
função recursiva precisa ter um "Caso Base" (condição de parada). Se você não disser quando ela 
deve parar, ela vai chamar a si mesma para sempre até estourar a memória do 
Python (o famoso erro RecursionError).

Aqui estão dois exemplos: um clássico para entender a mecânica, e um aplicado para a sua área.
'''

# Exemplo 1: O Clássico (Fatorial)
# Na matemática, o fatorial de 5 (escrito como 5!) é 5 * 4 * 3 * 2 * 1. Perceba que é uma 
# repetição diminuindo o número.

def fatorial(n):
    # 1. CASO BASE (Condição de parada)
    # Se chegar em 1 ou 0, para de chamar a si mesma e retorna 1
    if n <= 1:
        return 1
    
    # 2. CASO RECURSIVO
    # Ela multiplica o número atual pelo resultado dela mesma com o número - 1
    return n * fatorial(n - 1)

print(f"O fatorial de 5 é: {fatorial(5)}")
# Saída: O fatorial de 5 é: 120

'''
O que acontece por baixo dos panos (Pilha de chamadas / Call Stack):

fatorial(5) espera fatorial(4)

fatorial(4) espera fatorial(3)

fatorial(3) espera fatorial(2)

fatorial(2) espera fatorial(1)

fatorial(1) atinge o caso base e retorna 1. Aí a pilha vai se resolvendo de trás para frente.
'''

# Exemplo 2: Ciência de Dados / Cibersegurança (Lidando com estruturas aninhadas)

'''
Tanto em Dados (analisando JSONs complexos) quanto em Cibersegurança 
(varrendo pastas dentro de pastas em busca de um arquivo malicioso), você lida com estruturas 
que têm profundidade desconhecida.

A recursividade brilha aqui. Vamos criar uma função que "achata" 
(achatar = colocar tudo no mesmo nível) uma lista cheia de outras listas dentro dela.
'''

# Uma estrutura de dados "suja" e aninhada
dados_aninhados = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]

def achatar_lista(lista):
    lista_limpa = []
    
    for item in lista:
        # Se o item atual for uma lista, usamos a recursividade!
        if isinstance(item, list):
            # A função chama a si mesma para descer mais um nível
            resultado_interno = achatar_lista(item)
            lista_limpa.extend(resultado_interno)
        
        # CASO BASE: se for um número normal, só adiciona na lista limpa
        else:
            lista_limpa.append(item)
            
    return lista_limpa

dados_planos = achatar_lista(dados_aninhados)
print("Dados originais:", dados_aninhados)
print("Dados planos:   ", dados_planos)


'''
Aviso de Segurança (Limite do Python):
O Python tem um limite padrão de quantas vezes uma função pode chamar a si mesma 
(geralmente 1000 vezes) para proteger o seu computador de travar. É possível alterar esse limite 
com sys.setrecursionlimit(), mas se você estiver chegando nesse limite, geralmente é melhor usar 
um loop while ou for normal
'''