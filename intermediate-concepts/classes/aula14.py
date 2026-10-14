# dir, hasattr e getattr em Python

string = 'peter'
metodo = 'upper'

if hasattr(string, metodo):
    print('Tem o medodo upper?')
    print(getattr(string, metodo)())
else:
    print('Não tem o metodo upper')