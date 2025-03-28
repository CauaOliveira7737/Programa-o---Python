numero_impar = int(input("Insira um número ímpar: "))

if numero_impar % 2 == 0:
    print("O número inserido é par.")
else:
    numero_anterior = numero_impar - 2
    proximo_numero = numero_impar + 2
    diferenca_do_numero = (proximo_numero ** 2) - (numero_anterior ** 2)
    print(f"A diferença entre o quadrado de {proximo_numero} e {numero_anterior} é {diferenca_do_numero}.")
