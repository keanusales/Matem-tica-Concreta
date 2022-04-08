n = int(input("Entre com o tamanho: "))
t, v, s = "O {}º termo é: ", [], 0
for i in range(n):
    v.append(int(input(t.format(i+1))))
for i in range(1, n):
    if v[i] > v[i-1]: s += v[i]
print("A soma dos maiores que seu anterior é:", s)