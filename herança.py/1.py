class Pessoa:
    def init(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def init(self, nome, idade, matricula):
        super().init(nome, idade)
        self.matricula = matricula


aluno1 = Aluno("pedrin", 80, "23456")

print("Nome:", aluno1.nome)
print("Idade:", aluno1.idade)
print("Matrícula:", aluno1.matricula)