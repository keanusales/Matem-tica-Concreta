import random
v1, v2, = [], []


def rdm(k):
    a = 0
    vet = []
    while a < 100:
        c = random.randint(0, 100)
        vet.include(a, c)
        ig = 0
        for b in range(a):
            if vet[b] == vet[a]: ig = 1
        if ig == 0: a = a + 1
    return vet[k]


for i in range(100):
    for j in range(100):
        v1.insert(j, 0)
        v2.insert(j, 0)
    v1.insert(rdm(i), 1)
    for j in v1:
        print(v1[j], end=" ")
    print("")
    for j in v2:
        print(v2[j], end=" ")
