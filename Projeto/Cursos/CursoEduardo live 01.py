# criando classes de forma simples
class comput:
    def __init__(self):
        self.marca = 'Asus'
        self.processador = 'AMD'


marcapc = comput()
procepc = comput()
print(procepc.processador)
print(marcapc.marca)
print()


# classe de forma mais complexa


class comput:
    def __init__(self, placa, memória, video):
        self.placa = placa
        self.memória = memória
        self.video = video


pc1 = comput('Asus', '8GB', 'Nvidia')
pc2 = comput('Gigabyte', '12GB', 'Radeon')
print(pc1.placa, pc1.memória, pc1.video, pc1.video)
print(pc2.placa, pc1.memória, pc1.video, pc1.video)

# verifica se o comando está certo, afirma o comando
import unittest

assert 3 == 3, '3 não é maior que 3'


def soma(x, y):
    return x + y


def par(num):
    try:
        return True if num % 2 == 0 else False
    except TypeError:
        return 'Digite apenas número'


class test(unittest.TestCase):
    def test(self):
        self.assertEqual(soma(5, 6), 11)


class test_errado(unittest.TestCase):
    def test(self):
        self.assertEqual(soma(5, 6), 11)


class test_par(unittest.TestCase):
    def test(self):
        self.assertEqual(par('n'), False)

