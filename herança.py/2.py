class animal:
    def fazer_som(self):
        print("piu piu")
        
class cachorro(animal):
    def fazer_som(self):
        print("au au")

class gato(animal):
    def fazer_som(self):
        print("miau")
    
class vaca(animal):
    def fazer_som(self):
        print("mu mu")
    
cachorro = cachorro()
cachorro.fazer_som()