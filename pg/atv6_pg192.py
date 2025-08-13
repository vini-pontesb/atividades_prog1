while True:
    try:
        def inteiro(num):
            i = 0
            while i < num:
                if i % 2 != 0:
                    print(i)
                i += 1
            print(num)
        numero = int(input("Insira um número: "))
        inteiro(numero)
        break
    except ValueError:
        print("Valor inválido, insira um número inteiro")
