num = int(input("Insira um número: "))
i = num
fat = 1
if num < 0:
    print("Não existe fatorial de número de negativo")
else:
    if num == 0:
        print("O fatorial do número", num, "é: 1")
    else:
        while i >= 1:
            fat = fat * i
            i = i - 1
        print("O fatorial do número", num, "é:", fat)
