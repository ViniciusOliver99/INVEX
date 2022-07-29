while True:
    from random import randint
    print('=== Criador de Senhas ===')
    quant = int(input('Quantidades de caracteres: '))


    def a():
        for a in range(quant):
            aleat = randint(0, 60)
            letra = 'QWERTYUIOPPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789'
            digito = letra[aleat]
            print(digito, end='')
    for c in range(8):
        print(f'Senha {c + 1}:', end=' ')
        a()
        print()