turmas = int(input("Insira a quantidade de turmas: "))
alunos_turma = []

for i in range(turmas):
    alunos = int(input(f"Insira a quantidade de alunos da turma {i+1}: "))
    alunos_turma.append(alunos)
    if alunos > 40:
        print(f"A turma {i+1} tem mais de 40 alunos.")

media = sum(alunos_turma) / turmas
print(f"A média de alunos por turma é: {media:.2f}")
