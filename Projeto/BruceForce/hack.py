senha = -1
while senha not in range(0, 99999):
    senha = int(input('Digite uma senha de até 5 digitos:'))


while True:
    from random import randint
    compu = randint(0, 999999)
    print(compu)
    if compu == senha:
        print('Senha encontrada')
        print('A senha é:', senha)
        break

