# Variáveis livres + nonlocal

'''
Uma variável livre (free variable) é aquela que é utilizada dentro de uma função, mas não foi 
definida dentro dela e nem é uma variável global. Ela "pertence" ao escopo da função externa que a 
envolve.

O comando nonlocal é usado para avisar ao Python que você deseja modificar o valor dessa variável livre. 
Se você tentar alterá-la sem usar o nonlocal, o Python achará que você está tentando criar uma nova 
variável local e gerará um erro.

Aqui está o exemplo clássico de um contador (um tipo de Closure):
'''

def criar_contador(inicio):
    # 'total' pertence ao escopo de criar_contador.
    # Para a função de baixo, 'total' será uma VARIÁVEL LIVRE.
    total = inicio
    
    def adicionar(valor):
        # Sem o nonlocal, a linha abaixo daria erro (UnboundLocalError),
        # pois o Python acharia que 'total' é uma variável local ainda não definida.
        nonlocal total
        
        # Agora podemos modificar a variável livre da função externa
        total += valor
        return total
        
    return adicionar

# Criando um contador que começa em 10
meu_contador = criar_contador(10)

print(meu_contador(5))  # Saída: 15
print(meu_contador(20)) # Saída: 35
print(meu_contador(3))  # Saída: 38