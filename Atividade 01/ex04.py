km = float(input("Quantos km você pecorreu? "))
dias = int(input("Quantos dias você pecorreu? "))

valor_dias = dias * 90
if km > 100:
    km_ultrapassados = km - 100
    valor_taxa_km = km_ultrapassados * 12
    valor_total = valor_taxa_km + valor_dias
    print(f"Valor total a ser pago é {valor_total}")

else:

    print(f"Valor total a ser pago é {valor_dias}")
