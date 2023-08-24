class Instrumento:
    def tocar(self):
        print("Tocando um instrumento")

class Violino(Instrumento):
    def tocar(self):
        print("Tocando um violino")

class Piano(Instrumento):
    def tocar(self):
        print("Tocando um piano")

class Flauta(Instrumento):
    def tocar(self):
        print("Tocando uma flauta")

violino = Violino()
violino.tocar()

piano = Piano()
piano.tocar()

flauta = Flauta()
flauta.tocar()