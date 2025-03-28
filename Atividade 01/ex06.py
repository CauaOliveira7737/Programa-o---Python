num_primos = []
numero = 2

while len(num_primos) < 100:
    primo = True
    num = numero ** 0.5
    for x in range(2, int(num + 1)):
        if numero % x == 0:
            primo = False
            break

    if primo:
        num_primos.append(numero)
    numero += 1

for primo in num_primos:
    print(primo)
