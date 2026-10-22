# Modos de abertura de arquivo e encoding com with open

'''
Esse é um dos assuntos onde mais ocorrem dores de cabeça para quem está começando, principalmente
em Ciência de Dados, quando você baixa um arquivo gigante da internet e ele vem cheio de caracteres 
"estranhos" (como  no lugar de acentos).

O professor Luiz Otávio sempre bate nessa tecla: o problema quase sempre é o encoding.
'''

'''
O que é o Encoding (Codificação)?
Computadores só entendem números (0s e 1s). O encoding é o "dicionário" que traduz esses números 
para letras que nós humanos lemos.

O grande problema é que sistemas operacionais diferentes usam dicionários padrão diferentes:

Linux e Mac: Usam o padrão utf-8 (que suporta caracteres do mundo todo, emojis, etc.).

Windows: Historicamente, usa padrões locais como o cp1252 (Windows-1252) no Brasil.

Se você criar um arquivo no Windows sem especificar o encoding e enviar para um colega que usa 
Linux (ou subir para um servidor na nuvem), os acentos (ç, ã, é) vão quebrar.

A Regra de Ouro: Sempre, SEMPRE, especifique encoding='utf-8' ao usar o with open em arquivos de texto.
'''

'''
Exemplo 1: Ciência de Dados (Criando e Lendo CSVs com Segurança)
Vamos criar um arquivo de dados fictício com nomes e endereços brasileiros. 
Vamos usar o modo 'w' (Write - escrever do zero) e depois o modo 'r' (Read - ler).
'''

# MODO 'w': Cria o arquivo (ou apaga o existente) e escreve
with open('clientes_sp.csv', 'w', encoding='utf-8') as arquivo:
    arquivo.write("id,nome,cidade\n")
    arquivo.write("1,João da Conceição,São Paulo\n")
    arquivo.write("2,Marta Araújo,Ribeirão Preto\n")

# MODO 'r': Abre para leitura. Se não colocarmos utf-8 aqui no Windows, 
# as palavras "Conceição" e "Araújo" e "São" podem dar erro ou ficar distorcidas.
with open('clientes_sp.csv', 'r', encoding='utf-8') as arquivo:
    print("--- Lendo os dados ---")
    for linha in arquivo:
        print(linha.strip())

'''
Exemplo 2: Cibersegurança (Modo Append 'a')
Em segurança, você nunca quer apagar o log do dia anterior. Você quer adicionar informações ao 
final do arquivo. Para isso usamos o modo 'a' (Append). Se o arquivo não existir, ele cria; 
se existir, ele coloca o cursor na última linha e não apaga nada.
'''

def registrar_log(mensagem):
    # Abrindo no modo 'a' (Append)
    with open('auditoria_sistema.txt', 'a', encoding='utf-8') as log:
        log.write(mensagem + '\n')

# Simulando eventos em momentos diferentes
registrar_log("14:00 - Sistema iniciado.")
registrar_log("14:05 - Tentativa de invasão detectada no IP 192.168.0.50!")

# Se você rodar esse script 5 vezes, o arquivo não será apagado,
# ele apenas terá as mensagens adicionadas ao final 10 vezes.

'''
Modos com + (Leitura e Escrita simultâneas)
Às vezes, você quer fazer as duas coisas ao mesmo tempo.

'r+': Abre para leitura e escrita. O arquivo deve existir. O cursor começa no início.

'w+': Abre para escrita e leitura. Ele apaga tudo o que tinha no arquivo antes (ou cria um novo).

'a+': Abre para adicionar e ler. O cursor começa no final do arquivo.

Dica: Ao usar modos com +, você precisará usar muito aquele método arquivo.seek(0) que vimos antes, 
porque se você escrever algo, o cursor vai para o final. Se tentar ler logo em seguida sem mover o 
cursor de volta pro início, não vai ler nada!

A Exceção à Regra: Modo Binário ('b')
A única vez em que você NÃO usa encoding é quando abre arquivos em modo binário ('rb', 'wb', 'ab').

Em Cibersegurança, você usa isso para analisar arquivos compilados (como um .exe suspeito) 
ou capturas de rede (arquivos .pcap). Em Ciência de Dados, você usa para ler imagens ou modelos 
treinados (como arquivos .pkl do Scikit-Learn).
'''

# Note que NÃO tem o argumento encoding=''
with open('malware_suspeito.exe', 'rb') as arquivo_binario:
    # Lendo os primeiros 16 bytes do arquivo
    cabecalho = arquivo_binario.read(16)
    print(f"Assinatura em bytes: {cabecalho}")