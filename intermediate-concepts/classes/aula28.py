# count é um iterador sem fim (iterrtools)

from itertools import count

c1 = count(step=5, start=5)

print(c1)

for i in c1:
    if i > 100:
        break
    print(i)