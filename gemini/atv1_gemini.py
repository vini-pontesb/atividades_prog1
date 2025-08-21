while True:
    try:
        def calcular(n1, n2):
            soma = n1 + n2
            sub = n1 - n2
            prod = n1 * n2
            try:
                div = n1 / n2
            except ZeroDivisionError:
                print("Erro: Divisão por zero não é possível.")
            dic_resultados = {
                "Soma": soma,
                "Subtração": sub,
                "Produto": prod,
                "Divisão": div
            }
            return dic_resultados
        num1 = int(input("Insira um número qualquer: "))
        num2 = int(input("Insira outro número, tirando o 0: "))
        mensagem = calcular(num1, num2)
        print(mensagem)
        break
    except ValueError:
        print("Erro: Por favor, insira apenas números.")
