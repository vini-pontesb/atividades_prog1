# 1
def usuario(nome, sobrenome):
    print(f'Ola {nome} {sobrenome}! Seja bem-vindo a esse sistema!')


name = input('Digite seu primeiro nome: ')
surname = input('Digite seu sobrenome: ')
usuario(name, surname)

# 2


def usuario(nome, sobrenome):
    return f'Olá {nome} {sobrenome}! Seja bem-vindo a esse sistema!'


name = input('Digite seu primeiro nome: ')
surname = input('Digite seu sobrenome: ')
mensagem = usuario(name, surname)
print(mensagem)
