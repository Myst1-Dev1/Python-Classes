# Context Manager with

'''
O with (Gerenciador de Contexto ou Context Manager) é um dos recursos mais elegantes e importantes 
do Python. A regra de ouro dele é: ele garante que recursos sejam abertos e, o mais importante, 
fechados corretamente, mesmo que um erro grave aconteça no meio do seu código.

Tanto em Ciência de Dados quanto em Cibersegurança, você vai interagir o tempo todo com recursos 
externos: arquivos CSV gigantes, bancos de dados, conexões de rede e portas do servidor. Se você abre 
algo e esquece de fechar, causa vazamento de memória ou deixa arquivos travados/corrompidos.

Aqui estão as formas de usar, desde a clássica até a avançada.
'''

# Exemplo 1: O Clássico (Lendo e escrevendo arquivos)
# O jeito mais comum de usar o with é com a função open().

# O jeito RUIM (sem o with):

arquivo = open('logs_de_rede.txt', 'r')
dados = arquivo.read()
# Se der um erro (exceção) na linha acima, o Python para e NUNCA chega na linha de baixo.
# O arquivo fica preso e travado na memória.
arquivo.close()

# O jeito "Pythonic" (usando o with):

# Lê-se: "Com o arquivo aberto como 'arquivo', faça o seguinte:"
with open('logs_de_rede.txt', 'r') as arquivo:
    dados = arquivo.read()
    print("Arquivo está aberto e sendo lido.")

# O bloco do with acabou (acabou a indentação).
# O Python FECHA O ARQUIVO AUTOMATICAMENTE aqui, mesmo se o código tiver quebrado lá dentro.

# Exemplo 2: Ciência de Dados e Ciber (Manipulando dois arquivos juntos)
# Você pode abrir múltiplos gerenciadores de contexto na mesma linha.

# Imagine que você está fazendo um script de Cibersegurança que lê um arquivo com milhares de senhas 
# vazadas (Data Science também faz isso para limpar bases de dados) e quer salvar apenas as senhas 
# fortes em um novo arquivo.

# Abrimos o arquivo original para leitura ('r') e um novo para escrita ('w')
with open('senhas_vazadas.txt', 'r') as arquivo_leitura, \
     open('senhas_fortes_filtradas.txt', 'w') as arquivo_escrita:
    
    for linha in arquivo_leitura:
        senha = linha.strip()
        
        # Filtro simples: só salva se a senha tiver mais de 8 caracteres
        if len(senha) > 8:
            arquivo_escrita.write(senha + '\n')

print("Processo finalizado. Ambos os arquivos foram fechados em segurança.")

'''
O Segredo por baixo dos panos (Padrão Luiz Otávio)
O professor Luiz Otávio gosta muito de explicar as "engrenagens" do Python 
(os Magic Methods ou Dunder Methods). O with funciona porque o objeto que ele gerencia possui dois 
métodos mágicos configurados dentro dele:

__enter__(self): O que acontece quando o bloco with começa (ex: abrir o arquivo, conectar no 
banco de dados).

__exit__(self, exc_type, exc_val, exc_tb): O que acontece quando o bloco with termina 
ou dá erro (ex: fechar o arquivo, derrubar a conexão). É aqui que a mágica da segurança mora!
'''