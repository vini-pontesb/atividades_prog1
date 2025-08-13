num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
soma = num1 + num2
while soma >= 0:
    print("O resultado ainda é positivo, tente novamente!")
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    soma = num1 + num2
print("O resultado negativo obtido foi:", soma)
