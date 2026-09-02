if __name__ == "__main__":
    alunos = {}

    while True:
        nome = input("Nome do aluno: ")
        if nome == "0":
            break

        if nome not in alunos:
            notas = input("Digite as três notas do alunos: ").split()
            for i in range(len(notas)):
                notas[i] = int(notas[i])
            alunos[nome] = notas
        else:
            print("Notas do aluno já cadastradas")

    medias = []
    aprovados = 0
    for nome in alunos:
        print(f"Aluno {nome}:")
        soma = 0
        for i in range(3):
            soma += alunos[nome][i]
            print(f"Nota {i + 1}: {alunos[nome][i]}")
        media = soma/3
        medias.append(media)
        print(f"Media: {media}")
        print("Situação:", end="")
        if media >= 7:
            print("Aluno aprovado")
            aprovados += 1
        elif media >= 4:
            print("Aluno de recuperação")
        else:
            print("Aluno reprovado")

    mediaGeral = sum(medias)/len(medias)
    maiorMedia = max(medias)
    menorMedia = min(medias)
    percentualAprov = aprovados/len(alunos)*100

    print(f"Média geral da turma: {mediaGeral}")
    print(f"Maior média da turma: {maiorMedia}")
    print(f"Menor média da turma: {menorMedia}")
    print(f"Percentual de alunos aprovados da turma: %{percentualAprov:.2f}")

