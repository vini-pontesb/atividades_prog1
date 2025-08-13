num1 = int(input("Adicione o primeiro número: "))
num2 = int(input("Adicione o segundo número: "))
num3 = int(input("Adicione o terceiro número: "))
maior = num1
if maior < num2:
    maior = num2
if maior < num3:
    maior = num3
print("O maior número é:", maior)
