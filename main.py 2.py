class Aluno():
    def __init__(self, matricula, nome, idade, sexo,):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
aluno1 = Aluno(12312, 'joão', 17, 'masculino')
print('Matricula', aluno1.matricula)
print('Nome', aluno1.nome)
print('Idade',aluno1.idade)
print('sexo',aluno1.sexo)