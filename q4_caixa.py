def lerSaque():
    while True:
        saque = input("Informe o valor do saque: ")
        if not saque.isdigit():
            print("Digite um input válido")
            continue
        saque = int(saque)
        if saque > 1000:
            print("O saque máximo permitido é de R$1000,00")
            continue
        elif saque <= 0:
            print("O valor do saque deve ser um número inteiro positivo")
            continue
        break
    return saque

def minCedulas(saque, cedulas):
    min = []
    i = 0
    while i < len(cedulas):
        quant = saque // cedulas[i]
        saque %= cedulas[i]
        min.append(quant)
        i += 1

    return min


if __name__ == "__main__":
    cedulas = [200, 100, 50, 20, 10, 5, 2, 1]
    saque = lerSaque()
    quantCedulas = minCedulas(saque, cedulas)

    for i in range(len(cedulas)):
        print(f"Quantidade de cédulas {cedulas[i]}: {quantCedulas[i]}")