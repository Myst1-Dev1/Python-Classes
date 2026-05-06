'''
Faça um jogo para o usuário advinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas 
uma letra.
- Quando o usuário digitar uma letra , voce vai conferir se a letra digitada esta presente na palavra
secreta.
   - Se a letra digitada estiver na palavra secreta exiba a letra
    - se a letra digitada nao estiver presente na palavra secreta exiba um asterisco (*)
Faça a contagem de tentativas do seu usuário
'''

palavra_secreta = 'coxinha'
letras_acertadas = ''
tentativas = 0

while True:
    letra = input('Digite uma letra: ').lower()
    tentativas += 1

    # validação: apenas 1 letra
    if len(letra) != 1:
        print('Digite apenas UMA letra.')
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra:', palavra_formada)
    print('Tentativas:', tentativas)

    # condição de vitória
    if palavra_formada == palavra_secreta:
        print('Parabéns! Você acertou!')
        break