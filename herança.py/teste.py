# classe pai
class Carro:
    def __init__(self, nome, cor, marca):
        self.nome = nome
        self.cor = cor
        self.marca = marca
    def ligar(self):
        print("ligando", self.nome)

#outra classe pai   
class carro2:
    def __init__(self, ano):
      self.ano = ano
    def farol(self):
        print("acendendo as luzes")
    def acelerar(self):
        print("acelerando.....")  

# classe filho  
# neste caso minha classe filho só herdarão nome e a cor
# o super(). acessa as coisas da classe pai quando só existe uma classe pai
# para chamar mais de uma classe pai, deve se chamar o nome direto dela 
class Carrocitroem(Carro, carro2):
    def __init__(self,nome,cor, portas, ano):
        # super().__init__(nome,cor,"citroem")
        Carro.__init__(self,nome,cor,"citroem")
        carro2.__init__(self, ano)
        self.portas = portas
    def ligar(self):
        print("ligando", self.nome)

# aqui expus os valores de dois carros que ja tem a marca setada como citroem
car1 = Carrocitroem("C3","branco",4, 2018)
car2 = Carrocitroem("cactus","azul",9, 2020)
print(car1.nome, car1.cor, car1.marca, car1.portas, car1.ano)
print(car2.nome, car2.cor, car2.marca, car2.portas , car2.ano)