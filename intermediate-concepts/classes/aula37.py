# with open (context manager) e metodos uteis do TextIOWrapper

'''
Quando você usa a função open() no Python em modo de texto (o padrão), ela não retorna o texto 
do arquivo imediatamente. Ela retorna um objeto chamado TextIOWrapper. Ele é, essencialmente, o seu 
"controle remoto" para interagir com o sistema de arquivos do seu computador.

Compreender os métodos desse objeto e os modos de abertura é vital para processar arquivos de 
log gigantescos em Cibersegurança ou datasets massivos em Ciência de Dados sem 
travar o seu computador.
'''

# Modos de Abertura Principais
# Para criar o TextIOWrapper, você precisa informar como quer abrir o arquivo.

'''
Métodos Essenciais do TextIOWrapper
1. Métodos de Leitura

arquivo.read(): Lê o arquivo inteiro e o coloca na memória do computador como uma única string. 
Cuidado: Se você fizer isso com um dump de banco de dados de 10 GB, a memória RAM vai estourar 
e o script vai "crashar". Você pode passar um número de caracteres: read(10) lê apenas os primeiros 
10 caracteres.

arquivo.readline(): Lê apenas uma linha por vez. Excelente para economizar memória.

arquivo.readlines(): Lê todas as linhas e as devolve dentro de uma grande lista. Também é perigoso 
para arquivos gigantescos.

2. Métodos de Escrita

arquivo.write('texto'): Escreve a string exata no arquivo. Ele não adiciona quebra de linha 
automaticamente, você precisa incluir o \n no final da string se quiser descer uma linha.

arquivo.writelines(lista): Recebe um iterável (como uma lista ou tupla) de strings e as escreve 
no arquivo de uma vez.

3. Controle do Cursor (Avançado e muito útil)
Imagine que o Python tem um "cursor" (igual ao do mouse piscando no Word) dentro do arquivo. 
Conforme ele lê ou escreve, o cursor avança para a direita e para baixo.

arquivo.tell(): Informa em qual posição exata (em bytes) o seu cursor está no momento.

arquivo.seek(0): Move o cursor para o byte indicado (neste caso, 0, o início absoluto do arquivo). 
Isso é muito usado quando você lê um arquivo até o fim, mas precisa relê-lo no mesmo script sem ter 
que fechá-lo e abri-lo novamente.

O Jeito "Pythonic" (Otimizado para Memória)
Tanto o professor Luiz Otávio quanto profissionais seniores evitam usar o .read() ou .readlines() 
em dados pesados. A melhor forma de extrair dados é iterar diretamente sobre o objeto TextIOWrapper.

Isso funciona como um gerador: o Python puxa apenas uma linha do disco rígido para a RAM, 
processa e a descarta. Veja um exemplo prático aplicado a logs de segurança:
'''

ip_malicioso = "198.51.100.22"

with open('acessos_servidor.log', 'r') as arquivo:
    print(f"O cursor começou no byte: {arquivo.tell()}")
    
    # Iterar direto no 'TextIOWrapper' gasta quase zero RAM, não importa o tamanho do log
    for linha in arquivo:
        if ip_malicioso in linha:
            print(f"ALERTA! IP suspeito detectado: {linha.strip()}")
            break # Interrompe o loop na primeira ocorrência
            
    print(f"O cursor parou no byte: {arquivo.tell()}")
    
    # Reiniciando o arquivo para uma nova análise
    arquivo.seek(0)
    print(f"Cursor movido de volta para o byte: {arquivo.tell()}")