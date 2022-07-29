    import re


def menu():
    while True:
        print('_' * 30)
        print('MENU PRINCIPAL')
        print('_' * 30)
        print('''
            1 - Ver pessoa cadastrada:
            2 - Cadastrar pessoa:
            ''')

        try:

            op = int(input('Sua opção:'))
            while op >= 4:
                print('\033[0;31mErro, digite apenas os números das opções acima.\033[m')
                op = int(input('Sua opção:'))
            while op <= 0:
                print('\033[0;31mErro, digite apenas os números das opções acima.\033[m')
                op = int(input('Sua opção:'))

        except(ValueError):
            print('\033[0;31mErro, Digite apenas números inteiros\033[m')
            menu()

        if op == 1:
            print('_'*30)
            print('OPÇÃO 1'.center(30))
            print('_'*30)

        if op == 2:
            print('_'*30)
            print('CADASTRO DE PESSOAS'.center(30))
            print('_'*30)

            listp = list()
            listi = list()
            while True:
                nome = str(input('Nome do primeiro cadastro:'))
                listp += [nome]
                listps = str(listp)
                listpss = listps.replace("'", '')
                listpsss = listpss.replace('[', '')
                listpssss = listpsss.replace(']', '')
                idade = str(input('Qual é a sua idade:'))
                cont = str(input('Cadastrar mais uma pessoa ?')).strip().upper()[0]
                listi += [idade]
                listis = str(listi)
                listiss = listis.replace("'", '')
                listisss = listiss.replace('[', '')
                listissss = listisss.replace(']', '')
                if cont == 'S':
                    print('Próximo')

                elif cont == 'N':
                    print('Nome:', listpssss)
                    print('Idade:', listissss)
                    break

            cont = str(input('Quer encerrar o programada ?')).strip().upper()[0]
            while cont not in 'SN':
                print('\033[0;31mOpção invalida, Digite apenas sim ou não\033[0;31')
                cont = str(input('Quer encerrar o programada ?')).strip().upper()[0]
            if cont == 'S':
                print('Até')
                break


menu()


