class Cachorros:
    def __init__(self, nome, cor_de_pelo, idade):
        self.nome = nome
        self.cor_do_pelo = cor_de_pelo
        self.idade = idade


cachorro = Cachorros('Vinicius', 'Branco', 21)
print(cachorro.nome)
print(cachorro.idade)
print(cachorro.cor_do_pelo)