'''
Faça uma lista de compras com lista
o usuário deve ter a possibilidade de
inserir, apagar, e listar valores da sua lista
Não permita que o programa quebre com erros de 
indices inexistentes na lista.
'''

lista_compras = []

while True:
    print('1 - Adicionar item')
    print('2 - Apagar item')
    print('3 - Listar itens')
    print('4 - Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        item = input('Digite o item para adicionar: ')
        lista_compras.append(item)
        print(f'Item "{item}" adicionado à lista.')

    elif escolha == '2':
        try:
            indice = int(input('Digite o índice do item para apagar: '))
            if 0 <= indice < len(lista_compras):
                item_removido = lista_compras.pop(indice)
                print(f'Item "{item_removido}" removido da lista.')
            else:
                print('Índice inválido. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')

    elif escolha == '3':
        if len(lista_compras) > 0:
            print('Lista de Compras:')
            for i, item in enumerate(lista_compras):
                print(f'{i}: {item}')
        else:
            print('A lista de compras está vazia.')

    elif escolha == '4':
        print('Saindo do programa. Até mais!')
        break

    else:
        print('Opção inválida. Tente novamente.')