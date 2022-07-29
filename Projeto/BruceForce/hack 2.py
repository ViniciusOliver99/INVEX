from random import random, choice
import string
from itertools import combinations_with_replacement


valores = string.ascii_letters + string.digits
tamanho = 5
senha = ' '

list = combinations_with_replacement(['adc'], 3)

print(list)

for c in range(tamanho):
    compu = choice(valores)
    senha += compu

print(senha)
tentativas = 0
while True:
    hack = ''
    compu = choice(valores)
    for c in range(tamanho):
        compu = choice(valores)
        hack += compu

    tentativas += 1
    print('Tentativa:', tentativas)
    if senha == hack:
        print('A senha é:', hack)
        break
