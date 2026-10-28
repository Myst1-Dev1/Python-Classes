# Escopo da classe e de metodos da classe

class ScannerRede:
    # 1. ESCOPO DA CLASSE (Atributo de Classe)
    # Todos os scanners vão compartilhar a mesma porta padrão no início.
    porta_padrao = 80  

    def __init__(self, ip_alvo):
        # 2. ESCOPO DA INSTÂNCIA
        # Cada scanner terá o seu próprio IP.
        self.ip = ip_alvo 

    def escanear(self):
        # 3. ESCOPO LOCAL DO MÉTODO
        # Essa variável 'mensagem' só existe aqui dentro. 
        # O resto da classe não sabe que ela existe.
        mensagem = "Iniciando varredura..." 
        print(mensagem)
        
        # O GRANDE SEGREDO DO ESCOPO NO PYTHON:
        # Se você tentar printar só 'porta_padrao' ou 'ip', vai dar ERRO.
        # O método não enxerga fora dele. Você precisa usar o 'self.' ou o nome da classe.
        
        print(f"Buscando no IP: {self.ip}")
        
        # Para acessar a variável do escopo da classe, você tem duas opções:
        print(f"Testando porta: {self.porta_padrao}")       # Opção 1 (via objeto)
        print(f"Testando porta: {ScannerRede.porta_padrao}") # Opção 2 (direto na classe)

# Testando
scanner1 = ScannerRede('192.168.0.1')
scanner1.escanear()

# Se eu tentar printar 'mensagem' aqui fora, o Python dá erro, 
# porque ela já "morreu" quando o escanear() terminou.
# print(scanner1.mensagem) # ERRO!