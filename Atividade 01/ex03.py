mercadorias_compradas = float(input("Qual o valor total da mercadorias compradas? "))

if mercadorias_compradas > 500:
    taxa = (mercadorias_compradas * 0.5)
    print("Você foi TAXADO")
    print(f"Valor da taxa aplicada é de R${taxa}")
    print(f"Valor total: R${taxa + mercadorias_compradas}")

else:
    print("Você não foi TAXADO.")
    print(f"Valor total: R${mercadorias_compradas}")
