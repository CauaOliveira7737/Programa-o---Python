print("CALCULAR MÉDIA")
print("")

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

print("")
print("Você deseja utilizar que média, digite:\n \nARITMÉTRICA [ A ] \nPONDERADA [ P ]")

tipo_media = input("")

if tipo_media == "A" or tipo_media == "a":
    media_a = (nota1 + nota2 + nota3)/3
    print("Essa é sua média aritmétrica: ", media_a)
    
elif tipo_media == "P" or tipo_media == "p":
    media_p1 = ((nota1*2) + (nota2*2) + (nota3*3))/ (2 + 2 + 3)
    media_p2 = ((nota1*1) + (nota2*2) + (nota3*2))/ (1 + 2 + 2)
    print(f"Essas foram as suas médias: {media_p1:.2f} e {media_p2:.2f}")

else:
    print("Opção inválida. Digite 'A' para média aritmética ou 'P' para média ponderada.")
