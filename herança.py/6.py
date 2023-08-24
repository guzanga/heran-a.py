class empregado:
    def __init__(self,nome,salario):
        self.nome = nome
        self.cor = salario

class gerente(empregado):
    def __init__(self,nome,salario, setor):
        super().__init__(nome,salario)
        self.setor = setor