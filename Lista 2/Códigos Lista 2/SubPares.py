n = int(input("Entre com o tamanho: "))
t, v, s = "O {}º termo é: ", [], 0
for i in range(n):
    v.append(int(input(t.format(i+1))))
for i in range(n):
    if v[i] % 2 == 0: s += v[i]
print("A soma do subconjunto dos pares é:", s)