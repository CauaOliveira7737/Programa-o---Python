salario = float(input("Insira o salário inicial: "))
anos = int(input("Insira a quantidade de anos: "))
acrescimo = float(input("Insira o aumento inicial (%): "))

salario_atual = salario

for ano in range(1, anos + 1):
    salario_atual += salario_atual * (aumento / 100)
    aumento *= 2

print(f"O salário após {anos} anos é de R${salario_atual}")
