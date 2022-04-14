import random as rdm
# Importa a biblioteca para randomizar coisas
import matplotlib.pyplot as plt
# Importa a biblioteca para criar e mostrar gráficos
v1, v2, v3, f1 = [], [], [], 0
vt, s1, s2, f2 = [], [], [], 0
for i in range(100):
    vt.append(i)
# Cria um vetor vt com os índices 0 a 99 dos
# vetores, que futuramente vai ser embaralhado
for i in range(100):
# Faz 100 vezes todos os processos abaixo
    for j in range(100):
        v1.insert(j, 0)
        v2.insert(j, 0)
    # Cria os 2 vetores com 100 índices cada
    rdm.shuffle(vt)
    # O vetor vt é embaralhado randomicamente
    v1.insert(vt[i], 1)
    # Insere "1" no vetor v1 com um índice
    # aleatório definido por vt[i], onde nesse
    # vt[i] há um número aleatório entre 0 e 99,
    # já que vt foi embaralhado randomicamente
    for j in range(100):
        if v1[j] != v2[j]:
            s1.insert(i, j + 1)
            break
    # Percorre sequencialmente os 2 vetores até
    # achar o ponto em que são diferentes e
    # armazena esse ponto em um outro vetor (s1)
    rdm.shuffle(vt)
    # O vetor vt é embaralhado randomicamente
    for j in range(100):
        if v1[vt[j]] != v2[vt[j]]:
            s2.insert(i, j + 1)
            break
    # Após vt ter sido embaralhado novamente,
    # as 2 sequencias são percorridas randomica-
    # mente, onde os índices não são repetidos
    # As posições são salvas no vetor s2
# Os processos do loop for acabam aqui
for i in range(100):
    v3.append(i + 1)
# Gera um vetor que será o vetor "x" dos gráficos
plt.plot(v3, s1, color = "r")
# Gera o vetor com as posições dos percorrimentos
# sequenciais, onde esse vetor está em vermelho
plt.plot(v3, s2, color = "k")
# Gera o vetor com as posições dos percorrimentos
# randômicos, onde esse vetor está em preto
plt.show() # Exibe os 2 vetores
for i in range(100):
    f1 = f1 + s1[i] # Sequencialmente
    f2 = f2 + s2[i] # Aleatoriamente
f1, f2 = f1 / 100, f2 / 100
# A parte acima faz a média de ambos percorrimentos
print("Sequencialmente a média foi:", f1)
print("Aleatoriamente a média foi:", f2)