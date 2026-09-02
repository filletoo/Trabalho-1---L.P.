def calcPontuacao(senha, min):
    pontuacao = 0
    letraMaius = False
    letraMinus = False
    digito = False
    especial = False

    if len(senha) >= min:
        pontuacao += 1
    for char in senha:
        if char.isupper():
            letraMaius = True
        elif char.islower():
            letraMinus = True
        elif char.isdigit():
            digito = True
        elif not char.isalnum():
            especial = True

    if letraMaius: pontuacao += 2
    if letraMinus: pontuacao += 2
    if digito: pontuacao += 3
    if especial: pontuacao += 4

    return pontuacao

if __name__=="__main__":
    senha = input("Digite a senha: ")
    pontuacao = calcPontuacao(senha, 6)

    print(f"Pontuação: {pontuacao}")
    if pontuacao <= 4:
        print("Senha fraca")
    elif pontuacao >= 5 and pontuacao <= 8:
        print("Senha média")
    else:
        print("Senha forte")