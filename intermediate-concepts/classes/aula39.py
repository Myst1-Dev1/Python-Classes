# os.remove. os.unlink e os.rename - apagando, renomeando e movendo arquivos

import os

'''
O módulo os (Operating System) é a principal ponte entre o seu código Python e o sistema operacional 
(Windows, Linux, Mac). É com ele que você cria pastas, navega pelos diretórios e, claro, apaga ou 
move arquivos.

Tanto para Ciência de Dados (organizar bases de dados em pastas) quanto para Cibersegurança 
(apagar rastros de um script ou mover arquivos maliciosos para quarentena), essas três funções são o 
seu "feijão com arroz".

Para usá-las, você precisa sempre importar o módulo no topo do arquivo: import os.

1. Apagando arquivos: os.remove e os.unlink
A primeira coisa que você precisa saber: os.remove() e os.unlink() fazem exatamente a mesma coisa.

Eles servem apenas para apagar arquivos. Se você tentar apagar uma pasta com eles, 
o Python vai jogar um erro na sua tela (IsADirectoryError).

os.remove() é o nome mais amigável e comum em Python.

os.unlink() é um nome que vem da linguagem C e de sistemas Unix (Linux/Mac). 
Existe no Python para manter compatibilidade histórica para programadores dessas áreas.

Exemplo prático (Limpando arquivos temporários):
Imagine que seu script de Ciência de Dados gerou um arquivo .csv temporário apenas 
para fazer um cálculo e agora você quer apagá-lo.
'''

caminho_arquivo = 'relatorio_temporario.csv'

# Criando um arquivo rápido só para o exemplo não dar erro
with open(caminho_arquivo, 'w') as f:
    f.write('dados temporarios')

# O jeito SEGURO de apagar (Padrão Luiz Otávio de qualidade)
# Sempre verifique se o arquivo existe antes de tentar apagá-lo!
if os.path.exists(caminho_arquivo):
    os.remove(caminho_arquivo)  # ou os.unlink(caminho_arquivo)
    print(f"O arquivo '{caminho_arquivo}' foi apagado com sucesso.")
else:
    print("Arquivo não encontrado.")


'''
2. Renomeando e Movendo: os.rename
O os.rename(origem, destino) é uma função duas em uma.

Se você mudar apenas o nome final no destino, ele renomeia.

Se você mudar a pasta no caminho de destino, ele move o arquivo.

Exemplo prático (Cibersegurança - Quarentena):
Vamos imaginar que seu script detectou que um arquivo chamado script_suspeito.exe é um malware. 
Você quer tirar ele da pasta de downloads e mover para uma pasta de quarentena, mudando a 
extensão dele para .txt para que ele não possa ser executado acidentalmente.
'''

# Caminhos (Estou usando caminhos relativos aqui)
arquivo_original = 'downloads/script_suspeito.exe'
novo_caminho = 'quarentena/ameaca_isolada.txt'

# Atenção: para o move funcionar, a pasta de destino ('quarentena') JÁ DEVE EXISTIR.
try:
    os.rename(arquivo_original, novo_caminho)
    print("Arquivo isolado e renomeado com sucesso!")
except FileNotFoundError:
    print("O arquivo original ou a pasta de destino não existem.")
except FileExistsError:
    print("Já existe um arquivo com esse nome no destino.")


'''
⚠️ Duas dicas avançadas para evitar dores de cabeça:
Diferentes Discos (Drives): O os.rename funciona perfeitamente para mover arquivos dentro do mesmo 
disco (ex: do C:\ para o C:\). Mas, no Windows, se você tentar mover um arquivo do disco C:\ para um 
pen drive no disco D:\ usando os.rename, ele pode falhar. Para mover entre discos diferentes, 
a comunidade prefere usar o módulo shutil (especificamente shutil.move()).

Tratamento de Erros: Note que no segundo exemplo eu usei try...except. Ao lidar com o 
sistema operacional, as coisas falham muito: você pode não ter permissão de administrador para apagar 
o arquivo, ele pode estar aberto em outro programa, ou a pasta sumiu. Sempre "abrace" suas operações 
de os com blocos de tratamento de erro ou condicionais como os.path.exists().
'''