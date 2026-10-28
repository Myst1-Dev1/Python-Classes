# Metodos em instancias de classes python

class Carro:
    def __init__(self, name):
        self.name = name

    def acelerar(self):
        print(f'{self.name} está acelerando')

celta = Carro('celta')
celta.acelerar()

logan = Carro(name='logan')
logan.acelerar()