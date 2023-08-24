class Bebida:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

class Refrigerante(Bebida):
    def __init__(self, nome, tipo, sabor, tamanho):
        super().__init__(nome, tipo)
        self.sabor = sabor
        self.tamanho = tamanho

class Cafe(Bebida):
    def __init__(self, nome, tipo):
        super().__init__(nome, tipo)

refrigerante = Refrigerante("Coca-Cola", "Refrigerante", "Coca-Cola", "1L")
cafe = Cafe("CafÃ©", "Cafe")

print(refrigerante.nome, refrigerante.tipo, refrigerante.sabor, refrigerante.tamanho)
print(cafe.nome, cafe.tipo)