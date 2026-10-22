# 📘 Estudos em Python — Conceitos Intermediários

Documentação técnica de referência rápida e aprofundamento prático cobrindo os conceitos intermediários da linguagem Python. Esta base serve como guia definitivo para revisões de arquitetura de código, preparação técnica e consulta diária.

---

## 📑 Sumário

1. [Funções, Escopos e Assinaturas Avançadas](#1-funções-escopos-e-assinaturas-avançadas)
2. [Closures, Variáveis Livres e Funções de Primeira Classe](#2-closures-variáveis-livres-e-funções-de-primeira-classe)
3. [Dicionários e Conjuntos (Sets) em Profundidade](#3-dicionários-e-conjuntos-sets-em-profundidade)
4. [Comprehensions e Expressões Lambda](#4-comprehensions-e-expressões-lambda)
5. [Introspecção, Tipagem Dinâmica e Falsy/Truthy](#5-introspecção-tipagem-dinâmica-e-falsytruthy)
6. [Iterables, Iterators e Geradores (Lazy Evaluation)](#6-iterables-iterators-e-geradores-lazy-evaluation)
7. [Tratamento de Exceções e Resiliência (Fail-Fast)](#7-tratamento-de-exceções-e-resiliência-fail-fast)
8. [Modularização, Pacotes e Ciclo de Vida de Módulos](#8-modularização-pacotes-e-ciclo-de-vida-de-módulos)
9. [Decoradores e Metaprogramação](#9-decoradores-e-metaprogramação)
10. [Manipulação de Iteráveis com `itertools`](#10-manipulação-de-iteráveis-com-itertools)
11. [Programação Funcional e Recursão](#11-programação-funcional-e-recursão)
12. [Gestão de Recursos, Context Managers e Venv](#12-gestão-de-recursos-context-managers-e-venv)
13. [Persistência em Disco: File I/O, OS e JSON](#13-persistência-em-disco-file-io-os-e-json)
14. [Laboratório Prático: Exercícios Resolvidos](#14-laboratório-prático-exercícios-resolvidos)

---

## 1. Funções, Escopos e Assinaturas Avançadas

### Fundamentos e Assinatura
- **Funções (`def`)**: Blocos reutilizáveis com entrada (parâmetros) e saída determinística via `return` (retorno implícito é `None`).
- **Argumentos Posicionais vs Nomeados**: Parâmetros com valor padrão (`default`) devem sempre suceder parâmetros obrigatórios.
- **Assinaturas Restritivas (PEP 570 / PEP 3102)**:
  - `/` (*Positional-Only*): Força argumentos anteriores a serem passados exclusivamente por posição.
  - `*` (*Keyword-Only*): Força argumentos posteriores a serem passados obrigatoriamente nomeados.
  - `*args`: Empacota múltiplos argumentos posicionais em uma tupla imutável.
  - `**kwargs`: Empacota múltiplos argumentos nomeados em um dicionário.

```python
# Exemplo de controle estrito de assinatura
def configurar_conexao(host, /, porta=5432, *, timeout=30, **opcoes):
    # host: estritamente posicional
    # porta: posicional ou nomeado
    # timeout: estritamente nomeado
    return f"{host}:{porta} (timeout={timeout}s, extras={opcoes})"

configurar_conexao("localhost", 8080, timeout=10, ssl=True)
```

**Arquivos de estudo:**
- [aula1.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula1.py) — Introdução e retorno de funções
- [aula2.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula2.py) — Argumentos nomeados, posicionais e valores padrão
- [aula41.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula41.py) — Restrições Positional-Only (`/`) e Keyword-Only (`*`)

---

## 2. Closures, Variáveis Livres e Funções de Primeira Classe

### Regra de Escopo LEGB
Python pesquisa identificadores na seguinte ordem:
1. **L**ocal: Definido dentro da função corrente.
2. **E**nclosing: Definido em funções envelopadoras (aninhadas).
3. **G**lobal: Definido no topo do módulo (`global` keyword para mutação).
4. **B**uilt-in: Nomes internos da linguagem (`print`, `len`, `range`).

### First-Class Citizens & Higher Order Functions
Funções são tratadas como objetos de primeira classe: podem ser atribuídas a variáveis, passadas como argumentos ou retornadas por outras funções.

### Closures e a Palavra-chave `nonlocal`
Uma **closure** ocorre quando uma função aninhada referencia variáveis do escopo que a envelopa (*free variables* ou variáveis livres), mantendo o estado preservado na memória mesmo após o encerramento do escopo pai.
- Para alterar o valor dessa variável no escopo pai sem redefini-la como local, utiliza-se a palavra-chave `nonlocal`.

```python
def criar_contador(inicio=0):
    valor = inicio  # Variável livre (free variable)
    def incrementar(passo=1):
        nonlocal valor
        valor += passo
        return valor
    return incrementar

c1 = criar_contador(10)
print(c1(2))  # 12
print(c1(3))  # 15
```

**Arquivos de estudo:**
- [aula3.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula3.py) — Escopo de funções (`global` e `local`)
- [aula4.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula4.py) — Higher Order Functions e First-Class Functions
- [aula5.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula5.py) — Implementação prática de Closures
- [aula25.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula25.py) — Free variables e instrução `nonlocal`

---

## 3. Dicionários e Conjuntos (Sets) em Profundidade

### Dicionários (`dict`)
Estruturas associativas chave-valor baseadas em hash tables ($O(1)$ amortizado para busca/inserção).
- **Métodos Críticos**: `.get(chave, fallback)` (evita `KeyError`), `.update()`, `.pop()`, `.keys()`, `.values()`, `.items()`.
- **Cópia Rasa vs Profunda**:
  - `d.copy()` gera uma cópia rasa (*shallow copy*), compartilhando ponteiros de objetos aninhados.
  - `copy.deepcopy(d)` realiza a clonagem recursiva total de estruturas aninhadas.
- **Empacotamento e Desempacotamento**: Fusão elegante com `{**dict_a, **dict_b}`.

### Conjuntos (`set`)
Coleções não ordenadas de elementos únicos baseadas em hash.
- **Restrição**: Aceita apenas elementos imutáveis (*hashable*) internamente.
- **Operações Algébricas**:
  - União (`|` ou `.union()`): Todos os elementos de ambos.
  - Interseção (`&` ou `.intersection()`): Elementos presentes em ambos.
  - Diferença (`-` ou `.difference()`): Elementos exclusivos do primeiro conjunto.
  - Diferença Simétrica (`^` ou `.symmetric_difference()`): Elementos que não estão em ambos simultaneamente.

```python
admin_permissions = {"read", "write", "delete"}
user_permissions = {"read"}

revoked = admin_permissions - user_permissions  # {'write', 'delete'}
common = admin_permissions & user_permissions   # {'read'}
```

**Arquivos de estudo:**
- [aula6.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula6.py) — Dicionários, manipulação e `copy.deepcopy`
- [aula7.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula7.py) — Sets, unicidade e álgebra de conjuntos
- [aula9.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula9.py) — Desempacotamento e união de dicionários

---

## 4. Comprehensions e Expressões Lambda

Construções idiomáticas e pythônicas para transformação e filtragem declarativa de dados.

### Matriz de Sintaxe
| Estrutura | Sintaxe Base |
| :--- | :--- |
| **List Comprehension** | `[transformacao for item in iteravel if condicao]` |
| **Dict Comprehension** | `{k: v for k, v in iteravel if condicao}` |
| **Set Comprehension** | `{transformacao for item in iteravel if condicao}` |
| **Lambda Expression** | `lambda arg1, arg2: expressao_retornada` |

### List Comprehension com Operador Ternário
- Filtragem pura: `if` fica no final (`[x for x in lista if x > 0]`).
- Mapeamento condicional (Ternário): `if-else` fica no início (`[x if x > 0 else 0 for x in lista]`).

```python
produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Teclado", "preco": 150}
]

# Aumenta 10% nos produtos acima de R$ 100, mantendo os demais
ajustados = [
    {**p, "preco": round(p["preco"] * 1.10, 2)} if p["preco"] > 100 else {**p}
    for p in produtos
]
```

**Arquivos de estudo:**
- [aula8.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula8.py) — Funções anônimas lambda e ordenação com `sort(key=...)`
- [aula10.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula10.py) — List Comprehension (mapeamento, filtros e ternário)
- [aula11.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula11.py) — Dictionary Comprehension e Set Comprehension

---

## 5. Introspecção, Tipagem Dinâmica e Falsy/Truthy

### Avaliação Booleana (Truthy vs Falsy)
Em Python, objetos em contexto condicional avaliam para `True` ou `False` intrinsecamente:
- **Falsy**: `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()`, `range(0)`.
- **Truthy**: Qualquer estrutura preenchida ou número diferente de zero.

### Introspecção e Verificação em Tempo de Execução
- `isinstance(obj, (TipoA, TipoB))`: Checagem segura de tipos suportando tuplas de classes e herança.
- `hasattr(obj, 'nome_atributo')`: Valida existência de método/atributo.
- `getattr(obj, 'nome_atributo', fallback)`: Recupera dinamicamente a referência do atributo ou método.
- `dir(obj)`: Mapeia todos os atributos e métodos disponíveis no objeto.

```python
alvo = "dados_seguros"
metodo = "upper"

if hasattr(alvo, metodo):
    fn = getattr(alvo, metodo)
    print(fn())  # "DADOS_SEGUROS"
```

**Arquivos de estudo:**
- [aula12.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula12.py) — Verificação com `isinstance`
- [aula13.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula13.py) — Valores Truthy e Falsy, mutabilidade vs imutabilidade
- [aula14.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula14.py) — Introspecção dinâmica com `dir`, `hasattr` e `getattr`

---

## 6. Iterables, Iterators e Geradores (Lazy Evaluation)

A distinção fundamental para consumo eficiente de memória em larga escala:
- **Iterable**: Objeto que implementa o método dunder `__iter__()`. Pode ser percorrido por loops.
- **Iterator**: Objeto que implementa `__iter__()` e `__next__()`. Retém o estado do ponteiro e entrega um item por vez sob demanda.
- **Generator Expression**: Sintaxe com parênteses `(x for x in iterable)` que gera valores preguiçosamente (*lazy evaluation*).

### Generator Functions e `yield from`
Funções que utilizam `yield` suspendem seu estado de execução mantendo o frame na memória sem carregar toda a coleção no Heap. O operador `yield from` delega o controle diretamente para um subgerador ou iterável aninhado.

```python
def stream_logs():
    yield from ["INFO: Inicializado", "WARN: Memória 85%"]
    yield from ["ERROR: Falha de I/O"]

gen = stream_logs()
print(next(gen))  # "INFO: Inicializado"
```

**Arquivos de estudo:**
- [aula15.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula15.py) — Iterables, Iterators e Generator Expression
- [aula16.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula16.py) — Generator functions e ciclo do `yield`
- [aula17.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula17.py) — Delegação com `yield from`

---

## 7. Tratamento de Exceções e Resiliência (Fail-Fast)

### Estrutura Completa de Captura
O bloco de controle de fluxo de erros suporta 4 seções:
- `try`: Trecho com potencial risco de execução.
- `except Exception as err`: Captura erros específicos (evitar `except:` nu sem tipo).
- `else`: Executado exclusivamente se nenhuma exceção for disparada.
- `finally`: Executado incondicionalmente (garantia de liberação de recursos).

### Lançamento Explícito (`raise`)
Adotar a postura **Fail-Fast**: validar pré-condições logo no início do fluxo e lançar exceções explícitas com mensagens claras em vez de mascarar problemas.

```python
def registrar_usuario(nome: str, idade: int) -> dict:
    if not isinstance(idade, int) or idade < 0:
        raise ValueError(f"Idade inválida: {idade}. Deve ser um inteiro positivo.")
    if idade < 18:
        raise PermissionError("Usuário deve ser maior de idade para cadastro.")
    return {"nome": nome, "idade": idade, "status": "ativo"}
```

**Arquivos de estudo:**
- [aula18.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula18.py) — Fluxos `try`, `except`, `else` e `finally`
- [aula19.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula19.py) — Validação de contrato e disparo de exceções com `raise`

---

## 8. Modularização, Pacotes e Ciclo de Vida de Módulos

### Arquitetura de Módulos e Pacotes
- Módulos são arquivos `.py`. Pacotes são diretórios contendo módulos e opcionalmente um arquivo `__init__.py`.
- **Mecanismo de Importação**: O Python consulta caminhos registrados no `sys.path`.
- **Padrão Singleton de Módulos**: Módulos são executados apenas na primeira importação e armazenados em cache no `sys.modules`. Para forçar nova carga, recorre-se ao `importlib.reload()`.
- **Padrão `if __name__ == '__main__':`**: Isola rotinas de teste e execução CLI, impedindo execução colateral em caso de import.
- **Fachada via `__init__.py`**: Exposição controlada da API pública do pacote via `__all__` ou re-exportação direta, reduzindo acoplamento.

```
intermediate-concepts/classes/
├── aula21.py
├── aula21_operacoes.py
├── aula22.py
├── aula22_config.py
├── aula23_package/
│   └── modulo.py
└── aula24_package/
    ├── __init__.py
    ├── modulo_a.py
    └── modulo_b.py
```

**Arquivos de estudo:**
- [aula20.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula20.py) — Imports nativos (`import`, `from`, `as`, boas práticas)
- [aula21.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula21.py) & [aula21_operacoes.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula21_operacoes.py) — Modularização e isolamento de escopo
- [aula22.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula22.py) & [aula22_config.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula22_config.py) — `sys.modules` e recarregamento com `importlib.reload`
- [aula23.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula23.py) — Criação e estrutura de pacotes
- [aula24.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula24.py) — Inicialização de pacotes e fachada com `__init__.py`

---

## 9. Decoradores e Metaprogramação

### Sintaxe e Funcionamento
Decoradores são *Higher Order Functions* que recebem uma função alvo, injetam comportamentos antes/depois da sua execução e retornam uma nova função envolvida (*wrapper*).
A sintaxe `@decorador` é um mero *Syntax Sugar* para: `minha_funcao = decorador(minha_funcao)`.

### Fábrica de Decoradores (Decoradores com Parâmetros)
Quando o decorador precisa de parâmetros próprios (ex: `@retry(tentativas=3)`), implementa-se três camadas aninhadas:
1. **Fábrica**: Recebe a configuração do decorador.
2. **Decorador**: Recebe a função original.
3. **Wrapper**: Intercepta os argumentos (`*args`, `**kwargs`) e executa a lógica.

```python
def log_execucao(rotulo="AUDIT"):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"[{rotulo}] Executando: {func.__name__}")
            resultado = func(*args, **kwargs)
            print(f"[{rotulo}] Concluído.")
            return resultado
        return wrapper
    return decorador

@log_execucao(rotulo="DATABASE")
def consultar_status(servidor: str):
    return f"Servidor {servidor} OK"
```

**Arquivos de estudo:**
- [aula26.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula26.py) — Funções decoradoras básicas e empacotamento genérico
- [aula27.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula27.py) — Decoradores parametrizados (Fábricas de decoradores)

---

## 10. Manipulação de Iteráveis com `itertools`

O módulo nativo `itertools` implementa blocos algorítmicos em C voltados para consumo com eficiência $O(1)$ de memória:

- `itertools.count(start, step)`: Contador infinito stateful.
- `itertools.combinations(iter, r)`: Subconjuntos de tamanho $r$ onde a **ordem não importa** (sem repetição de pares idênticos).
- `itertools.permutations(iter, r)`: Subconjuntos de tamanho $r$ onde a **ordem importa**.
- `itertools.product(*iterables, repeat=1)`: Produto cartesiano (equivalente a loops `for` aninhados).
- `itertools.groupby(iterable, key)`: Agrupa itens consecutivos baseados em uma função chave.
  > **⚠️ Regra Crítica**: A coleção **deve estar previamente ordenada** pela mesma chave antes de invocar `groupby`, sob pena de gerar grupos fragmentados.

```python
from itertools import groupby

logs = [
    {"ip": "10.0.0.1", "status": "ALLOW"},
    {"ip": "10.0.0.2", "status": "DENY"},
    {"ip": "10.0.0.3", "status": "ALLOW"}
]

# Ordenação obrigatória pré-agrupamento
logs_ordenados = sorted(logs, key=lambda x: x["status"])

for status, grupo in groupby(logs_ordenados, key=lambda x: x["status"]):
    print(status, list(grupo))
```

**Arquivos de estudo:**
- [aula28.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula28.py) — Geradores infinitos com `itertools.count`
- [aula29.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula29.py) — Combinatória: `combinations`, `permutations` e `product`
- [aula30.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula30.py) — Agrupamento determinístico com `itertools.groupby`

---

## 11. Programação Funcional e Recursão

### Tríade Funcional Clássica
- `map(func, iteravel)`: Aplica transformação homogênea em cada elemento, retornando um iterador (sem mutar a coleção original).
- `filter(func_booleana, iteravel)`: Filtra elementos cujo predicado resulte em `True`.
- `functools.reduce(func_acumuladora, iteravel, inicializador)`: Agrega/esmaga a coleção iterativa em um valor escalar cumulativo.

### Recursividade e Caso Base
Função recursiva é aquela que invoca a si mesma. Exige obrigatoriamente:
1. **Caso Base (Condição de Parada)**: Evita recursão infinita e saturação de pilha (*Stack Overflow*).
2. **Caso Recursivo**: Convergência em direção ao caso base.
- Configuração do limite: `sys.getrecursionlimit()` e `sys.setrecursionlimit()`.

```python
def fatorial(n: int) -> int:
    # 1. Caso base
    if n <= 1:
        return 1
    # 2. Caso recursivo
    return n * fatorial(n - 1)
```

**Arquivos de estudo:**
- [aula31.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula31.py) — Mapeamento de dados com `map`
- [aula32.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula32.py) — Filtragem declarativa com `filter`
- [aula33.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula33.py) — Redução e agregação com `functools.reduce`
- [aula34.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula34.py) — Recursão, caso base e limites de pilha

---

## 12. Gestão de Recursos, Context Managers e Venv

### Ambientes Virtuais (`venv`)
Isolamento hermético das dependências do projeto para evitar conflito de versões no interpretador do sistema:
- Criação: `python -m venv .venv`
- Ativação (Windows PowerShell): `.\.venv\Scripts\Activate.ps1`
- Exportação de dependências: `pip freeze > requirements.txt`

### Gerenciador de Contexto (`with`)
O padrão de gerenciador de contexto implementa o protocolo `__enter__()` e `__exit__()`, garantindo que arquivos, sockets e conexões sejam desalocados de maneira determinística, mesmo em cenários de exceções não tratadas.

**Arquivos de estudo:**
- [aula35.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula35.py) — Isolamento de ambientes com `venv`
- [aula36.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula36.py) — Protocolo `with` e Context Managers

---

## 13. Persistência em Disco: File I/O, OS e JSON

### Modos de Abertura (`with open`)
| Modo | Ação | Descrição Técnica |
| :---: | :--- | :--- |
| `'r'` | Leitura (Padrão) | Abre para leitura; falha com `FileNotFoundError` se não existir. |
| `'w'` | Escrita | Sobrescreve integralmente ou cria o arquivo novo. |
| `'a'` | Append | Posiciona ponteiro no final do arquivo sem sobrescrever. |
| `'x'` | Criação Exclusiva | Cria o arquivo; falha se o arquivo já existir. |
| `'+'` | Atualização | Acrescenta permissão combinada (ex: `'r+'`, `'w+'`). |
| `'b'` | Modo Binário | Manipula bytes puros (`rb`, `wb`) para imagens/PDFs. |

> **Encoding Obligatório**: Sempre explicitar `encoding='utf-8'` para evitar corrupção em transferências interplataforma (Windows cp1252 vs Linux UTF-8).

### Módulo `json` e Módulo `os`
- **JSON**:
  - `json.dump(dado, fp, indent=2, ensure_ascii=False)`: Escreve estrutura nativa diretamente em arquivo aberto.
  - `json.load(fp)`: Lê de arquivo convertendo para tipos Python.
  - `json.dumps()` / `json.loads()`: Operações idênticas executadas em memória sobre strings.
- **OS**:
  - `os.rename(origem, destino)`: Renomeia ou move arquivos atomicamente.
  - `os.remove(caminho)` / `os.unlink()`: Apaga arquivo do disco.

```python
import json

dados_auditoria = {"status": "success", "eventos": [101, 102]}

with open("auditoria.json", "w", encoding="utf-8") as file:
    json.dump(dados_auditoria, file, indent=4, ensure_ascii=False)
```

**Arquivos de estudo:**
- [aula37.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula37.py) — Métodos do `TextIOWrapper` (`read`, `readline`, `seek`)
- [aula38.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula38.py) — Modos de abertura de arquivos e padronização de encodings
- [aula39.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula39.py) — Operações com `os.remove`, `os.rename` e caminhos
- [aula40.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/classes/aula40.py) — Serialização estruturada com o módulo `json`

---

## 14. Laboratório Prático: Exercícios Resolvidos

Nesta seção, consolidam-se os padrões arquiteturais através da resolução dos exercícios práticos:

| Exercício | Arquivo | Foco Técnico e Padrões Aplicados |
| :--- | :--- | :--- |
| **Exercício 1** | [exercise1.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/exercises/exercise1.py) | **Acumulador com `*args`**: Função de multiplicação com desempacotamento dinâmico de argumentos não-nomeados e verificação par/ímpar. |
| **Exercício 2** | [exercise2.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/exercises/exercise2.py) | **Closures e Fábrica de Funções**: Multiplicadores dinâmicos (duplicar, triplicar, quadruplicar) reaproveitando o escopo externo. |
| **Exercício 3** | [exercise3.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/exercises/exercise3.py) | **CLI Interativa e Estrutura de Dicionários**: Motor de perguntas e respostas com validação de opções e cálculo de assertividade. |
| **Exercício 4** | [exercise4.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/exercises/exercise4.py) | **Complexidade Algorítmica $O(N)$ com `set`**: Algoritmo para identificação do primeiro elemento duplicado com base na segunda ocorrência usando busca em hash table. |
| **Exercício 5** | [exercise5.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/exercises/exercise5.py) | **Imutabilidade e List Comprehensions**: Ajuste percentual em massa via deepcopy e ordenação encadeada (`sorted` com `key=lambda`). |
| **Exercício 6** | [exercise6.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/exercises/exercise6.py) | **Currying / Aplicação Parcial de Funções**: Padrão de adiamento de execução de chamadas funcionais retendo o primeiro operando via closure. |
| **Exercício 7** | [exercise7.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/exercises/exercise7.py) | **Função Zipper**: Implementação manual do emparelhamento de listas assimétricas orientada pelo menor comprimento, comparada a `zip` e `itertools.zip_longest`. |
| **Exercício 8** | [exercise8.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/exercises/exercise8.py) | **Combinação de Fluxos com `zip`**: Soma vetorial de duas listas numéricas combinando `zip` com List Comprehension funcional. |
| **Exercício 9** | [exercise9.py](file:///D:/Estudo-aulas/Python/intermediate-concepts/exercises/exercise9.py) | **Aplicação CLI com Histórico e Persistência**: Sistema completo de Todo-List com pilhas de `desfazer`/`refazer` (Undo/Redo), separação de comandos e persistência atômica em arquivo JSON com tratamento defensivo de erros. |

---

## 📌 Guia de Boas Práticas (Tech Lead Checklist)

1. **Assinaturas Estritas**: Restrinja argumentos com `/` e `*` para evitar acoplamento acidental da API a nomes de parâmetros internos.
2. **Imutabilidade nas Transformações**: Prefira gerar novos dicionários e listas (via Comprehensions) em vez de aplicar mutações diretas em coleções de entrada.
3. **Gerenciamento Seguro de Arquivos**: Nunca abra arquivos sem o bloco `with` acompanhado de `encoding='utf-8'`.
4. **Resolução de Erros Explicita**: Adote a postura Fail-Fast com `raise` descritivo. Evite blocos `except:` vazios que engolem falhas críticas.
5. **Memória sob Controle**: Utilize Geradores (`yield`) e Itertools para fluxos volumosos de dados a fim de manter consumo constante de memória $O(1)$.
