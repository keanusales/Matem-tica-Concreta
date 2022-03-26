import random
vt, v1, v2 = [], [], []
s1, s2, f1, f2 = [], [], 0, 0
for a in range(100):
    vt.insert(a, a)
for i in range(100):
    random.shuffle(vt)
    for j in range(100):
        v1.insert(j, 0)
        v2.insert(j, 0)
    v1.insert(vt[i], 1)
    for j in range(100):
        if v1[j] != v2[j]:
            s1.insert(i, j + 1)
            break
    random.shuffle(vt)
    for j in range(100):
        if v1[vt[j]] != v2[vt[j]]:
            s2.insert(i, j + 1)
            break
for i in range(100):
    f1 = f1 + s1[i]
    f2 = f2 + s2[i]
f1 = f1 / 100
f2 = f2 / 100
print("Sequencialmente a média foi:", f1)
print("Aleatoriamente a média foi:", f2)