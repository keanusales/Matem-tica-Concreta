import random as rdm
import matplotlib.pyplot as plt
v1, v2, v3, f1 = [], [], [], 0
vt, s1, s2, f2 = [], [], [], 0
for i in range(100):
    v1.insert(i, i)
for i in range(100):
    vt.insert(i, i)
for i in range(100):
    rdm.shuffle(vt)
    for j in range(100):
        v2.insert(j, 0)
        v3.insert(j, 0)
    v2.insert(vt[i], 1)
    for j in range(100):
        if v2[j] != v3[j]:
            s1.insert(i, j + 1)
            break
    rdm.shuffle(vt)
    for j in range(100):
        if v2[vt[j]] != v3[vt[j]]:
            s2.insert(i, j + 1)
            break
plt.plot(v1, s1, color="Red")
plt.plot(v1, s2, color="Blue")
plt.show()
for i in range(100):
    f1 = f1 + s1[i]
    f2 = f2 + s2[i]
f1, f2 = f1 / 100, f2 / 100
print("Sequencialmente a média foi:", f1)
print("Aleatoriamente a média foi:", f2)