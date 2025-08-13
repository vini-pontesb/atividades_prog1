n1 = float(input("Insira a nota 1: "))
n2 = float(input("Insira a nota 2: "))
n3 = float(input("Insira a nota 3: "))
media = round((n1+n2+n3)/3, 2)
if media >= 7:
    print("Você tirou", media, "e foi aprovado!")
else:
    if media < 7 and media >= 5:
        print("Você tirou", media, "e está de recuperação!")
    else:
        print("Você tirou", media, "e está reprovado!")
