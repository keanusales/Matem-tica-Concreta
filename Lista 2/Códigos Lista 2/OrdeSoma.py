n, s1, s2, s3 = int(input("Entre com o tamanho n: ")), 0, 0, 0
x, y, v = int(input("Valor de x: ")), int(input("Valor de y: ")), []
if x + y < n > 10 and y > x > 2:
    for i in range(n):
        v.append(float(input("Digite o {}º termo: ".format(i+1))))
    for i in range(x):
        s1 = s1 + v[i]
    for i in range(x, y):
        s2 = s2 + v[i]
    for i in range(y, n):
        s3 = s3 + v[i]
    if s1 > s2 and s1 > s3:
        print("A parte com a maior soma é:", v[:x])
        if s2 > s3:
            print("A parte com a 2ª maior soma é:", v[x:y])
            print("A parte com a 3ª maior soma é:", v[y:n])
        else:
            print("A parte com a 2ª maior soma é:", v[y:n])
            print("A parte com a 3ª maior soma é:", v[x:y])
    elif s2 > s3:
        print("A parte com a maior soma é:", v[x:y])
        if s1 > s3:
            print("A parte com a 2ª maior soma é:", v[:x])
            print("A parte com a 3ª maior soma é:", v[y:n])
        else:
            print("A parte com a 2ª maior soma é:", v[y:n])
            print("A parte com a 3ª maior soma é:", v[:x])
    else:
        print("A parte com a maior soma é:", v[y:n])
        if s1 > s2:
            print("A parte com a 2ª maior soma é:", v[:x])
            print("A parte com a 3ª maior soma é:", v[x:y])
        else:
            print("A parte com a 2ª maior soma é:", v[x:y])
            print("A parte com a 3ª maior soma é:", v[:x])
else: print("Digite valores inteiros onde y > x > 2 e x + y < n > 10!")