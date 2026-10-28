# class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Myst', 'Vas')

print(p1.nome)
print(p1.sobrenome)

'''
1. O Molde (class Pessoa:)
Você está ensinando ao Python que agora existe um novo tipo de dado no seu sistema chamado Pessoa. 
Assim como existe o tipo list e str, agora existe o seu tipo personalizado.

2. O Construtor (__init__)
Esse é um método mágico (por ter dois underlines, chamamos de dunder method). Ele é a primeira coisa 
executada no momento em que você "chama" a classe. Ele é responsável por inicializar o objeto.

3. O grande segredo: O self
O self é a referência à própria instância (o objeto) que está sendo criado naquele exato momento.
Quando você digita p1 = Pessoa('Myst', 'Vas'), o Python faz isso nos bastidores: ele pega a variável 
p1 e a injeta no lugar do self. Logo:

self.nome = nome é o mesmo que p1.nome = 'Myst'

self.sobrenome = sobrenome é o mesmo que p1.sobrenome = 'Vas'

Se você criasse um p2 = Pessoa('Ana', 'Silva'), o self daquela execução seria o p2. O self impede que 
os dados do p1 se misturem com os do p2.

Como isso se aplica às suas áreas de interesse?

Cibersegurança: Em vez de Pessoa, imagine uma class AlvoReconhecimento:. O __init__ pediria ip, 
porta_aberta, e sistema_operacional. Assim, você modela as ameaças na memória do script de forma 
organizada.

Ciência de Dados: A famosa biblioteca pandas é puramente POO. Quando você lê um CSV, você cria um 
objeto da classe DataFrame. E esse objeto tem atributos (como .columns, .shape) que guardam as 
características dos seus dados.
'''