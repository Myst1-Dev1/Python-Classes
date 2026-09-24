#Exercicio - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

name = input('Digite seu nome: ')
correct_answers = 0

for i, p in enumerate(perguntas):
    print(f"\nPergunta {i + 1}: {p['Pergunta']}")

    opcoes = p['Opções']
    for idx, opcao in enumerate(opcoes):
        print(f"{idx}) {opcao}")
        
    resposta_usuario = input('Escolha a opção (número): ')
    
    try:
        indice_escolhido = int(resposta_usuario)
        if opcoes[indice_escolhido] == p['Resposta']:
            print('✅ Resposta correta!')
            correct_answers += 1
        else:
            print('❌ Resposta incorreta!')
    except (ValueError, IndexError):
        print('❌ Opção inválida! Você perdeu a chance desta pergunta.')

print(f"\nFim do jogo, {name}!")
print(f"Você acertou {correct_answers} de {len(perguntas)} perguntas.")