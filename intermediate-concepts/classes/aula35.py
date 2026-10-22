# Ambientes virtuais em Python (venv)

'''
Um ambiente virtual (venv) é como uma "caixa de areia" isolada para o seu projeto. Ele cria 
uma instalação do Python exclusiva para aquela pasta, totalmente separada do Python global do seu 
computador.

Se o seu computador fosse uma oficina, usar o Python global seria jogar todas as ferramentas 
(bibliotecas) em uma única caixa gigante. Com o tempo, as ferramentas se misturam e causam 
problemas. O venv cria uma caixa de ferramentas separada para cada cliente (projeto).

Por que isso é obrigatório em Ciência de Dados e Cibersegurança?
Ciência de Dados: Você pode ter um projeto de 2022 que usa a biblioteca pandas na versão 1.0, e 
um projeto de 2026 que exige o pandas versão 2.0. Se você atualizar no Python global, seu 
projeto antigo para de funcionar. O venv garante que cada projeto tenha a versão exata que precisa.

Cibersegurança: Você frequentemente fará o download de scripts ou ferramentas do GitHub criadas 
por outros hackers ou pesquisadores. Muitas dessas ferramentas dependem de bibliotecas antigas e 
específicas (como versões vulneráveis do urllib3 ou requests). Rodar isso no Python global do seu 
sistema operacional pode "quebrar" outras ferramentas de rede da sua própria máquina.

Como criar e usar na prática (Passo a Passo)
Abra o terminal do seu sistema operacional, navegue até a pasta do seu projeto e siga estes passos:

1. Criando o ambiente virtual
O padrão da comunidade é dar o nome da pasta também de venv, mas você pode escolher qualquer nome.

Bash
python -m venv venv
Isso vai criar uma pasta chamada venv cheia de arquivos. Você nunca deve mexer nos arquivos de dentro 
dela manualmente.

2. Ativando o ambiente virtual
Você precisa "ligar" o ambiente para o terminal saber que deve usar o Python isolado, e não o global.

No Windows:

Bash
venv\Scripts\activate
No Linux ou Mac:

Bash
source venv/bin/activate
(Se der certo, o nome (venv) vai aparecer no começo da linha do seu terminal).

3. Instalando bibliotecas isoladas
Agora, qualquer coisa que você instalar, ficará apenas nessa pasta.

Bash
pip install pandas requests
4. Salvando suas ferramentas (A regra de ouro)
Como o ambiente virtual é apenas uma pasta pesada, você nunca envia ela para o GitHub 
ou para outro colega. Em vez disso, você gera um arquivo de texto com a "receita" de tudo o 
que instalou:

Bash
pip freeze > requirements.txt
Quando outro cientista de dados ou analista de segurança baixar seu projeto, ele cria o próprio 
venv dele e roda: pip install -r requirements.txt.

5. Desativando o ambiente
Quando terminar de trabalhar no projeto, basta digitar:

Bash
deactivate
'''