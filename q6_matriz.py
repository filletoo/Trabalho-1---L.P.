def lerN():
    while True:
        n = input("Indique a ordem da matriz: ")
        if not n.isdigit() or int(n) <= 0:
            print("Digite um valor inteiro positivo")
            continue
        n = int(n)
        break
    return n

def lerDados(n, i):
    valido = False
    while not valido:
        dados = input(f"Digite os valores da linha {i + 1}: ").split()
        if len(dados) < n: 
            print("Sequencia invalida")
            continue
        valido = True
        for i in range(len(dados)):
            if dados[i].isnumeric():
                dados[i] = int(dados[i])
            else:
                print("Sequencia invalida")
                valido = False
                break
        if not valido: continue
    return dados

def lerMatriz(n):
    matriz = []
    for i in range(n):
        linha = lerDados(n, i)
        matriz.append(linha)

    return matriz
if __name__=="__main__":
    n = lerN()
    matriz = lerMatriz(n)
    somas = []

    print("Matriz:")
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=" ")
        print()

    for linha in range(n):
        somaLinha = 0
        for elem in range(n):
            somaLinha += matriz[linha][elem]
        print(f"Soma da linha {linha + 1}: {somaLinha}")
        somas.append(somaLinha)

    for coluna in range(n):
        somaColuna = 0
        for elem in range(n): 
            somaColuna += matriz[elem][coluna]
        print(f"Soma da coluna {coluna + 1}: {somaColuna}")
        somas.append(somaColuna)

    linha = 0
    coluna = 0
    somaDigPrincipal = 0
    while linha < n and coluna < n:
        somaDigPrincipal += matriz[linha][coluna]
        linha += 1
        coluna += 1
    print(f"Soma da diagonal principal: {somaDigPrincipal}")
    somas.append(somaDigPrincipal)

    linha = 0
    coluna = n - 1
    somaDigSecundaria = 0
    while linha < n and coluna >= 0:
        somaDigSecundaria += matriz[linha][coluna]
        linha += 1
        coluna -= 1
    print(f"Soma da diagonal secundária: {somaDigSecundaria}")
    somas.append(somaDigSecundaria)

    quadMagico = True
    for i in somas:
        if i != somas[0]:
            quadMagico = False
            break

    if quadMagico:
        print("A matriz é um quadrado mágico")

    

    