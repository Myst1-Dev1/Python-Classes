# Introdução as Generator function em Python
# generator = (n for n in range(10000))

def generator(n = 0, maximun = 10):
    while True:
        yield n

        n += 1

        if n > maximun:
            return('Acabou')

gen = generator()

for n in gen:
    print(n)