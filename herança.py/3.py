class forma():
    def __init__(self, p, a):
        self.p = p
        self.a = a
class retangulo(forma):
    def __init__(self,p,a):
        super().__init__(p,a)
    def area(self):
        mult = self.p * self.a
        print(mult)
   # def perimetro(self):

class triangulo(forma):
    def __init__(self,p,a):
        super().__init__(p,a)
    def area(self):
        mult = (self.p*self.a)/2
        print(mult)


   # def perimetro(self):
forma = forma(10,5)
triangulo = triangulo(10,9)
retangulo = retangulo(10,5)
retangulo.area()
triangulo.area()

