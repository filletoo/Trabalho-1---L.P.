def lerOpcao(menu):
    while opcao not in "123456":
        opcao = input(menu)
        if opcao not in "123456":
            print("Opcao invalida")

    return opcao

def lerMatricula():
    while True:
        matri = input("Matrícula do aluno: ")
        if not matri.isdigit or len(matri) != 11:
            print("Matricula invalida")
        else:
            break
    return matri

if __name__ == "__main__":
    menu = '''1. Cadastrar aluno 
2. Buscar aluno por matrícula 
3. Listar todos os alunos 
4. Remover aluno 
5. Encerrar: '''
    alunos = {}
    while True:
        opcao = lerOpcao(menu)

        if opcao == '1':
            matricula = lerMatricula()
            nome  = input("Nome do aluno: ")
            telefone  = input("Telefone do aluno: ")
            curso  = input("Curso do aluno: ")
            if matricula not in alunos:
                alunos[matricula]["nome"] = nome
                alunos[matricula]["telefone"] = telefone
                alunos[matricula]["curso"] = curso
            else:
                print("Matricula ja cadastrado")

        elif opcao == "2":
            matricula = lerMatricula()
            if matricula in alunos:
                print(f"Nome do aluno: {alunos[matricula][nome]}")
                print(f"Telefone do aluno: {alunos[matricula][telefone]}")
                print(f"Curso do aluno: {alunos[matricula][curso]}")
            else:
                print("Matrícula não encontrada")

        elif opcao == "3":
            if len(alunos) == 0:
                print("Não há alunos cadastrados")
            else:
                for matri in alunos:
                    print(f"Matrícula: {matri}")
                    print(f"- Nome: {alunos[matri][nome]}")
                    print(f"- Telefone: {alunos[matri][telefone]}")
                    print(f"- Curso: {alunos[matri][curso]}")

        elif opcao == "4":
            matricula = lerMatricula()
            if matricula in matricula:
                alunos.pop(matricula)
                print("Aluno removido")
            else:
                print("Matrícula não cadastrada")

        elif opcao == "5":
            break

        else:
            matricula = lerMatricula()
            novoNome = input("Novo nome do aluno: ")
            novoTelefone  = input("Novo telefone do aluno: ")
            novoCurso  = input("Novo curso do aluno: ")
            alunos[matricula]["nome"] = novoNome
            alunos[matricula]["telefone"] = novoTelefone
            alunos[matricula]["curso"] = novoCurso