import random
num_aleatorio = random.randint(1, 10)
num_escolhido = int(input("Insira um número, de 1 a 10, para testar se é o número aleatório: "))
while num_aleatorio != num_escolhido:
    print("Tente novamente até acertar o número")
    num_escolhido = int(input("Insira um número, de 1 a 10, para testar se é o número aleatório: "))
print("Você acertou o número, que era o:", num_aleatorio) 
