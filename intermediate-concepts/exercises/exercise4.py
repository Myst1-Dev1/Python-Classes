'''
Crie uma função que encontre o primeiro duplicado considerando o segundo número
como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda ocorrência do número
    ou seja o número duplicado em si.
    Exemplo:
        [1, ,2, 3, 3, 2, 1] -> 1 2 e 3 são duplicados, retorne 3.
        [1 , 2, 3 ,4, ,5 ,6] -> não tem duplicados, retorne -1
    Se não encontrar duplicados na lista retorne -1
'''

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_vistos = set()
    
    for numero in lista_de_inteiros:
        # Se o número já está no conjunto, ele é o primeiro duplicado (pela segunda ocorrência)
        if numero in numeros_vistos:
            return numero
        # Se não está, adicionamos ao conjunto de vistos
        numeros_vistos.add(numero)
        
    # Se percorrer tudo e não encontrar nenhum duplicado
    return -1

lista_de_lista_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
]

for i, listas in enumerate(lista_de_lista_de_inteiros, 1):
    resultado = encontra_primeiro_duplicado(listas)
    print(f"Lista {i}: {listas} -> Duplicado: {resultado}")