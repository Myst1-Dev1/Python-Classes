# Funçoes decoradoras e decoradores
# Decorar = adicionar / remove / restringir / alterar
# Funçoes decoradoras sao funçoes que decoram outras funçoes
# Decoradores sao usados para fazer o python
# usar as funçoes decoradoras em outras funçoes
# Decoradores sao Syntax Sugar (açucar sintatico)

# 1. FUNÇÃO DECORADORA
# Recebe uma função (func) como parâmetro para "decorá-la"
def adicionar_moldura(func):
    
    # A função interna (closure) é onde a alteração de comportamento acontece.
    # Usamos *args e **kwargs para aceitar qualquer parâmetro que a função original exija.
    def funcao_interna(*args, **kwargs):
        print("+" + "-"*30 + "+")
        print("| Iniciando a execução...      |")
        
        # Executa a função original e guarda o resultado
        resultado = func(*args, **kwargs)
        
        print("| Execução finalizada!         |")
        print("+" + "-"*30 + "+")
        
        return resultado # Retorna o resultado da função original
        
    # A função decoradora retorna a função interna modificada, sem executá-la
    return funcao_interna


# --- COMO ERA FEITO ANTES DO SYNTAX SUGAR ---

def saudacao_simples(nome):
    print(f"| Olá, {nome}! Tudo bem?{' '*4}|")

# Você precisava reatribuir a função manualmente passando ela mesma como argumento
saudacao_simples = adicionar_moldura(saudacao_simples)


# --- COMO É FEITO HOJE COM SYNTAX SUGAR (@) ---

# O Python faz exatamente a mesma reatribuição da linha 25 automaticamente por baixo dos panos.
@adicionar_moldura 
def despedida(nome):
    print(f"| Tchau, {nome}! Até logo!{' '*4}|")