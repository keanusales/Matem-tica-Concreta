import random
import matplotlib.pyplot as m
v1, v2, v3, f1 = [], [], [], 0
s1, s2, vt, f2 = [], [], [], 0
for i in range(100):
    v3.insert(i, i)
for i in range(100):
    vt.insert(i, i)
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
m.plot(v3, s1, color="Red")
m.plot(v3, s2, color="Blue")
m.show()
for i in range(100):
    f1 = f1 + s1[i]
    f2 = f2 + s2[i]
f1 = f1 / 100
f2 = f2 / 100
print("Sequencialmente a média foi:", f1)
print("Aleatoriamente a média foi:", f2)