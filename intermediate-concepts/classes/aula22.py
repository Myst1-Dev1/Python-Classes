# Recarregando modulos, impotlib e singleton

'''
1. O que é o importlib (Recarregando módulos)?
Por padrão, quando você importa um módulo em Python, ele é carregado apenas na primeira vez.
Se você alterar o código daquele arquivo .py enquanto o programa está rodando,
o Python não atualiza as mudanças automaticamente. O módulo importlib possui a função reload() 
que força o Python a ler o arquivo atualizado da máquina sem precisar reiniciar o script.

2. O que é o padrão Singleton?
O Singleton é um padrão de projeto (design pattern) que garante que uma classe tenha apenas uma única 
instância em todo o ciclo de vida do programa, fornecendo um ponto global de acesso a ela 
(muito usado em conexões de banco de dados, arquivos de configuração ou logs).
'''

import importlib
import aula22_config

# --- PADRÃO SINGLETON ---
class GerenciadorConfiguracao:
    _instancia = None

    def __new__(cls):
        # Garante que só existe UM objeto desta classe na memória
        if cls._instancia is None:
            print("-> Criando a única instância do Singleton (GerenciadorConfiguracao)...")
            cls._instancia = super(GerenciadorConfiguracao, cls).__new__(cls)
            cls._instancia.atualizar_dados()
        return cls._instancia

    def atualizar_dados(self):
        # Carrega ou recarrega os dados do módulo config.py
        self.versao = aula22_config.VERSAO_SISTEMA
        self.manutencao = aula22_config.MODO_MANUTENCAO

    def recarregar_configuracoes(self):
        print("\n[Ação] Forçando a recarga do módulo 'config' com importlib...")
        # Usa o importlib para atualizar o módulo que mudou no disco
        importlib.reload(aula22_config)
        # Atualiza os valores dentro do Singleton
        self.atualizar_dados()

# --- TESTANDO O SISTEMA ---

# 1. Criando a primeira instância do Singleton
cfg1 = GerenciadorConfiguracao()
print(f"Versão inicial: {cfg1.versao} | Manutenção: {cfg1.manutencao}")

# 2. Provando que é Singleton (tentando criar uma segunda instância)
cfg2 = GerenciadorConfiguracao()
print(f"cfg1 é o mesmo objeto que cfg2? {cfg1 is cfg2}")

# 3. Simulando alteração no arquivo config.py via código (para fins didáticos)
print("\n--- Simulando alteração manual no arquivo config.py ---")
aula22_config.VERSAO_SISTEMA = "2.0"
aula22_config.MODO_MANUTENCAO = True

# Veja que sem recarregar, o Singleton ainda está com os valores antigos:
print(f"Antes do reload (cfg1): Versão {cfg1.versao}")

# 4. Usando o importlib para recarregar as configurações em tempo de execução
cfg1.recarregar_configuracoes()

# 5. Agora os dados estão atualizados na mesma instância única!
print(f"Após o reload (cfg1): Versão {cfg1.versao} | Manutenção: {cfg1.manutencao}")