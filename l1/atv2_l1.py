num = float(input("Informe um número: "))
if num < 0:
    print("O número escolhido foi:", num, "e ele é negativo")
else:
    if num > 0:
        print("O número escolhido foi:", num, "e ele é positivo")
    else:
        print("O número escolhido foi:", num, "e ele é zero")
