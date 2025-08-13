"""1"""
while True:
    try:
        def lista(*args):
            total = 0
            for numero in args:
                total += numero
            print(total)
        lista(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        break
    except ValueError:
        print("Valor inválido, insira um número")

"""2"""
while True:
    try:
        def lista(*args):
            total = sum(args)
            print(total)
        lista(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        break
    except ValueError:
        print("Valor inválido, insira um número")
