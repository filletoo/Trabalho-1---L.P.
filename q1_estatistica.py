def lerDados():
    valido = False
    while not valido:
        dados = input("Digite a sequência de numeros inteiros:\n").split()
        if len(dados) == 0: 
            print("Sequencia invalida")
            continue
        valido = True
        for i in range(len(dados)):
            if dados[i].isdigit():
                dados[i] = int(dados[i])
            else:
                print("Sequencia invalida")
                valido = False
                break
        if not valido: continue
    return dados

def maiorMenor(dados):
    maior = dados[0]
    menor = dados[0]
    for i in dados:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i

    return maior, menor

def quantParImp(dados):
    par = 0
    impar = 0
    for i in dados:
        if i % 2 == 0:
            par += 1
        else:
            impar += 1

    return par, impar

if __name__ == "__main__":
    dados = lerDados()

    quantElem = len(dados)
    maior, menor = maiorMenor(dados)
    soma = sum(dados)
    media = soma/quantElem
    quantPar, quantImp = quantParImp(dados)
    quantDistintos = len(set(dados))

    print(f"Quantidade de elementos:", quantElem)
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Soma dos valores: {soma}")
    print(f"Media aritmetica: {media:.2f}")
    print(f"Quantidade de numeros pares: {quantPar}")
    print(f"Quantidade de numeros impares: {quantImp}")
    print(f"Quantidade de valores distintos: {quantDistintos}")

    

