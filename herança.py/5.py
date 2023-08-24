class Veiculos:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
class Carro(Veiculos):
    def __init__(self, marca, modelo, ano, rodas):
        super().__init__(marca, modelo, ano)
        self.rodas = rodas

class Moto(Veiculos):
    def __init__(self, marca, modelo, ano, rodas):
        super().__init__(marca, modelo, ano)
        self.rodas = rodas


Moto = Moto ('Suzuki','Hayabusa', 1999, 2 )
Carro = Carro ('toyota', 'corolla', 2022,4 )

print(Moto.marca, Moto.modelo, Moto.ano, Moto.rodas)
print(Carro.marca, Carro.modelo, Carro.ano, Carro.rodas)