# Raise - lançando excessões (erros)

def cadastrar_usuario(idade):
    if idade < 0:
        # Lança explicitamente um ValueError se a idade for negativa
        raise ValueError("A idade não pode ser um valor negativo!")
    
    if idade < 18:
        # Lança um PermissionError se for menor de idade
        raise PermissionError("Usuário menor de idade não pode se cadastrar.")
    
    print(f"Sucesso! Usuário cadastrado com a idade de {idade} anos.")

# Testando a função junto com o bloco try...except que vimos antes:
testes = [25, -5, 16]

for idade_teste in testes:
    print(f"\n--- Testando idade: {idade_teste} ---")
    try:
        cadastrar_usuario(idade_teste)
    except ValueError as erro:
        print(f"Capturado ValueError: {erro}")
    except PermissionError as erro:
        print(f"Capturado PermissionError: {erro}")