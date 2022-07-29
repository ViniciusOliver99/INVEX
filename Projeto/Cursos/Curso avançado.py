from collections import Counter
from time import sleep

# List comprehensions

lista = [v for v in range(1, 11)]
print(lista)

lista_2 = [(a, b) for a in (1, 2, 3) for b in ('a', 'b', 'c')]
print(lista_2)

lista_3 = [(a, b) for a in (1, 2, 3) for b in ('a', 'b', 'c') if a % 2 == 0]
print(lista_3)

lista_4 = [[i for i in range(4)] for v in range(4)]
print(lista_4)

# ler letras de um arquivo
with open('123.txt', 'r') as t:
    text = t.read()

chars = []
chars2 = set()
notchars = []
posic = []
iguais = []
iguais_2 = []
iguaisposi = []
index = 0
num = 0

for c in text:
    chars2.add(c)

for c in text:
    num += 1
    if c not in chars:
        chars.append(c)
    else:
        notchars.append(num)
        iguais_2.append(c)


def fun(text):
    return Counter(text).most_common(3)


print('Letras sem se reptiram:', chars)
print('Posião das letras que repetem:', notchars)
print('Letras que reptiram:', iguais_2)
print('Letras sem se reptiram usando o set:', chars2)
print('Letras que mais se reptiram:', fun(text))


def aa(limit=10):
    n = 1
    while True:
        n += 2
        if n > limit:
            return
        yield n


def bb(limit=10):
    n = 0
    while True:
        n += 2
        if n > limit:
            return
        yield n


def dois(g1, g2):
    yield from aa()
    yield from bb()


for i in dois(aa(), bb()):
    print(i)


# Exemplo de yield


def gen():
    print('meu nome é:')
    yield 'Vinicius'
    print('e o seu vai ser esse')
    yield 'Carlos'


g = gen()

for x in g:
    print(x)
# esse já não repete mais nada
for x in g:
    print(x)

# ai para ele aparecer de novo deve-se adicionar a variavel de novo tbm
g = gen()

for x in g:
    print(x)

with open('marco.txt', 'w') as file:
    file.write('''“Não desperdice o que resta da sua vida ao especular sobre seus vizinhos. 
Qualquer coisa que o distraia da fidelidade ao Governante dentro de você significa uma perda de oportunidade para alguma outra tarefa. ”
- Marco Aurélio''')

marco = open('marco.txt')

# a cada print é mostrado uma linha do gerador
sleep(0.1)
print(next(marco))
sleep(0.1)
print(next(marco))
sleep(0.1)
print(next(marco))
sleep(0.1)


def bom(ate):
    yield from range(1, ate)


b = bom(10)

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print()


def y():
    yield from [1, 2, 4, 5, 6, 7]


y = y()

print(next(y))

