while True:
    try:
        def par(num):
            while num % 2 != 0:
                num = int(input("O número inserido é ímpar, insira um número par: "))
            print(f"O número escolhido foi {num} e ele é par!")
        numero = int(input("Insira um número par: "))
        par(numero)
        break
    except ValueError:
        print("Você não insireu um número! Tente novamente.")