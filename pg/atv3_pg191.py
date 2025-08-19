#1
while True:
    try:
        def operacoes(n1, n2):
            soma = n1+n2
            sub = n1-n2
            div = n1-n2
            prod = n1*n2
            print(f'A soma dos valores informados é: {soma}')
            print(f'A subtração dos valores informados é: {sub}')
            print(f'A divisão dos dois valores informados é {div}')
            print(f'O produto dos valores informados é {prod}')
        n1 = float(input('Digite o valor do primeiro número: '))
        n2 = float(input('Digite o valor do segundo número: '))
        operacoes(n1, n2)
        break
    except ValueError:
        print('Valor inválido! Tente novamente.')

#2
while True:
    try:
        def operacoes(n1, n2):
            dic_resultados = {
                'Soma': n1+n2,
                'Subtração': n1-n2,
                'Divisão': n1/n2,
                'Produto': n1*n2
                }
            return dic_resultados
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        mensagem = operacoes(num1, num2)
        print(mensagem)
        break
    except ValueError:
        print('Valor inválido! Tente novamente.')