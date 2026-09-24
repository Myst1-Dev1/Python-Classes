'''
Closure e funções que retornam outras funções

Uma closure (ou fechamento) é uma das aplicações mais elegantes do conceito de escopo 
Enclosing (o "E" da regra LEGB) em Python.

Em termos simples, uma closure é uma função interna que "lembra" e consegue acessar as variáveis 
do seu escopo externo, mesmo depois que a função externa já terminou de ser executada e retornado.

Os 3 requisitos para uma Closure
Para que uma closure exista em Python, precisamos atender a três condições básicas:

Função aninhada: Você deve ter uma função definida dentro de outra função.

Referência externa: A função interna deve referenciar (usar) uma variável definida 
na função externa.

Retorno: A função externa deve retornar a função interna (sem executá-la, apenas 
passando sua referência).

'''

'''
Exemplo Prático
Imagine que queremos criar funções que multiplicam números por um fator 
específico, mas queremos gerar essas funções de forma dinâmica:
'''

def criar_multiplicador(fator):
    # 'fator' está no escopo envolvente (enclosing)
    def multiplicar(numero):
        return numero * fator
    
    # Retornamos a função interna (ainda não executada)
    return multiplicar

# Criamos funções especializadas
dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(dobrar(5))    # Saída: 10
print(triplicar(5)) # Saída: 15

'''
O que aconteceu aqui?
Quando chamamos criar_multiplicador(2), a função externa terminou e foi apagada da memória.
No entanto, a variável fator (com valor 2) foi "congelada" junto com a função multiplicar 
dentro de um objeto de closure. É por isso que dobrar(5) ainda sabe que o fator é 2.
'''


'''
Para que servem as Closures?

Encapsulamento de dados: Permitem criar estado privado sem precisar recorrer a classes completas e 
orientação a objetos.

Fábricas de funções (Function Factories): Útil para gerar funções customizadas em tempo de 
execução com base em certas configurações iniciais.

Decoradores: O mecanismo de decorators do Python, muito usado para modificar o comportamento de funções, 
é construído inteiramente em cima do conceito de closures.
'''