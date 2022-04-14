n, s1, s2, s3 = int(input("Entre com o tamanho n: ")), 0, 0, 0
x, y, v = int(input("Valor de x: ")), int(input("Valor de y: ")), []
if 1 < x < y < n > 10:
    for i in range(n):
        v.append(float(input("Digite o {}º termo: ".format(i+1))))
    for i in range(x): s1 = s1 + v[i] # Faz a soma do subconjunto x
    for i in range(x, y): s2 = s2 + v[i] # Faz a soma do subconjunto y
    for i in range(y, n): s3 = s3 + v[i] # Faz a soma do subconjunto n
    if s1 < s2 and s1 < s3: # Caso do subconjunto x ser o menor
        print("A parte com a 3ª maior soma é:", v[:x])
        if s2 < s3: # Depois verifica se o sub. y é o 2º menor
            print("A parte com a 2ª maior soma é:", v[x:y])
            # E depois exibe o subconjunto n como o maior
            print("A parte com a maior soma é:", v[y:n])
        else: # Caso contrário, o sub. n é o 2º menor
            print("A parte com a 2ª maior soma é:", v[y:n])
            # E o subconjunto y é exibido como maior
            print("A parte com a maior soma é:", v[x:y])
    elif s2 < s3: # Agora, o caso do sub. y ser o menor
        print("A parte com a 3ª maior soma é:", v[x:y])
        if s1 < s3: # Verifica se o sub. x é o 2º menor
            print("A parte com a 2ª maior soma é:", v[:x])
            # E depois exibe o subconjunto n como o maior
            print("A parte com a maior soma é:", v[y:n])
        else: # Caso contrário, o sub. n é o 2º menor
            print("A parte com a 2ª maior soma é:", v[y:n])
            # E o subconjunto x é exibido como maior
            print("A parte com a maior soma é:", v[:x])
    else: # Agora, o caso do sub. n ser o menor
        print("A parte com a 3ª maior soma é:", v[y:n])
        if s1 < s2: # Verifica se o sub. x é o 2º menor
            print("A parte com a 2ª maior soma é:", v[:x])
            # E depois exibe o subconjunto y como o maior
            print("A parte com a maior soma é:", v[x:y])
        else: # Caso contrário, o sub. y é o 2º menor
            print("A parte com a 2ª maior soma é:", v[x:y])
            # E o subconjunto x é exibido como maior
            print("A parte com a maior soma é:", v[:x])
else: print("Digite valores inteiros tal que 1 < x < y < n > 10!")