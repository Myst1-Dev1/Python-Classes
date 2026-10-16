# Decoradores com parametros

'''
Para criar um decorador que aceita parâmetros (como @repetir(vezes=3)), você precisa de três níveis 
de funções em vez de dois.

Isso acontece porque o Python precisa primeiro avaliar o parâmetro que você passou no decorador, 
para só então criar o decorador real que vai envolver a sua função.

Aqui está um exemplo de um decorador que repete a execução 
de uma função um determinado número de vezes:
'''

# 1. FÁBRICA DE DECORADOR: Recebe os parâmetros do decorador
def repetir(vezes):
    
    # 2. O DECORADOR REAL: Recebe a função a ser decorada
    def decorador(func):
        
        # 3. A FUNÇÃO INTERNA (WRAPPER): Recebe os argumentos da função original
        def wrapper(*args, **kwargs):
            
            print(f"--- Iniciando repetição ({vezes} vezes) ---")
            
            # Altera o comportamento: executa num loop de acordo com o parâmetro 'vezes'
            for i in range(vezes):
                resultado = func(*args, **kwargs)
                
            print("--- Fim da repetição ---\n")
            
            return resultado # Retorna o resultado da última execução
            
        return wrapper
        
    return decorador

# Usando o decorador com parâmetro
@repetir(vezes=3)
def enviar_alerta(mensagem):
    print(f"Alerta: {mensagem}")

@repetir(vezes=2)
def dar_boas_vindas(nome):
    print(f"Bem-vindo(a), {nome}!")

# Executando as funções
enviar_alerta("Sistema reiniciando!")
dar_boas_vindas("Ana")