"""
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade foram digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        seu nome contém (ou não) espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba "Desculpe, você deixou campos vazios"
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    nome_invertido = nome[::-1]
    tem_espaco = "contém" if " " in nome else "não contém"
    n_letras = len(nome.replace(" ", ""))
    primeira_letra = nome[0]
    ultima_letra = nome[-1]

    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")
    print(f"Seu nome {tem_espaco} espaços")
    print(f"Seu nome tem {n_letras} letras")
    print(f"A primeira letra do seu nome é {primeira_letra}")
    print(f"A última letra do seu nome é {ultima_letra}")
else:
    print("Desculpe, você deixou campos vazios")