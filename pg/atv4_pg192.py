while True:
    try:
        def verificacao(numero):
            if numero % 2 == 0:
                print('Seu número é par!')
            else:
                print('Seu número é impar!')
        n1 = int(input('Digite o número: '))
        verificacao(n1)
        break
    except ValueError:
        print('Você precisa digitar um número!')