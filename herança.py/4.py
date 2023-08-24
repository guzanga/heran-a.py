class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Livro(Produtos):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

class Eletronico(Produtos):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


Livro = Livro("Livro", 50, 'Autor' )
Eletronico = Eletronico("Computador Pichau Gamer", 4000, 850)

print(Livro.nome, Livro.preco, Livro.autor)
print(Eletronico.nome, Eletronico.preco, Eletronico.voltagem)