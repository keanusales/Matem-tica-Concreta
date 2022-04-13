import random as rdm
# Importa a biblioteca para randomizar coisas
import matplotlib.pyplot as plt
# Importa a biblioteca para criar e mostar gráficos
v1, v2, v3, f1 = [], [], [], 0
vt, s1, s2, f2 = [], [], [], 0
for i in range(100):
    vt.append(i)
# Cria um vetor vt com os índices 0 a 100 dos
# vetores, que futuramente vai ser embaralhado
for i in range(100):
# Faz 100 vezes o processo de criar 2 vetores
    for j in range(100):
        v1.insert(j, 0)
        v2.insert(j, 0)
    # Cria os 2 vetores com 100 índices cada
    rdm.shuffle(vt)
    # O vetor vt é embaralhado randomicamente
    v1.insert(vt[i], 1)
    # Insere "1" no vetor v1 com um índice
    # aleatório definido por vt[i], onde nesse
    # vt[i] há um número aleatório entre 0 e 100,
    # já que vt foi embaralhado randomicamente
    for j in range(100):
        if v1[j] != v2[j]:
            s1.insert(i, j + 1)
            break
    # Percorre sequencialmente os 2 vetores até
    # achar o ponto em que são diferentes e
    # armazena esse ponto em um outro vetor
    rdm.shuffle(vt)
    # O vetor vt é embaralhado randomicamente
    for j in range(100):
        if v1[vt[j]] != v2[vt[j]]:
            s2.insert(i, j + 1)
            break
for i in range(100):
    v3.append(i + 1)
plt.plot(v3, s1, color = "r")
plt.plot(v3, s2, color = "k")
plt.show()
for i in range(100):
    f1 = f1 + s1[i]
    f2 = f2 + s2[i]
f1, f2 = f1 / 100, f2 / 100
print("Sequencialmente a média foi:", f1)
print("Aleatoriamente a média foi:", f2)