class Cliente:
    def __init__(self, nome, cpf, salario, emprego, casa_propria, negativado):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.emprego = emprego
        self.casa_propria = casa_propria
        self.negativado = negativado

    def verificar_aprovacao(self):
        if self.negativado:
            return False
        elif not self.emprego or not self.salario or not self.casa_propria:
            return False
        elif self.salario * 1.5 < self.salario_declarado:
            return False
        else:
            return True

nome = input("Digite o nome do cliente: ")
cpf = input("Digite o CPF do cliente: ")
salario = float(input("Digite o salário do cliente: "))
emprego = input("O cliente possui emprego? (s/n): ").lower() == 's'
casa_propria = input("O cliente possui casa própria? (s/n): ").lower() == 's'
negativado = input("O cliente está negativado? (s/n): ").lower() == 's'
salario_declarado = float(input("Digite o salário declarado pelo cliente: "))

cliente = Cliente(nome, cpf, salario, emprego, casa_propria, negativado)
cliente.salario_declarado = salario_declarado

if cliente.verificar_aprovacao():
    print("Crédito aprovado para o cliente", cliente.nome)
else:
    print("Crédito negado para o cliente", cliente.nome)
