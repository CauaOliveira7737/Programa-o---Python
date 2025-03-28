valor = int(input("Insira um número inteiro (maior que 1): "))

if valor <= 1:
    print("O número deve ser maior que 1.")
else:
    num_primo = True
    x = valor ** 0.5
    for x in range(2, int(x + 1)):
        if valor % x == 0:
            num_primo = False
            break
    if num_primo:
        print(f"{valor} é um número primo.")
    else:
        print(f"{valor} não é um número primo.")
