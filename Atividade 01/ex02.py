segundos = int(input("Insira o valor em s: "))

dia = segundos // 86400
hora = (segundos % 86400) // 3600
minuto = (segundos % 3600) // 60
segundos_rest = segundos % 60

print(f"{dia} dias, {hora} horas, {minuto} minutos e {segundos_rest} segundos.")
