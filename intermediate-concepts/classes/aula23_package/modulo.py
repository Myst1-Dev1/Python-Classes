# Fazendo da forma abaixo ao importar com : import * só será importado
# o que está dentro de []

__all__ = [
    'soma'
]

def soma(x, y):
    return x + y