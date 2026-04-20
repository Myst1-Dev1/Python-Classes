
Alguns conceitos iniciais sobre python:

    # Permite escrever um comentário em uma unica linha;

    ''' hello ''' ou """ hello """ -> é chamado de Docstring: Permite escrever um comentário em múltiplas linhas;

    Print -> função que permite imprime uma mensagem na tela;
    print(12 , 35, sep="-") -> É exibido 12-35 sep = separator, o que separa os valores;
    print(12, 35, 1011, sep='-', end='##\n') -> end = o que é colocado no final da linha, por padrão é \n (quebra de linha)

    ###

    Sobre strings:

        str -> string -> texto
        Strings são textos que estão dentro de aspas simples ou duplas

        # Aspas simples
        print('Olá, Mundo!')
        print(1, 'olá, "mundo"')
        # Aspas duplas
        print("Olá, Mundo")
        print(1, "olá, 'mundo'")
        # Escape
        print("Olá, Mundo! \"Bem-vindo ao curso de Python!\"")
        # r
        print(r"Olá, Mundo! \"Bem-vindo ao curso de Python!\"")

    Código acima exibido em tela:

        Ol�, Mundo!
        1 ol�, "mundo"
        Ol�, Mundo
        1 ol�, 'mundo'
        Ol�, Mundo! "Bem-vindo ao curso de Python!"
        Ol�, Mundo! \"Bem-vindo ao curso de Python!\"

    ###

    ###

    Tipos int e float:

        int -> Número inteiro
        o tipo int representa qualquer número positivo ou negativo. int sem sinal é considerado positivo

        print(11), # int
        print(-11) # int
        print(0) # int

        float -> Número com ponto flutuante
        o tipo float representa qualquer número positivo ou negativo com ponto flutuante. float sem sinal é considerado positivo

        print(3.14) # float
        print(-3.14) # float
        print(0.0) # float

        A função type mostra o tipo que o Python inferiu ao valor.

        print(type('Myst')) exibido -> <class 'str'>
        print(type(1.1)) exibido -> <class 'float'>
        print(type(1)) exibido -> <class 'int'>

    ###

    Tipo de dado bool (boolean)

    Ao questionar algo em um programa. só existem duas respostas possíveis: sim(True) ou não(False).
    Existem vários operadores para "questionar". Dentre eles o ==, que é um operador lógico para questionar se um valor é igual ao outro;

    print(10 == 10); # true
    print(10 == 11); # false
    print(type(True)) # bool
    print(type(False)) # bool
    print(type(10 == 10)) # bool
    print(type(10 == 11)) # bool

    ##

    ##

    Conversão de tipos, coerção
    type convertion, typecasting, coercion é o ato de converter um tipo em outro.
    tipos imutaveis e primitivos:
    str, int, float, bool

    print(int('1'), type(int('1')));
    print(int('1') + 1);
    print(float(1) + 1);
    print(float('1.5'), type(float('1.5')));
    print(bool(''))
    print(str(11) + 'b');

    ##

    ##

    Variáveis são usadas para salvar algo na memória do computador.
    PEP8: inicie variavéis com letras minúsculas, pode usar números e underline _.
    O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome(variável).
    Uso: nome_variavel = expressão

    nome_completo = "Myst Vas";
    soma = 2 + 2;
    int_um = int("1");
    idade = 24
    maior_de_idade = idade >= 18

    print(nome_completo);
    print(soma);
    print(int_um, type(int_um));
    print(idade);
    print(maior_de_idade);
    print("Nome completo: " + str(nome_completo) + ", Idade: " + str(idade) + ", É maior de idade: " + str(maior_de_idade))

    ##

    ##

    Introdução aos operadores aritmeticos

   adicao = 10 + 10
    print('adicao', adicao)

    subtracao = 10 - 10
    print('subtracao', subtracao)

    multiplicacao = 10 * 10
    print('multiplicacao', multiplicacao)

    divisao = 10 / 2.2
    print('divisao', divisao)

    divisao_inteira = 10 // 2.2
    print('divisao_inteira', divisao_inteira)

    exponenciacao =  2 ** 10
    print('exponenciacao', exponenciacao)

    modulo = 55 % 2
    print('modulo', modulo)

    ##

    ##

    Concatenação e repetiçao com operadores atmeticos

    concatenacao = 'A' + 'B' + 'C'
    print(concatenacao)

    a_dez_vezes = 'A' * 10
    tres_vezes_myst = 3 * 'Myst'
    print(a_dez_vezes)
    print(tres_vezes_myst)

    ##

    ##

    Precedencia entre os operadores aritmeticos

    # 1. (n + n)
    # 2. **
    # 3. * / //%
    # 4. + -

    conta_1 = 1 + 1 ** 5 + 5
    conta_2 = (1 + 1) ** (5 + 5)
    print(conta_1)
    print(conta_2)


    ##