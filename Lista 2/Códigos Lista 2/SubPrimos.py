n = int(input("Entre com o tamanho: "))
# Recebe o tamanho do vetor
t, v, d, s = "O {}º termo é: ", [], 0, 0
for i in range(n):
    v.append(int(input(t.format(i+1))))
    # Recebe os termos do vetor
for i in range(n):
    # Abaixo há a verificação se é primo
    # Se for, d (divisores) será igual a 2
    for j in range(1, v[i] + 1):
        if v[i] % j == 0: d += 1
        if d == 3: break
    if d == 2: s += v[i]
    d = 0 # O d é zerado para o próximo número
print("A soma do subconjunto dos primos é:", s)