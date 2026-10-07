# isInstance - para saber se o objeto e de determinado tipo

lista = ['a', 1, 1.1, True, [0, 1 , 2, 3], (1, 2), { 0, 1 }, {'nome': 'Peter'}]

for item in lista:
    if isinstance(item, set):
        print('Set')
        item.add(5)
        print(item, isinstance(item, set))
    elif isinstance(item, str):
        print('str')
        print(item.upper)
    elif isinstance(item, (int, float)):
        print('num')
        print(item, item * 2)
    else:
        print('OUTRO')